from tensorflow.keras.applications import VGG16
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Input
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.models import load_model

import os
from collections import deque
import numpy as np
import argparse
import cv2

from fpdf import FPDF


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True, help="path to input images folder")
ap.add_argument("-m", "--model", required=True, help="path to model (.h5)")
ap.add_argument("-o", "--output", required=True, help="path to the output pdf (.pdf)")
args = vars(ap.parse_args())

def get_model():
    # load the VGG16 network, ensuring the head FC layer sets are left
    # off
    baseModel = VGG16(weights="imagenet", include_top=False,input_tensor=Input(shape=(224, 224, 3)))

    # construct the head of the model that will be placed on top of the
    # the base model
    headModel = baseModel.output
    headModel = Flatten(name="flatten")(headModel)
    headModel = Dense(512, activation="relu")(headModel)
    headModel = Dropout(0.5)(headModel)
    headModel = Dense(1, activation="sigmoid")(headModel)

    # place the head FC model on top of the base model (this will become
    # the actual model we will train)
    model = Model(inputs=baseModel.input, outputs=headModel)

    # loop over all layers in the base model and freeze them so they will
    # *not* be updated during the first training process
    for layer in baseModel.layers:
        layer.trainable = False

    # compile our model (this needs to be done after our setting our
    # layers to being non-trainable
    print("[INFO] compiling model...")
    opt = SGD(lr=1e-6, momentum=0.9)
    model.compile(loss="binary_crossentropy", optimizer=opt,metrics=["accuracy"])
    return model

model = get_model()
model.load_weights(args["model"])


print("[INFO] Generating Predictions...")
preds = []
filename_list = []

for filename in os.listdir(args["input"]):
    #print(filename, end=' ')
    filename_list.append(filename)
    preds_temp = []
    frame = cv2.imread(args["input"]+"//"+filename)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = frame.copy()
    frame = cv2.resize(frame, (224, 224))
    frame = frame.astype("float32")
    preds.append((output, model.predict(np.expand_dims(frame, axis=0))[0][0]))
    
preds = np.array(preds)

print("[INFO] Generating \"hasar_oranlari.pdf\"...")

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=20, style='B')
pdf.cell(190, 10, txt="HASAR ORANLARI", ln=1, align="C")
pdf.set_font("Arial", size=12)


for i, f_id in enumerate(preds[:,1].argsort()[::-1]):
    if(i % 2 == 0):
        if(i != 0):
            pdf.add_page()
            pdf.ln(10)
        pdf.image(args["input"]+"//"+filename_list[f_id], x=55, y=30, w=100, h=100)
        pdf.ln(110)
    else:
        pdf.image(args["input"]+"//"+filename_list[f_id], x=55, y=160, w=100, h=100)
        pdf.ln(120)
    pdf.cell(190, 10, txt="Hasar Ihtimali: %{:.2f}".format(preds[f_id][1]*100), ln=1, align='C')

pdf.output(args["output"])

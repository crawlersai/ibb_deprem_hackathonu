# HATİS Model ve DEMO Notebooklar

Bu klasörde modelimizi eğittimiz ve bu eğitilmiş modeli kullanrak demolar yaptığımız notebook'ları bulabilirsiniz. predict notebooklarının çalışabilmesi için eğitim sonucunda elde edilen modele ihtiyaç vardım (model.h5). Şu linkten modele ulaşabilirsiniz: https://drive.google.com/file/d/1-SOSeEpjh3-k49o7le4brna9A13Xs1ll/view?usp=sharing

## model

Bu notebook gelistirdiğimiz makine öğrenmesi algoritmasının ayrıntılarını ve algoritmanın eğitim sürecini içerir.

## predict_video

Bu notebook kullanıcıdan bir adet video alır. Geliştirdiğimiz makine öğrenmesine sokulan video, sol üst köşesine tahmin edilen hasarlı olma ihtimalinin anlık değişimi bastırılarak verilen lokasyona kaydedilir.

[![Drone Hasar Tespit Videosu](https://www.youtube.com/watch?v=G46-tUq9-20/0.jpg)](https://www.youtube.com/watch?v=G46-tUq9-20)

## predict_image

Bu notebook kullanıcıdan bir adet resim alır. Geliştirdiğimiz makine öğrenmesine sokulan resim, sol üst köşesine tahmin edilen hasarlı olma ihtimali bastırılarak verilen lokasyona kaydedilir.

![deprem_ornek](../figures/deprem_ornek.png) 

## predict_pdf

Bu notebook kullanıcıdan bir adet resimler içeren klasör alır. Bütün resimler öncelikle geliştirdiğimiz makine öğrenmesine sokulur. Çıktı olarak ise resimler ve resimlerin hasarlı olma ihtimallerinin bulunduğu bir pdf oluşturabilirsiniz. Oluşturulan PDF'te resimler hasar ihtimali en yüksekten en düşüğe doğru sıralanacaklardır. Ayrıca IPython Widget'ları ile notebook üzerinden resimleri tek tek inceleyebilirsiniz (Bunun için notebook'u uygun bir ortamda (lokalinizde veya Colab gibi) çalıştırmanız gerekir).

[Hasar Ihtimalleri PDF](hasar_ihtimalleri.pdf))
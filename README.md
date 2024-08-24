# Senkronize Sanal Mikroskop

Bu proje, iki farklı mikroskopik görüntünün (HE ve PR boyaları) aynı anda senkronize bir şekilde görüntülenmesini sağlar. Ayrıca, bu iki görüntüdeki ortak noktaları kullanarak görüntüleri doğru hizalamak için gerekli X, Y kaydırma ve döndürme değerlerini hesaplamaya yardımcı olan bir Python aracı sunar.

## Proje Yapısı

Proje dosya yapısı aşağıdaki gibidir:

```
/he
    ├── output.dzi
    └── output_files/
/pr
    ├── output.dzi
    └── output_files/
README.md
image1.html
image2.html
index.html
senkronizekoordinatlar.PNG
senkronizekoordinatlar.py
```

- **/he ve /pr**: HE ve PR boyalı mikroskopik görüntülerin dizinleridir. Bu dizinler, OpenSeadragon tarafından kullanılan Deep Zoom Image (DZI) formatındaki görüntü dosyalarını barındırır.
- **image1.html ve image2.html**: Bu dosyalar, HE ve PR görüntülerini ayrı ayrı görüntülemek için kullanılır. Kullanıcı bu dosyalar aracılığıyla iki görüntüdeki ortak noktaları bulabilir.
- **index.html**: İki görüntüyü aynı anda senkronize olarak gösteren ana HTML dosyasıdır.
- **senkronizekoordinatlar.py**: İki görüntüdeki ortak noktaları kullanarak gerekli X, Y kaydırma ve döndürme değerlerini hesaplayan Python scriptidir.
- **senkronizekoordinatlar.PNG**: Python scripti çalıştırıldıktan sonra elde edilen sonuçların ekran görüntüsüdür.

## Kurulum ve Kullanım

### 1. Görüntüleri Fayanslara Ayırma

SVS dosyalarınızı, OpenSeadragon tarafından kullanılabilecek bir formata dönüştürmek için aşağıdaki adımları izleyin. VIPS kütüphanesini kullanarak .svs dosyasını fayanslara ayırabilirsiniz:

```bash
vips dzsave input.svs output_folder
```

Bu komut, `input.svs` dosyasını `output_folder` adında bir klasöre `dzi` formatında kaydeder.

### 2. Görüntüleri İnceleme ve Ortak Nokta Belirleme

1. **Görüntüleri Açın**: `image1.html` ve `image2.html` dosyalarını tarayıcıda ayrı ayrı pencerelerde açın. Bu dosyalar, HE ve PR görüntülerini ayrı ayrı incelemenizi sağlar.
2. **Ortak Noktaları Bulun**: İki görüntüde de aynı olan noktaları belirleyin ve bu noktaların X, Y koordinatlarını, Zoom ve Rotasyon değerlerini kaydedin. Aşağıdaki örnek formatta bu bilgileri elde edebilirsiniz:

   ```
   image1.png;0.75;0.89;13.37;0.00°
   image2.png;0.75;0.88;13.09;0.00°
   ```

### 3. Senkronizasyon Kodunu Hesaplama

1. **Python Scriptini Çalıştırın**: `senkronizekoordinatlar.py` dosyasını çalıştırın. Aşağıdaki komut ile Python scriptini çalıştırabilirsiniz:

   ```bash
   python senkronizekoordinatlar.py
   ```

2. **Koordinatları Girin**: Elde ettiğiniz ortak nokta bilgilerini aşağıdaki formatta girin:

   ```
   image1.png;0.75;0.89;13.37;0.00°
   image2.png;0.75;0.88;13.09;0.00°
   ```

   Bu adımı 10 adet ortak nokta için yapabilirsiniz.

3. **Kodları Kopyalayın**: "Kaydet ve Göster" tuşuna bastığınızda, hesaplanan X, Y kaydırma ve döndürme kodları ekranda gösterilecektir. Bu kodları "Kodu Kopyala" tuşuna basarak kopyalayabilirsiniz.

### 4. Kodları `index.html` Dosyasına Ekleyin

1. **Kopyalanan Kodları Yapıştırın**: `senkronizekoordinatlar.py` dosyasından elde ettiğiniz kodları `index.html` dosyanızın `viewer1` konfigürasyonu altına ekleyin. Örneğin:

   ```html
   viewer1.viewport.panBy(new OpenSeadragon.Point(0.0220, 0.0060));
   viewer1.viewport.setRotation(0.00);
   ```

2. **index.html'i Tarayıcıda Açın**: `index.html` dosyasını tarayıcıda açarak, senkronize edilmiş iki görüntüyü inceleyin.

## Ekran Görüntüsü

Aşağıdaki ekran görüntüsü, `senkronizekoordinatlar.py` dosyasını çalıştırdıktan sonra elde edilen sonuçları göstermektedir:

![senkronizasyon sonucu](https://raw.githubusercontent.com/metinciris/senkronize/main/senkronizekoordinatlar.PNG)


## Demo 

Demo bakın https://metinciris.github.io/senkronize/

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakabilirsiniz.



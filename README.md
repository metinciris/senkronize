
# Senkronize Sanal Mikroskop

Bu proje, iki farklı mikroskopik görüntünün (HE ve PR boyaları) aynı anda senkronize bir şekilde görüntülenmesini sağlar. Kullanıcılar, her iki görüntüde de eş zamanlı olarak dolaşabilir, yakınlaştırabilir ve görüntüyü döndürebilir. HE ve PR görüntüleri arasındaki pozisyon farkını düzeltmek için ince senkronizasyon ayarları yapılmıştır.

## Demo

Projenin canlı demosuna aşağıdaki bağlantıdan ulaşabilirsiniz:

[Senkrnoize Sanal Mikroskop Demo](https://metinciris.github.io/senkronize/)

## Kullanım

Bu proje, OpenSeadragon kütüphanesini kullanarak iki mikroskopik görüntüyü senkronize eder. README.md dosyasındaki kod, proje dizin yapısına ve OpenSeadragon'un kullanımıyla ilgili temel bilgilere yer verir.

## Dizin Yapısı

Projenin dizin yapısı şu şekildedir:

```
/senkronize/
    ├── index.html
    ├── /he/
    │   ├── output.dzi
    │   └── output_files/
    ├── /pr/
        ├── output.dzi
        └── output_files/
```

- **`index.html`**: Projenin ana HTML dosyasıdır. HE ve PR görüntülerinin senkronize bir şekilde görüntülenmesini sağlar.
- **`/he/`** ve **`/pr/`**: HE ve PR görüntü dosyalarını içeren dizinlerdir. Bu dizinler, OpenSeadragon tarafından kullanılan Deep Zoom Image (DZI) formatındaki görüntü dosyalarını barındırır.

## OpenSeadragon Kullanımı

Bu proje, [OpenSeadragon](https://openseadragon.github.io/) JavaScript kütüphanesini kullanarak yüksek çözünürlüklü mikroskopik görüntülerin web üzerinde senkronize şekilde görüntülenmesini sağlar.

### Senkronizasyon Ayarları

Görüntüler arasındaki pozisyon farkını düzeltmek için `panBy` fonksiyonu kullanılarak HE görüntüsü PR'ye göre hafifçe kaydırılmıştır.

```javascript
viewer1.viewport.panBy(new OpenSeadragon.Point(0.01, 0.01));
```

Bu ayarlar, X ve Y ekseninde kaydırma yaparak görüntülerin senkronize olmasını sağlar.

## Katkıda Bulunma

Katkıda bulunmak isterseniz, lütfen bir `pull request` gönderin veya bir `issue` açarak geri bildirimde bulunun.

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakabilirsiniz.
```

Bu `README.md` dosyası, projenizin ana özelliklerini, dosya yapısını, kullanımını ve OpenSeadragon'u nasıl entegre ettiğinizi açıklar. Ayrıca, demo bağlantısını ekledim, böylece ziyaretçiler kolayca projeyi deneyebilirler. README dosyasını ihtiyacınıza göre özelleştirebilirsiniz!

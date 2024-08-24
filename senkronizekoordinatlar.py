import numpy as np

def calculate_transform(coords1, coords2):
    # Koordinatları numpy array'ine dönüştür
    points1 = np.array(coords1)
    points2 = np.array(coords2)

    # Her iki koordinat setinin merkezini hesapla
    center1 = np.mean(points1, axis=0)
    center2 = np.mean(points2, axis=0)

    # X ve Y kaydırma miktarlarını hesapla
    delta_x = center2[0] - center1[0]
    delta_y = center2[1] - center1[1]

    # Zoom farkı hesaplama
    zoom1 = np.mean([c[2] for c in coords1])
    zoom2 = np.mean([c[2] for c in coords2])
    zoom_factor = zoom2 / zoom1

    # Eğer rotasyon açısı da dahil edilecekse
    rotation1 = np.mean([c[3] for c in coords1])
    rotation2 = np.mean([c[3] for c in coords2])
    delta_rotation = rotation2 - rotation1

    return delta_x, delta_y, zoom_factor, delta_rotation

def main():
    # Ortak noktaların koordinatları (image1, image2)
    coords1 = [
        [0.49, 0.57, 23.10, 0.00],
        [0.73, 0.73, 23.10, 0.00],
        [0.45, 0.92, 13.37, 0.00],
        [0.75, 0.89, 13.37, 0.00],
        [0.11, 0.35, 11.14, 0.00]
    ]
    
    coords2 = [
        [0.53, 0.59, 13.09, 0.00],
        [0.73, 0.74, 13.09, 0.00],
        [0.46, 0.90, 13.09, 0.00],
        [0.75, 0.88, 13.09, 0.00],
        [0.17, 0.38, 13.09, 0.00]
    ]

    # Hesaplamaları yap
    delta_x, delta_y, zoom_factor, delta_rotation = calculate_transform(coords1, coords2)

    # Sonuçları yazdır
    print(f"X kaydırma: {delta_x}")
    print(f"Y kaydırma: {delta_y}")
    print(f"Zoom faktörü: {zoom_factor}")
    print(f"Döndürme açısı: {delta_rotation}")

    # HTML kodu için formatlı çıktı
    print(f"\nHTML kodu için:")
    print(f"viewer1.viewport.panBy(new OpenSeadragon.Point({delta_x}, {delta_y}));")
    print(f"viewer1.viewport.setRotation({delta_rotation});")

if __name__ == "__main__":
    main()

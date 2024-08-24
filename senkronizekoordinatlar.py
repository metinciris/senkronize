import tkinter as tk
from tkinter import simpledialog
import numpy as np

def calculate_transform(coords1, coords2):
    points1 = np.array(coords1)
    points2 = np.array(coords2)

    center1 = np.mean(points1, axis=0)
    center2 = np.mean(points2, axis=0)

    delta_x = center2[0] - center1[0]
    delta_y = center2[1] - center1[1]

    zoom1 = np.mean([c[2] for c in coords1])
    zoom2 = np.mean([c[2] for c in coords2])
    zoom_factor = zoom2 / zoom1

    rotation1 = np.mean([c[3] for c in coords1])
    rotation2 = np.mean([c[3] for c in coords2])
    delta_rotation = rotation2 - rotation1

    return delta_x, delta_y, zoom_factor, delta_rotation

def parse_input(input_str):
    data = input_str.split(';')
    return [float(data[1]), float(data[2]), float(data[3]), float(data[4].replace('°', ''))]

def on_calculate():
    coords1 = []
    coords2 = []

    for entry1, entry2 in zip(entries_image1, entries_image2):
        if entry1.get() and entry2.get():
            coords1.append(parse_input(entry1.get()))
            coords2.append(parse_input(entry2.get()))

    delta_x, delta_y, zoom_factor, delta_rotation = calculate_transform(coords1, coords2)

    result_text.set(f"X kaydırma: {delta_x:.4f}\n"
                    f"Y kaydırma: {delta_y:.4f}\n"
                    f"Zoom faktörü: {zoom_factor:.4f}\n"
                    f"Döndürme açısı: {delta_rotation:.4f}\n\n"
                    "HTML Kodu:\n"
                    f"viewer1.viewport.panBy(new OpenSeadragon.Point({delta_x:.4f}, {delta_y:.4f}));\n"
                    f"viewer1.viewport.setRotation({delta_rotation:.2f});")

    button_calculate.config(text="Kodu Kopyala", command=copy_to_clipboard)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(result_text.get())

root = tk.Tk()
root.title("Senkronizasyon Hesaplayıcı")

# Giriş talimatları
instructions = tk.Label(root, text=("index1.html ve index2.html dosyalarını ayrı pencerelerde açın.\n"
                                    "Zoom yaparak ortak noktaları bulun ve koordinatları girin.\n"
                                    "Örnek giriş: image1.png;0.75;0.89;13.37;0.00°\n"
                                    "Kodu Kopyala tuşuna bastıktan sonra HTML kodunu kopyalayabilirsiniz."),
                        justify=tk.LEFT, padx=10, pady=10)
instructions.grid(row=0, column=0, columnspan=3)

# Giriş alanları
entries_image1 = []
entries_image2 = []

for i in range(10):
    label = tk.Label(root, text=f"Nokta {i + 1}")
    label.grid(row=i + 1, column=0, pady=5)

    entry1 = tk.Entry(root, width=40)
    entry2 = tk.Entry(root, width=40)

    entry1.grid(row=i + 1, column=1, padx=10)
    entry2.grid(row=i + 1, column=2, padx=10)

    entries_image1.append(entry1)
    entries_image2.append(entry2)

# Düğmeler ve sonuç gösterme
button_calculate = tk.Button(root, text="Kaydet ve Göster", command=on_calculate)
button_calculate.grid(row=11, column=1, pady=10)

button_exit = tk.Button(root, text="Çık", command=lambda: root.destroy())
button_exit.grid(row=11, column=2, pady=10)

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify=tk.LEFT, font=("Courier", 10))
result_label.grid(row=12, column=0, columnspan=3, pady=10)

root.mainloop()

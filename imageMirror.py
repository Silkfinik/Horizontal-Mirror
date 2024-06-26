import os
from PIL import Image, ImageOps
from tkinter import Tk, Label, Button, filedialog


def select_input_folder():
    folder = filedialog.askdirectory()
    if folder:
        input_folder_label.config(text=folder)
        input_folder_label.input_folder = folder


def select_output_folder():
    folder = filedialog.askdirectory()
    if folder:
        output_folder_label.config(text=folder)
        output_folder_label.output_folder = folder


def mirror_images():
    input_folder = getattr(input_folder_label, 'input_folder', None)
    output_folder = getattr(output_folder_label, 'output_folder', None)

    if not input_folder or not output_folder:
        return

    for file in os.listdir(input_folder):
        if file.lower().endswith(('png', 'jpg', 'jpeg')):
            img = Image.open(os.path.join(input_folder, file))
            mirrored_img = ImageOps.mirror(img)
            output_path = os.path.join(output_folder, f'mirrored_{file}')
            mirrored_img.save(output_path)

    result_label.config(text=f'Изображения отзеркалены и сохранены в папке {output_folder}')


# Создаем графический интерфейс
root = Tk()
root.title("Image Mirror")

input_folder_label = Label(root, text="Выберите папку с изображениями")
input_folder_label.pack()

input_button = Button(root, text="Выбрать папку с изображениями", command=select_input_folder)
input_button.pack()

output_folder_label = Label(root, text="Выберите папку для сохранения")
output_folder_label.pack()

output_button = Button(root, text="Выбрать папку для сохранения", command=select_output_folder)
output_button.pack()

mirror_button = Button(root, text="Отзеркалить изображения", command=mirror_images)
mirror_button.pack()

result_label = Label(root, text="")
result_label.pack()

root.mainloop()

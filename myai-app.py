from tkinter import *
from base64 import b64decode
import webbrowser
import openai

def generate_image_and_save(prompt, image_count, size):
    images = []
    response = openai.Image.create(
        prompt=prompt,
        n=image_count,
        size=size,
        response_format='b64_json'
    )

    for image in response['data']:
        images.append(image.b64_json)

    prefix ='img'
    for index, image in enumerate(images):
        with open(f'{prefix}_{index}.jpg', 'wb')as file:
            file.write(b64decode(image))

def generate_images():
    prompt = prompt_var.get()
    image_count = int(image_count_var.get())
    size = size_var.get()
    openai.api_key = " MENTION OPENAI-KEY NUMBERS"
    generate_image_and_save(prompt, image_count, size)
    output_label.config(text=f'{image_count} images generated')

# Create the main window
root = Tk()
root.geometry('600x400')
root.title('Logo Generation App by Muhammad Shariq Siddiqui')

# Create input fields and labels
prompt_label = Label(root, text='Enter prompt:', font=('Arial', 14))
prompt_label.place(x=50, y=50)
prompt_var = StringVar()
prompt_entry = Entry(root, textvariable=prompt_var, font=('Arial', 14), width=40)
prompt_entry.place(x=200, y=50)

image_count_label = Label(root, text='Enter number of images to generate:', font=('Arial', 14))
image_count_label.place(x=50, y=100)
image_count_var = StringVar()
image_count_entry = Entry(root, textvariable=image_count_var, font=('Arial', 14), width=10)
image_count_entry.place(x=350, y=100)

size_label = Label(root, text='Select image size:', font=('Arial', 14))
size_label.place(x=50, y=150)
size_var = StringVar(value='512x512')
size_menu = OptionMenu(root, size_var, '256x256', '512x512', '1024x1024')
size_menu.config(font=('Arial', 14), width=10)
size_menu.place(x=250, y=150)

# Create generate button
generate_button = Button(root, text='Generate Images', command=generate_images, font=('Arial', 14), bg='blue', fg='white')
generate_button.place(x=50, y=250)

# Create output label
output_label = Label(root, text='', font=('Arial', 14))
output_label.place(x=50, y=320)

root.mainloop()

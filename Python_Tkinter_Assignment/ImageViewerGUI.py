from my_package.model import ImageCaptioningModel
from my_package.model import ImageClassificationModel
from tkinter import *
from functools import partial
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import ttk


def fileClick(event=None, x=None, y=None):
    # Define the function you want to call when the filebrowser button (Open) is clicked.
    # This function should pop-up a dialog for the user to select an input image file.
    # To have a better clarity, please check out the sample video.
    img_path.set(filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")]))

    # Get the corresponding outputs from the captioner or classifier based on the dropdown choice
    choice = dropdown.get()
    if choice == "Image Captioning":
        caption = captioner.__call__(img_path.get())
        output_label.config(text=caption)
    elif choice == "Image Classification":
        class_name = classifier(img_path.get())
        output_label.config(text=class_name)

    # Display the original image file
    img = Image.open(img_path.get())
    img = img.resize((300, 300), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    img_label.config(image=img)
    img_label.image = img

                                               
def process(clicked, captioner, classifier):
    # This function will produce the required output when 'Process' button is clicked.
    # Note: This should handle the case if the user clicks on the `Process` button without selecting any image file.
    while img_path.get() == "":
        output_label.config(text="Please select an image file.")
        return
    choice = dropdown.get()
    if choice == "Image Captioning":
        caption = captioner.__call__(img_path.get())
        output_label.config(text=caption)
    elif choice == "Image Classification":
        class_name = classifier(img_path.get())
        output_label.config(text=class_name)


if __name__ == '__main__':
    # Complete the main function preferably in this order:
    # Instantiate the root window.
    root = Tk()
    # Provide a title to the root window.
    root.title("Image Viewer GUI")
    # Instantiate the captioner, classifier models.
    captioner = ImageCaptioningModel()
    classifier = ImageClassificationModel()
    # Declare the file browsing button.
    img_path = StringVar()
    file_btn = Button(root, text="Open", command=partial(fileClick, captioner, classifier, img_path))
    file_btn.pack(pady=10)
    # Declare the drop-down button.
    dropdown = ttk.Combobox(root, values=["Image Captioning", "Image Classification"])
    dropdown.current(0)
    dropdown.pack(pady=10)
    # Declare the process button.
    process_btn = Button(root, text="Process", command=partial(process, captioner, classifier, img_path))
    process_btn.pack(pady=10)
    # Declare the image label.
    img_label = Label(root)
    img_label.pack(pady=10)
    # Declare the output label.
    output_label = Label(root, font=("Arial", 14), wraplength=400)
    output_label.pack(pady=10)
    # Run the main loop.
    root.mainloop()

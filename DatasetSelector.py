import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os
import shutil

class ImageSorterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dataset Builder")

        self.image_paths = []
        self.current_index = 0
        self.actions = {}

        self.output_base_folder = None

        # UI Elements
        self.label = tk.Label(self.root, text="No image loaded", font=("Arial", 16))
        self.label.pack(pady=10)

        self.canvas = tk.Canvas(self.root, width=800, height=600, bg='gray')
        self.canvas.pack()

        # Bind keys
        self.root.bind("<space>", self.move_to_no_dataset)
        self.root.bind("<Return>", self.move_to_dataset)
        self.root.bind("<Left>", self.go_back)
        self.root.bind("<Right>", self.go_forward)

        self.load_button = tk.Button(self.root, text="Select Image Folder", command=self.load_image_folder)
        self.load_button.pack(pady=5)

        self.output_button = tk.Button(self.root, text="Select Output Folder", command=self.select_output_folder)
        self.output_button.pack(pady=5)

        # Hold the image reference
        self.image_ref = None

    def select_output_folder(self):
        selected_folder = filedialog.askdirectory(title="Select Output Base Folder")
        if selected_folder:
            self.output_base_folder = selected_folder
            print(f"Output base folder set to: {self.output_base_folder}")

    def load_image_folder(self):
        folder_selected = filedialog.askdirectory(title="Select Image Folder")
        print(f"Selected folder: {folder_selected}")

        if not folder_selected:
            return

        supported_exts = (".jpg", ".jpeg", ".png", ".bmp", ".gif")
        self.image_paths = [
            os.path.join(folder_selected, f)
            for f in os.listdir(folder_selected)
            if f.lower().endswith(supported_exts)
        ]
        self.image_paths.sort()
        print(f"Found {len(self.image_paths)} images.")

        if not self.image_paths:
            messagebox.showwarning("Warning", "No supported images found in this folder.")
            return

        if not self.output_base_folder:
            messagebox.showwarning("Warning", "Please select an output folder first.")
            return

        os.makedirs(os.path.join(self.output_base_folder, "Dataset"), exist_ok=True)
        os.makedirs(os.path.join(self.output_base_folder, "No_dataset"), exist_ok=True)

        self.current_index = 0
        self.actions = {}

        self.load_image()

    def load_image(self):
        if self.current_index < 0:
            self.current_index = 0
        if self.current_index >= len(self.image_paths):
            messagebox.showinfo("Info", "All images have been sorted!")
            self.canvas.delete("all")
            self.label.config(text="No image loaded")
            return

        image_path = self.image_paths[self.current_index]
        print(f"Loading image: {image_path}")

        try:
            image = Image.open(image_path).convert("RGB")
            w, h = image.size
            ratio = min(800 / w, 600 / h)
            new_size = (int(w * ratio), int(h * ratio))
            image = image.resize(new_size, Image.LANCZOS)

            self.tk_image = ImageTk.PhotoImage(image)
            self.image_ref = self.tk_image

            self.canvas.delete("all")
            x = (800 - new_size[0]) // 2
            y = (600 - new_size[1]) // 2
            self.canvas.create_image(x, y, anchor='nw', image=self.tk_image)
            self.label.config(text=f"Image: {os.path.basename(image_path)}")

            print("Image displayed!")
        except Exception as e:
            print(f"Error loading image: {e}")
            self.current_index += 1
            self.load_image()

    def move_to_dataset(self, event):
        if self.current_index < len(self.image_paths):
            self.copy_image("Dataset")

    def move_to_no_dataset(self, event):
        if self.current_index < len(self.image_paths):
            self.copy_image("No_dataset")

    def copy_image(self, folder_name):
        if not self.output_base_folder:
            messagebox.showwarning("Warning", "Please select an output folder first.")
            return

        image_path = self.image_paths[self.current_index]
        image_name = os.path.basename(image_path)
        dest_folder = os.path.join(self.output_base_folder, folder_name)
        dest_path = os.path.join(dest_folder, image_name)

        previous_folder_name = self.actions.get(image_path)
        if previous_folder_name and previous_folder_name != folder_name:
            prev_folder = os.path.join(self.output_base_folder, previous_folder_name)
            prev_path = os.path.join(prev_folder, image_name)
            if os.path.exists(prev_path):
                os.remove(prev_path)
                print(f"Removed {prev_path}")

        shutil.copy(image_path, dest_path)
        print(f"Copied {image_path} to {dest_path}")

        self.actions[image_path] = folder_name

        self.current_index += 1
        self.load_image()

    def go_back(self, event):
        if self.current_index > 0:
            self.current_index -= 1
            self.load_image()

    def go_forward(self, event):
        if self.current_index < len(self.image_paths) - 1:
            self.current_index += 1
            self.load_image()

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageSorterApp(root)
    root.mainloop()

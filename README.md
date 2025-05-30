# Dataset Builder (Image Sorter Tool)

A simple Python GUI application that helps you quickly sort images into two categories: `Dataset` and `No_dataset`. Perfect for building or curating image datasets!

---

## 🚀 Features

✅ **Load multiple images** at once  
✅ **View images** on a large canvas  
✅ **Sort images** with keyboard shortcuts  
✅ **Navigate backward and forward** to reassign images  
✅ **Reassign images** between folders (`Dataset` and `No_dataset`)  
✅ **No duplication** – ensures images are only in one folder at a time  

---

## 🖼️ How It Works

1. **Load Images**  
   - Click the **Select Images** button and choose the images you want to sort.

2. **Sort Images**  
   - **Assign to `Dataset`**: Press `Enter`  
   - **Assign to `No_dataset`**: Press `Space`  
   - Images are **copied** (not moved) from their original location.

3. **Navigate**  
   - **Go back** to the previous image: Press `Left Arrow`  
   - **Go forward** to the next image: Press `Right Arrow`

4. **Reassign Images**  
   - If you made a mistake, just go back and reassign the image – the app **removes it** from the previous folder and places it in the new one.

---

## 🔑 Keyboard Shortcuts

| Key           | Action                            |
|---------------|-----------------------------------|
| `Enter`       | Assign image to `Dataset`         |
| `Space`       | Assign image to `No_dataset`      |
| `Left Arrow`  | Go back to previous image         |
| `Right Arrow` | Go forward to next image          |

---

## 🛠️ Requirements

- Python 3.x
- `Pillow` library (`pip install pillow`)

---

## 📝 Usage

1. **Run the script:**

   ```bash
   python DatasetSelector.py

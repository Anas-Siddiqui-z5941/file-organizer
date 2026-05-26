# 📁 File Organizer

A Python CLI tool that automatically organizes cluttered folders by sorting files into categorized subfolders — images, documents, videos, audio, archives, scripts, and more.

---

## ✨ Features

- **Auto-categorizes files** by extension into named subfolders
- **7 categories supported** — Images, Documents, Audio, Videos, Archives, Scripts, Others
- **Handles unknown files** — anything unrecognized goes into an `Others` folder
- **Non-destructive** — only moves files, never deletes
- **Modular design** — rules are separate from logic, easy to extend

---

## 🗂️ Categories

| Folder | Extensions |
|---|---|
| Images | `.jpg` `.jpeg` `.png` `.gif` `.bmp` |
| Documents | `.pdf` `.docx` `.txt` `.xlsx` `.pptx` |
| Audio | `.mp3` `.wav` `.aac` `.flac` |
| Videos | `.mp4` `.avi` `.mkv` `.mov` |
| Archives | `.zip` `.rar` `.tar` `.gz` |
| Scripts | `.py` `.js` `.sh` `.bat` |
| Others | anything else |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x (no external libraries required)

### Run the organizer

```bash
git clone https://github.com/Anas-Siddiqui-z5941/file-organizer.git
cd file-organizer
python main.py
```

By default it organizes the `test_folder` directory. To organize a different folder, edit `main.py`:

```python
organize_files("your/folder/path")
```

---

## 📁 Project Structure

```
file-organizer/
│
├── main.py          # Entry point — call organize_files() here
├── organizer.py     # Core logic — iterates files and moves them
├── rules.py         # Category rules — extensions mapped to folder names
├── test_folder/     # Sample folder to test the organizer
└── README.md
```

---

## ⚙️ How It Works

1. `main.py` calls `organize_files()` with a target folder path
2. `organizer.py` iterates every file in that folder
3. Each file's extension is matched against the rules in `rules.py`
4. The file is moved into the matching category subfolder
5. Unmatched files go into `Others/`

---

## ➕ Adding New Categories

Just edit `rules.py`:

```python
file_category = {
    'images': ['.jpg', '.jpeg', '.png'],
    'ebooks': ['.epub', '.mobi'],   # ← add new category like this
    ...
}
```

No changes needed in `organizer.py` — it reads categories dynamically.

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)

**Libraries used:** `pathlib` · `shutil` — all Python built-ins, no pip install needed.

---

## 👤 Author

**Anas Mohiuddin Siddiqui**  
B.Tech CSE @ Integral University | Aspiring ML Engineer  
[LinkedIn](https://www.linkedin.com/in/anas-siddiqui-z5941) • [GitHub](https://github.com/Anas-Siddiqui-z5941)

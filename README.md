# Hands-Free Mouse Control Using Eye Movement

## 6.1 — What this project does

This project lets you control your mouse using only your eyes. It tracks your eye movement to move the cursor and detects blinks to perform clicks.

---

## 6.2 — Exact Python Version

Please install **Python 3.10** from [https://www.python.org](https://www.python.org).

---

## 6.3 — How to install dependencies

### Windows

1. Open **Command Prompt** (press Windows key, type "cmd", hit Enter)
2. Check Python version:

---

## 6.4 — Permissions Instructions

### Windows

- Enable **Camera access**: Settings → Privacy → Camera → Allow apps to access camera
- Run Command Prompt as **Administrator** to allow mouse control

### macOS

- Go to **System Preferences → Privacy & Security**
- Enable **Camera** access for Terminal
- Add **Terminal** to:
- Accessibility
- Input Monitoring

### Linux

- Ensure camera access is enabled
- You may need to add **udev rules** for webcam access (search your distro’s guide)

---

## 6.5 — Troubleshooting

- Webcam not detected:


---

## 6.6 — How Blink Detection Works

The program checks the distance between your eyelid landmarks. If your eye closes (distance shrinks), it counts as a blink and triggers a click.

---

## 6.7 — How Eye-to-Cursor Mapping Works

The program tracks your iris position and maps it to your screen size. It moves the mouse to match your gaze direction.

---

## 6.8 — How to Stop the Script

- Press **q** in the OpenCV preview window
- Or press **Ctrl + C** in the terminal

---

## 6.9 — Time Estimate

| Task                          | Time (minutes) |
|-------------------------------|----------------|
| Install Python                | 5              |
| Install packages              | 5              |
| Run the script                | 2              |
| Grant permissions             | 5              |
| Test eye movement             | 5              |
| Test blink click              | 5              |
| Upload to GitHub              | 10             |
| **Total**                     | **37 minutes** |

---

# STEP 7 — How to Upload This Project to GitHub (Beginner Friendly)

## 7.1 — Create a GitHub Account

Go to [https://github.com](https://github.com) and click **Sign Up**. Enter your email, username, and password.

---

## 7.2 — Create a New Repository

1. Click your profile picture
2. Click **Your repositories**
3. Click **New**
4. Name it: `eye_mouse_control`
5. Choose **Public**
6. Do **NOT** add a README
7. Click **Create repository**

---

## 7.3 — Upload Files Using GitHub Website

1. Click **Add file** → **Upload files**
2. Drag and drop:
 - `main.py`
 - `requirements.txt`
 - `README.md`
3. Click **Commit changes**

---

## 7.4 — Avoid GitHub Size Errors

✅ Do NOT upload:
- Virtual environment folders
- `.pyc` files
- Large images
- Files over 20 MB

This project is small and safe to upload.

---

## 7.5 — Optional: Upload Using Git

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/USERNAME/eye_mouse_control.git
git push -u origin main
```

## How do you access the project??
- Click the green “Code” button →
Choose “Download ZIP”
- Unzip the folder on their computer
- Open Terminal or Command Prompt in that folder
- Install dependencies:
 ```
  pip install -r requirements.txt
```
- Run the project:
```
python main.py
```
And It should run in your device!!


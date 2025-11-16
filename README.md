##🔍 Hands-Free Mouse Control Using Eye Movement
Modular Add-On System (Safe — No Code Breaking)

This project allows you to control your computer mouse using eye movement and blink gestures.
It also supports a modular add-on system, letting you add new features without touching or modifying main.py, ensuring the core project always stays stable and error-free.

##✅ Features

Eye tracking using Mediapipe Face Mesh

Mouse movement controlled by gaze position

Blink-to-click functionality

Modular add-on system for safe feature expansion

No large files, no heavy models, no GitHub upload issues

##📁 Project Structure
eye_mouse_control/
│
├── main.py                 ← Core file (DO NOT MODIFY)
├── requirements.txt
├── README.md
│
└── modules/
    ├── __init__.py
    ├── addon_manager.py
    ├── voice_commands.py          (example add-on)
    ├── gesture_shortcuts.py       (example add-on)

##🧠 How the Modular Add-On System Works

All new features are added inside the modules/ folder

Each add-on lives in its own file

Add-ons run independently from the main program

You never modify main.py

If an add-on fails, the main project still works

This ensures zero errors, zero breaks, and full project stability.

##🚀 How to Enable Add-Ons

Open:

modules/addon_manager.py


Find this dictionary:

addons = {
    "voice_commands": False,
    "gesture_shortcuts": False,
}


Turn any add-on ON by setting it to True:

addons = {
    "voice_commands": True,
    "gesture_shortcuts": False,
}


Save the file — you're done.
No changes to main.py needed.

##➕ How to Add a New Add-On (Safely)
Step 1 — Create new file

Inside modules/, create:

my_addon.py

Step 2 — Add required function

Paste:

def run(frame, landmarks):
    # Your add-on code here
    return None

Step 3 — Register it

In modules/addon_manager.py, add:

addons["my_addon"] = True

Step 4 — Import it

Inside addon_manager.py, add:

from . import my_addon

Step 5 — Trigger it

Inside the add-on execution block:

if addons["my_addon"]:
    my_addon.run(frame, landmarks)


✔ Add-on added
✔ No conflicts
✔ Main program unchanged

##🛑 Do NOT Modify main.py

main.py contains core logic:

Eye tracking

Blink detection

Mouse movement

Changing it can break the entire project.
All extra features must stay inside the modules/ folder only.

##💡 Example Add-Ons You Can Create

Voice commands

Wink-based shortcuts

Sound feedback

Calibration tools

Sensitivity controls

Region-limited cursor movement

Activity logging

Gaze gestures

All are added as separate modules.

##⚙️ Installation
1. Install Python 3.10

Download from: python.org

2. Install dependencies
Windows (Command Prompt)
python -m pip install --upgrade pip
pip install -r requirements.txt

macOS / Linux (Terminal)
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

##▶️ Running the Project
Windows:
python main.py

macOS / Linux:
python3 main.py


Press q to quit the preview window.
Press Ctrl + C to stop in terminal.

##🔐 Permissions
Windows

Enable:

Camera Access

Run terminal as Administrator if mouse control fails

macOS

Go to:
System Settings → Privacy & Security →

Camera → Allow Terminal

Accessibility → Allow Terminal

Input Monitoring → Allow Terminal

##🐞 Troubleshooting
Webcam not detected

Close apps using the camera (Zoom, Teams, etc.)

Try another USB port

Restart your PC

“ImportError”

Run:

pip install -r requirements.txt

Add-on crashes

Check for typing mistakes

Make sure the add-on has a run() function

Make sure it’s registered in addon_manager.py

GitHub upload errors

Do not upload venv/

Do not upload large files

This project is safe to upload

🛡 Guaranteed Safe Workflow

Main code stays untouched

Add-ons cannot break core project

All modules are optional

Add unlimited features safely

##🎉 You're Ready!

Your modular system is now fully set up.
You can add, remove, or expand features freely — main.py will remain stable forever.

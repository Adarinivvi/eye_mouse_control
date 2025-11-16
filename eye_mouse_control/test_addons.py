import traceback
from modules.addon_manager import run_addons

# Simulated test values
frame = None
landmarks = None
x, y = 500, 300
eye_position = (x, y)
blink_count = 1  # Simulate a blink

print("Running test_addons.py with simulated blink...")

# Run the add-ons
run_addons(frame=frame, landmarks=landmarks, eye_position=eye_position, blink_count=blink_count)

print("Add-ons executed. Check for sound or blink_log.txt.")
try:
    run_addons(frame=frame, landmarks=landmarks, eye_position=eye_position, blink_count=blink_count)
except Exception:
    traceback.print_exc()
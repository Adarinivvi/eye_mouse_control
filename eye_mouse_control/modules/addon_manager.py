def load_addons():
    """
    Returns a dictionary of available add-ons and their enabled status.
    Users can toggle these manually in their own scripts.
    """
    return {
        "sound_feedback": True,
        "blink_logger": True,
        "voice_commands": False,
        "gesture_shortcuts": False,
        "calibration_tool": False,
    }

def run_addons(frame=None, landmarks=None, eye_position=None, blink_count=0):
    """
    Safely runs enabled add-ons. All parameters are optional.
    """
    addons = load_addons()

    if addons.get("sound_feedback"):
        try:
            from .sound_feedback import run_sound_feedback
            run_sound_feedback(blink_count)
        except Exception:
            pass

    if addons.get("blink_logger"):
        try:
            from .blink_logger import run_blink_logger
            run_blink_logger(blink_count)
        except Exception:
            pass

    # Future add-ons can be added here safely
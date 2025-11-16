def run_sound_feedback(blink_count):
    """
    Plays a beep sound when a blink is detected.
    """
    try:
        import os
        import platform

        if blink_count > 0:
            if platform.system() == "Windows":
                import winsound
                winsound.Beep(1000, 150)
            else:
                os.system('printf "\\a"')  # macOS/Linux beep
    except Exception:
        pass  # Always fail silently
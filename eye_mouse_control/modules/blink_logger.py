def run_blink_logger(blink_count):
    """
    Logs blink events to a text file.
    """
    try:
        if blink_count > 0:
            with open("blink_log.txt", "a") as f:
                from datetime import datetime
                f.write(f"{datetime.now()} — Blink detected ({blink_count})\n")
    except Exception:
        pass  # Always fail silently
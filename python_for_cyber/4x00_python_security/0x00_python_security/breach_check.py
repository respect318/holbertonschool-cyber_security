#!/usr/bin/env python3
import logging

# -----------------------------
# Task 6: The Logger
# -----------------------------
def setup_logger(name: str, logfile: str = None, level=logging.INFO):
    """
    Create a logger with optional file output.
    Logs to console by default.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Prevent adding multiple handlers if function called multiple times
    if not logger.hasHandlers():
        # Console handler
        ch = logging.StreamHandler()
        ch.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
        logger.addHandler(ch)

        # Optional file handler
        if logfile:
            fh = logging.FileHandler(logfile)
            fh.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
            logger.addHandler(fh)
    
    return logger

# -----------------------------
# Example usage for testing
# -----------------------------
if __name__ == "__main__":
    log = setup_logger("BreachLogger", "breach.log")
    log.info("This is an info message.")
    log.warning("This is a warning message.")
    log.error("This is an error message.")

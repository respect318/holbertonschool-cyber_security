BLACKLIST = {'10.0.0.1', '192.168.1.66'}


def check_threat_intel(log_entry):
    """
    Checks if log_entry.ip is in the BLACKLIST.
    If yes, sets log_entry.alert_level = 'HIGH'.
    Otherwise, sets log_entry.alert_level = 'LOW'.
    Returns the updated log_entry.
    """
    if hasattr(log_entry, 'ip') and log_entry.ip in BLACKLIST:
        log_entry.alert_level = 'HIGH'
    else:
        log_entry.alert_level = 'LOW'
    return log_entry

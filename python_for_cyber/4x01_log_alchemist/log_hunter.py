def analyze_user_agent(log_entry):
    """
    Checks if a LogEntry message contains automated tool User-Agent strings.
    If it contains sqlmap, nikto, curl, or python, sets log_entry.is_bot = True.
    Otherwise, sets log_entry.is_bot = False.
    Returns the updated log_entry.
    """
    if not hasattr(log_entry, 'message') or log_entry.message is None:
        log_entry.is_bot = False
        return log_entry

    bot_keywords = ['sqlmap', 'nikto', 'curl', 'python']

    message_lower = log_entry.message.lower()
    log_entry.is_bot = any(keyword in message_lower for keyword in bot_keywords)

    return log_entry


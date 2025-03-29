def base_detection(data):
    """
    Dummy function to detect possible encodings.
    Returns 'Base64' if the string ends with '=', and checks for hexadecimal.
    """
    detected = []
    if data:
        if data.endswith('='):
            detected.append("Base64")
        try:
            int(data, 16)
            detected.append("Hexadecimal")
        except ValueError:
            pass
    return detected if detected else ["Unknown"]

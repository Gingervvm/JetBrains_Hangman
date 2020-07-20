def what_to_do(instructions):
    condition_string = "Simon says"
    if instructions.startswith(condition_string) or instructions.endswith(condition_string):
        return "I " + instructions.replace(condition_string, "").strip()
    return "I won't do it!"
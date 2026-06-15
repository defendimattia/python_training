def make_readable(seconds):

    mins = seconds / 60
    hours = mins / 60

    return f"{int(hours):02d}:{int(mins % 60):02d}:{(seconds % 60):02d}"

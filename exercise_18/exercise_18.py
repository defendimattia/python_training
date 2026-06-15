def string_reduc(arr):
    string = " ".join(arr)
    string2 = (
        string.replace("NORTH SOUTH", "")
        .replace("SOUTH NORTH", "")
        .replace("EAST WEST", "")
        .replace("WEST EAST", "")
    )
    string3 = string2.split()
    return string_reduc(string3) if len(string3) < len(arr) else string3

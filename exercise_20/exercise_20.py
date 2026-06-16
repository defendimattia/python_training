def generate_hashtag(s):

    string = "".join(s.title().split())

    return False if (len(string) > 139 or len(string) == 0) else "#" + string

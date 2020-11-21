# user = input()

def check_email(string):
    if " " not in string and "@" in string and "@." not in string and "." in string and ".@" not in string:
        return True
    else:
        return False


# check_email(user)

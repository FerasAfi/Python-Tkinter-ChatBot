import string


def check(password):
    warning=[]
    alnum=0 if password.isalnum() else 1
    length=0 if (len(password) < 8) else 1
    symbol=0 if any(symbol in password for symbol in string.punctuation) else 1
    lower=0 if password.islower() else 1
    upper=0 if password.isupper() else 1

    if not length:
        warning.append("Password must be at least 8 characters long.")
    if not alnum:
        warning.append("Password must contain at least one digit")
    if symbol:
        warning.append("Password must contain at least one special character")
    if not lower:
        warning.append("Password must contain at least one uppercase letter")
    if not upper:
        warning.append("Password must contain at least one lowercase letter")


    return ('\n'.join(warning))

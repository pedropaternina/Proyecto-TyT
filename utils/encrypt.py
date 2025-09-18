import bcrypt


def hash_password(password: str) -> str:
    pwd_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password=pwd_bytes,  salt=salt)
    return hashed.decode("utf-8")


def check_password(password, hashed) -> bool:
    password_plain = password.encode("utf-8")
    hashed_password = hashed.encode("utf-8")
    return bcrypt.checkpw(password_plain, hashed_password)


import hashlib
import random
import string

def hash_password(password):
    salt = "".join(random.choices(string.hexdigits, k=32))
    salted_password = (password+salt).encode("utf-8")
    hash_object = hashlib.sha256(salted_password)
    hashed_password = hash_object.hexdigest()
    return hashed_password, salt


def check_password(password, saved_hashed_password, salt):
    salted_password = (password + salt).encode("utf-8")
    hash_object = hashlib.sha256(salted_password)
    hashed_password = hash_object.hexdigest()
    return hashed_password == saved_hashed_password


def test_hash_and_check_password():
    hashed_password, salt = hash_password("hohoho")
    assert type(hashed_password) is str
    assert type(salt) is str
    assert check_password("hoho",hashed_password,salt) == False
    assert check_password("hohoho",hashed_password,salt) == True


if __name__ == "__main__":
    test_hash_and_check_password()
    print("done.")

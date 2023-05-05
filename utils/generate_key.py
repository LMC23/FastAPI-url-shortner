import random
import string


def generate_keys(length_secret_key=8, length_key=5):

    secret_key = "".join(random.choices(string.ascii_letters + string.digits, k=length_secret_key))
    key = "".join(random.choices(string.ascii_letters + string.digits, k=length_key))

    return secret_key, key

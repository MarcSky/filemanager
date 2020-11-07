import uuid
import time
from hashlib import md5


def generate_unique_filename(filename):
    return "%s" % md5(str(filename+str(int(time.time()))).encode()).hexdigest()


def generate_unique_link():
    return str(uuid.uuid4())

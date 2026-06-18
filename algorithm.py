import hashlib

def get_short(url : str):
    text = url.encode("utf-8")
    obj = hashlib.sha256(text)
    shorted = obj.hexdigest()
    return shorted[:6]
import hashlib

with open('addons.xml', 'rb') as f:
    content = f.read()

hash_md5 = hashlib.md5(content).hexdigest()

with open('addons.xml.md5', 'w') as f:
    f.write(hash_md5)

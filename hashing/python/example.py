import hashlib, uuid
password = "password1"
salt = uuid.uuid4().hex
hashed_password = hashlib.sha512(password + salt).hexdigest()
print(password, salt, hashed_password)

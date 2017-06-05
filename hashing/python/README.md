# Password Hashing Notes
Example of how to store passwords by hashing with a salt

## Summary
- Storing passwords as plaintext is for dweebs
- Storing passwords as simple hash is susceptible to rainbow attacks
- Store passwords by hashing with a salt, see [password_hashing_example.py](example.py) for basic example on how to do this
- Will need to store hashed password and salt in database

## Sources
- https://stackoverflow.com/questions/9594125/salt-and-hash-a-password-in-python

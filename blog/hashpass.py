from passlib.context import CryptContext

passwd = CryptContext(schemes=['bcrypt'], deprecated='auto')


class Hash:
    def bcrypt(password: str):
        return passwd.hash(password)

    def verify(hashed, plain_password):
        return passwd.verify(plain_password, hashed)

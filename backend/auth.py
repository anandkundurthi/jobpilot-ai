from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

users_db = {}

def hash_password(password):
    return pwd_context.hash(password)

def verify_password(password, hashed):
    return pwd_context.verify(password, hashed)

def create_user(username, password):
    users_db[username] = hash_password(password)

def authenticate_user(username, password):

    if username not in users_db:
        return False

    return verify_password(password, users_db[username])

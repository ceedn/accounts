import logging
from passlib.context import CryptContext
import re
import datetime
    
# Define the hashing context   
PasswordHashingContext = CryptContext(
    # The first hash in the list will be the default one used to hash passwords.
    # The rest will be supported for verification but will be marked as deprecated.
    schemes = ["argon2", "pbkdf2_sha256"],
    pbkdf2_sha256__min_rounds=150,
    argon2__min_rounds=150,
    deprecated="auto"
) 

# Hash a password using the hashing context
# This will return a hash of the password.
def hash_password(password):
    '''Hash a password'''
    try:
        return PasswordHashingContext.hash(password)
    except Exception as err:
        logging.error("Errored trying to hash password. This should never happen. Returning None.")
        return None

# Verify a password against a hash
# This will return true if the password matches the hash, and false if it doesn't.
def verify_password(password, hash):
    '''Verify a password against a hash'''
    try:
        return PasswordHashingContext.verify(password, hash)
    except Exception as err:
        logging.error("Errored trying verify password. This should never happen. Continuing as if incorrect password.")
        return False
    
# Verify a email address is valid
# This will return true if the email address is valid, and false if it isn't.
# This is used to verify that the email address is valid before creating a user.
# This is not a perfect email address validator, but it's good enough for our purposes.
def verify_email(email):
    '''Verify that an email address is valid'''
    try:
        if re.search("^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$", email):
            return True
        else:
            return False
    except Exception as err:
        logging.error("Errored trying verify email address. This should never happen. Continuing as if invalid email address.")
        return False
    
# Get the time in SQL format
# This will return a string of the current time in SQL format.
def GetSQLTime():
    '''Get the current time in SQL format'''
    now = datetime.datetime.now()
    sqltime = now.strftime("%Y/%m/%d %H:%M:%S")
    return(sqltime)

# Get the time in nice format
def GetNiceTime(seconds):
    '''Convert seconds to a nice format'''
    min, sec = divmod(seconds, 60)
    hour, min = divmod(min, 60)
    day, hour = divmod(hour, 24)
    return "%04d:%02d:%02d:%02d" % (day, hour, min, sec)
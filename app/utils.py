from pydantic import BaseModel
class PasswordRequest(BaseModel):
    length: int
    include_upper: bool
    include_lower: bool
    include_numbers: bool
    include_symbols: bool
def generate_password(data:PasswordRequest) -> str:
    import random as rd
    import string as str
    pool=""
    password_list=[]
    password=""
    if data.include_upper==True:
        pool+=str.ascii_uppercase
    if data.include_lower==True:
        pool+=str.ascii_lowercase
    if data.include_symbols==True:
        pool+=str.punctuation
    if data.include_numbers==True:
        pool+=str.digits
    if not pool:
        return "Please select at least one character type ."
    password_list=rd.choices(pool,k=data.length)
    rd.shuffle(password_list)
    password="".join(password_list)
    return password

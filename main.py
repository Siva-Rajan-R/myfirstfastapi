from fastapi import FastAPI
from pydantic import BaseModel,EmailStr
app=FastAPI()
db={}

class create(BaseModel):
    email:EmailStr
    password:str

@app.post('/signup')
def signup(request:create):
    print(request.email)
    if request.email not in db:
        db[request.email]=request.password
        return {'detail':'sign_uped successfully'}
    return {'detail':'email already exists'}

@app.get('/login/{email}/{password}')
def login(email,password):
    if email in db:
        if db[email]==password:
            return {'detail':f'welcome {email}'}
    return {'detail':'Incorrect Password or mail'}

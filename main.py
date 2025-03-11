from fastapi import FastAPI.Request
from pydantic import BaseModel,EmailStr
import pyrebase
app=FastAPI()
dbt={}
firebaseConfig = {
  'apiKey': "AIzaSyDoC4tzXQ7wOuPE-euUl9ZMhuz_nO0GOnI",
  'authDomain': "validation-f6e2e.firebaseapp.com",
  'databaseURL': "https://validation-f6e2e-default-rtdb.asia-southeast1.firebasedatabase.app",
  'projectId': "validation-f6e2e",
  'storageBucket': "validation-f6e2e.appspot.com",
  'messagingSenderId': "990295990161",
  'appId': "1:990295990161:web:ecf924935b2b2fb456c430",
  'measurementId': "G-PKM7J0WZNJ"
}
firebase=pyrebase.initialize_app(firebaseConfig)
db=firebase.database()
class create(BaseModel):
    email:EmailStr
    password:str

@app.post('/signup')
def signup(request:create,request:Request):
    headers = dict(request.headers)  # Convert headers to a dictionary
    print("headers from : ",headers)  # Print headers to the console
    if db.child('login_users').child(request.email.replace('.','c')).get().each()==None:
        dbt[request.email]=request.password
        db.child('login_users').child(request.email.replace('.','c')).set({request.email.replace('.','c'):request.password})
        return {'detail':'ulla vanthutada'}
    return {'detail':'email already exists'}

@app.get('/login/{email}/{password}')
def login(email:Emailstr,password:str,request:Request):
    headers = dict(request.headers)  # Convert headers to a dictionary
    print("headers from : ",headers) 
    a=db.child('login_users').child(email.replace('.','c')).get()
    if a.each()!=None:
        for i in a.each():
            if email.replace('.','c') == i.key():
                if i.val()==password:
                    return {'detail':f'welcome {email}'}
    return {'detail':'Incorrect Password or mail'}

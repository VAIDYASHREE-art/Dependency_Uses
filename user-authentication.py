from fastapi import FastAPI, Depends, Form, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI( )

#Setting a name for OAuth2 token URL
oauth2_schema= OAuth2PasswordBearer(tokenUrl='token')

#Endpoint to generate token, to seek access to protected routes
#The user sends request to acess the data/resource by providing the credentials.
@app.post('/token')
def login(username:str = Form(...), password: str= Form(...)):
    if username == 'johndoe' and password == 'pass123':
        return {'access_token': "valid_token", 'token_type': 'bearer'}
    raise HTTPException(status_code=400, detail='Invalid Credentials')

#Now in order to access the data, the generated token is extracted and decoded to verify the user - hppens via GET request.(with 2 functions))

def decode_token(token:str):
    if token == "valid_token":
        return {f'name':'johndoe'}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Invalid token',
    )

def get_current_user(token:str = Depends(oauth2_schema)):
    return decode_token(token)


@app.get('/profile')
def get_profile(user=Depends(get_current_user)):
    return {'username': user['name']}

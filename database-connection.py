from fastapi import FastaAPI, Depends

app = FastaAPI()

#Create a basic dependency to a database when an endpoint is called.

#dependency injection function
def get_db():
    db = {'Connection': 'mock database connection'}
    try:
        yield db
    finally:
        db.close()

#endpoint
@app.get('/hello')
def hello(db=Depends(get_db)):
    return{'db_status':'db_connection'}

#The dependency injection function get_db simulates establishing a database connection and ensures proper cleanup after the request is processed. The hello endpoint uses this dependency to access the database connection.

#Dependeny - depends ke zariye databse se connect, and injects the output into the db.


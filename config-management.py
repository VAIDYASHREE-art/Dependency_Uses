from fastapi import FastAPI, Depends

app = FastAPI()

class Settings:
    def __init__(self, api_key: str, debug: bool):
        self.api_key = 'my_secret_api_key'
        self.debug = True

# Dependency injection function to provide configuration settings
def get_settings():
    return Settings()

#Endpoint
@app.get('/config')
def get_config(settings:Settings=Depends(get_settings)): 
    return {'api_key': settings.api_key}

#Injects the config values(api_key, debug) into settings parameter of get_config endpoint using dependency injection.

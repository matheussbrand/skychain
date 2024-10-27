from google.oauth2 import id_token
from google.auth.transport import requests 

def authenticate_google_user(token):
    try: 
        # Load the token using the Google authentication client
        idinfo = id_token.verify_oauth2_token(token, requests.Request(),'YOU_CLIENT_ID')
        
        # Check the `aud` field to make sure it is the right token
        if idinfo['aud'] != 'YOU_CLIENT_ID':
            raise ValueError("Token is not for this client")
        
        # Returns authenticated user data
        return idinfo 
    
    except ValueError as e:
        print(f"Authentication error: {e}")
        return None
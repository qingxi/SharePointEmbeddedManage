import msal

# Constants
TENANT_ID = '<TENANT ID>'
CLIENT_ID = '<CLIENT ID'
CLIENT_SECRET = '<CLIENT SECRET>'
SCOPE = ['https://graph.microsoft.com/.default']  # Modify as needed
GRANT_TYPE = 'client_credentials'

authority = f'https://login.microsoftonline.com/{TENANT_ID}'
app = msal.ConfidentialClientApplication(CLIENT_ID, authority=authority, client_credential=CLIENT_SECRET)
token_respone = app.acquire_token_for_client(scopes=SCOPE)
if 'access_token' in token_respone:
    access_token = token_respone['access_token']
    #print(access_token)
else:
    print("Could not acquire token: ", token_response.get("error"), token_response.get("error_description"))
    throw(Exception("Could not acquire token"))

def getAuthorizationHeader():
    return {"Authorization":f"Bearer {access_token}"}

from google_auth_oauthlib.flow import Flow
import dotenv
from dotenv import load_dotenv

# Create the flow using the client secrets file from the Google API

# Console.

load_dotenv()

flow = Flow.from_client_secrets_file(
    '.env',
    scopes=['profile', 'email'],
    redirect_uri='urn:ietf:wg:oauth:2.0:oob')

# Tell the user to go to the authorization URL.
auth_url, _ = flow.authorization_url(prompt='consent')

print('Please go to this URL: {}'.format(auth_url))

# The user will get an authorization code. This code is used to get the
# access token.
code = input('Enter the authorization code: ')
flow.fetch_token(code=code)

# You can use flow.credentials, or you can just get a requests session
# using flow.authorized_session.
session = flow.authorized_session()
print(session.get('https://www.googleapis.com/userinfo/v2/me').json())

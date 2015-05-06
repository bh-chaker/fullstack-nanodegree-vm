import random, string, httplib2, json, requests

from oauth2client.client import flow_from_clientsecrets, FlowExchangeError

from database_utils import createUser, getUserID, getUser

def generate_random_string ( length ):
  """Generates and returns a random string."""
  return ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(length))

def init_csrf_token ( login_session ):
  """Generate a new CSRF token and save it login session"""
  login_session['csrf_token'] = generate_random_string(32)



def check_csrf_token ( login_session, request ):
  """Compare CSRF token from POST data and login session."""
  if 'csrf_token' not in login_session:
    return False

  if 'csrf_token' not in request.form:
    return False

  if login_session['csrf_token'] != request.form['csrf_token']:
    return False

  return True

def gconnect(login_session, request):
  """Processes the one-time-use code of Google OAuth2"""
  #Obtain authorization code
  code = request.form['code']
  try:
    # Upgrade the authorization code into a credentials object
    oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
    oauth_flow.redirect_uri = 'postmessage'
    credentials = oauth_flow.step2_exchange(code)
  except FlowExchangeError:
    return 'Failed to upgrade the authorization code.', 401

  # Check that the access token is valid.
  access_token = credentials.access_token
  url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
         % access_token)
  h = httplib2.Http()
  result = json.loads(h.request(url, 'GET')[1])
  # If there was an error in the access token info, abort.
  if result.get('error') is not None:
    return result.get('error'), 500


  # Verify that the access token is used for the intended user.
  gplus_id = credentials.id_token['sub']
  if result['user_id'] != gplus_id:
    return "Token's user ID doesn't match given user ID.", 401

  # Verify that the access token is valid for this app.
  GOOGLE_CLIENT_ID = json.loads(
  open('client_secrets.json', 'r').read())['web']['client_id']
  if result['issued_to'] != GOOGLE_CLIENT_ID:
    return "Token's client ID does not match app's.", 401

  stored_credentials = login_session.get('credentials')
  stored_gplus_id = login_session.get('gplus_id')
  if stored_credentials is not None and gplus_id == stored_gplus_id:
    return 'Current user is already connected.', 200

  # Store the access token in the session for later use.
  login_session['credentials'] = credentials
  login_session['gplus_id'] = gplus_id

  #Get user info
  userinfo_url =  "https://www.googleapis.com/oauth2/v1/userinfo"
  params = {'access_token': credentials.access_token, 'alt':'json'}
  answer = requests.get(userinfo_url, params=params)

  data = answer.json()

  login_session['username'] = data['name']
  login_session['picture'] = data['picture']
  login_session['email'] = data['email']
  #ADD PROVIDER TO LOGIN SESSION
  login_session['provider'] = 'google'

  #see if user exists, if it doesn't make a new one
  user_id = getUserID(data["email"])
  if not user_id:
    user_id = createUser(login_session)
  login_session['user_id'] = user_id

  return 'Successfully connected.', 200

def gdisconnect(login_session):
  """Revoke a current user's token and reset their login_session"""
  #Only disconnect a connected user.
  credentials = login_session.get('credentials')
  if credentials is None:
    return False

  access_token = credentials.access_token
  url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
  h = httplib2.Http()
  result = h.request(url, 'GET')[0]
  if result['status'] != '200':
    return False

  del login_session['gplus_id']
  del login_session['credentials']
  del login_session['username']
  del login_session['email']
  del login_session['picture']
  del login_session['user_id']
  del login_session['provider']

  return True
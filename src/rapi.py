from google.appengine.ext.remote_api import remote_api_stub
from google.appengine.tools import appengine_rpc_httplib2
from oauth2client.service_account import ServiceAccountCredentials


try:
    import dev_appserver
    dev_appserver.fix_sys_path()
except ImportError:
    print('Please make sure the App Engine SDK is in your PYTHONPATH.')
    raise


DEFAULT_REMOTE_API_ENDPOINT = '/_ah/remote_api'

def init(keyfile_path, app_id, remote_api_endpoint=DEFAULT_REMOTE_API_ENDPOINT):
    scopes = remote_api_stub._OAUTH_SCOPES
    
    creds = ServiceAccountCredentials.from_json_keyfile_name(keyfile_path, scopes=scopes)
    
    oauth2_parameters = appengine_rpc_httplib2.HttpRpcServerOAuth2.OAuth2Parameters(
            access_token=None,
            client_id=None,
            client_secret=None,
            scope=scopes,
            refresh_token=None,
            credential_file=None,
            credentials=creds)
    
    app_url = '{0}.appspot.com'.format(app_id)
    return remote_api_stub.ConfigureRemoteApiForOAuth(servername=app_url,
                                                      path=remote_api_endpoint,
                                                      oauth2_parameters=oauth2_parameters)

class RemoteApiBase(object):
    app_id = None
    keyfile_path = None
    remote_api_endpoint = '/_ah/remote_api'
    
    def __init__(self):
        if not self.app_id:
            raise ValueError('app_id Not Defined')
        if not self.keyfile_path:
            raise ValueError('keyfile_path Not Defined')
        
        init(self.keyfile_path, self.app_id, self.remote_api_endpoint)
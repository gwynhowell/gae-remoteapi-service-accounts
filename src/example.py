import models
import rapi


# the json file downloaded from a service account created in the google cloud console
CERT_FILEPATH = 'certs/your-filepath.json'

# the application id of your application 
APP_ID = 'your-appid'

def main():
    # init the connection to the remote api ...
    rapi.init(keyfile_path=CERT_FILEPATH, app_id=APP_ID)
    
    # a sample script to list 100 users from the datastore ...
    users = models.User.query().fetch(100)
    for user in users:
        user_dict = user.to_dict()
        print user_dict['email']
    
if __name__ == '__main__':
    main()

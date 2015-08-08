from linkedin import linkedin
from linkedin import server
import oauth2 as oauth

# https://developer-programs.linkedin.com/documents/getting-oauth-token-python

# Define CONSUMER_KEY, CONSUMER_SECRET,  
# USER_TOKEN, and USER_SECRET from the credentials 
# provided in your LinkedIn application

# Instantiate the developer authentication class

print linkedin.PERMISSIONS.enums.values()
authentication = linkedin.LinkedInDeveloperAuthentication(CONSUMER_KEY, CONSUMER_SECRET, 
                                                          USER_TOKEN, USER_SECRET, 
                                                          RETURN_URL, linkedin.PERMISSIONS.enums.values())

# Pass it in to the app...

application = linkedin.LinkedInApplication(authentication)

# Use the app....

#me = application.get_profile(member_url="https://tw.linkedin.com/pub/meng-ta-randy-hsieh/61/284/bbb", selectors=['first-name', 'last-name', 'location', 'skills', 'educations'])
me = application.get_profile(member_id="HaEDzbxmAl", selectors=['id', 'first-name', 'last-name', 'location', 'distance', 'num-connections', 'skills', 'educations'])
#me = application.get_profile()
print me
print type(me)

#semi_search = application.search_job(params={'title': 'semiconductor', 'count': 2})
#print semi_search
res = application.search_profile(selectors=[{'people': ['first-name', 'last-name']}], params={'keywords': 'apple microsoft'})
print res

#app = server.quick_api(USER_TOKEN, USER_SECRET)

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
token = oauth.Token(key=USER_TOKEN, secret=USER_SECRET)
client = oauth.Client(consumer, token)
resp, content = client.request("https://www.linkedin.com/pub/te-lin-wu/102/991/685")
#print resp
#print content

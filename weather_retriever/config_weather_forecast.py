"""
This python script contains sample username and sample apikey, which creates "config_sample.ini" file using "configparser".
The username and apikey can be obtained by signig-up on any of the weather forecast websites.

Weather website used: https://developer.accuweather.com/
Successful sign-up on the above website provides "apikey" which can be inputted in this file so as to access the api calls on the website, 
mentioned under the "API reference" (https://developer.accuweather.com/apis) tab. 

For instance, 
- if we click on "Location API" in order to get the city location, 
- all we need to do is under the "Text Search" space,
- click on "City Search" (https://developer.accuweather.com/accuweather-locations-api/apis/get/locations/v1/cities/search), fill in 
mandatory apikey(recieved while signing up) and q(text search, e.g.: Cupertino, CA)
- click on "Send this Request"
- grab the url from the "cURL" tab --> http://dataservice.accuweather.com/locations/v1/cities/search?apikey=<apikey>&q=California%2C%20CA
Here, in the link <apikey> should be replaced with the original apikey.
"""

from configparser import ConfigParser

config = ConfigParser()

config['auth'] = {
    'username': 'user',
    'apikey' : '0a1bxxxxxxx'
}

with open('./config_sample.ini', 'w') as f:
    config.write(f)

import twitter
import sys
import os
from os import environ
import json

class Twitter(object):
        def __init__ (self):
                configDir = environ.get('ETC','/etc')
                configFile = os.path.join(configDir, 'token.json')
                with open(configFile, 'r') as _f:
                        self.config = json.loads(_f.read())

        def tweet(self, message, media=None):
                api = twitter.Api(consumer_key=self.config['consumerKey'], consumer_secret=self.config['consumerSecret'],
                        access_token_key=self.config['accessToken'], access_token_secret=self.config['accessTokenSecret'],
                        input_encoding='utf-8')
                try:
                        status = api.PostUpdate(message, media)
                except UnicodeDecodeError:
                        print 'error with message'
                        print message
                        sys.exit(2)
                return

from lib.api_request import request
try:
    import json
except:
    import simplejson as json

# Github advice to use this header
request_header  = { 'Accept' : 'application/vnd.github.v3.text-match+json' }
# URL to Github API
url_api         = 'https://api.github.com'
# Path to make a search for Github
path_search     = '/search/repositories'

# Make a request on GitHub's API to research value in data
def getSearchResult(data):
    url = url_api + path_search
    return json.load(request(url, data, request_header))
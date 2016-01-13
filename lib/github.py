from lib.api_request import request
try:
    import json
except:
    import simplejson as json


github_api          = "https://api.github.com"
github_search       = "/search/repositories"

def getSearchGitHub(data):
    return json.load(request(github_api + github_search, data))
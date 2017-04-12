import os
import shutil
import xbmc
import xbmcvfs
from lib import info
from lib import tools
from lib import url_request
try:
    import json
except:
    import simplejson as json

__addonpath__   = info.__addonpath__

# Github advice to use this header
request_header  = { 'Accept' : 'application/vnd.github.v3.text-match+json' }
# URL to Github API
url_api         = 'https://api.github.com'
# Path to make a search for Github
path_search     = '/search/repositories'

tmpPath         = os.path.join(__addonpath__, 'tmp')

# Download a repository from Github
def downloadRepository(repository):
    if not xbmcvfs.exists(tmpPath + '/'):
        xbmcvfs.mkdir(tmpPath)
    pathToZip = tmpPath + '/' + tools.randomID() + '.zip'
    pathToAddon = os.path.dirname(__addonpath__) + '/' + repository['name']
    if not xbmcvfs.exists(pathToAddon + '/'):
        xbmcvfs.mkdir(pathToAddon)
    try:
        url_request.download(pathToZip,getDownloadPath(repository['full_name'],repository['default_branch']))
    except Exception as e:
        xbmc.log(msg=e.message, level=xbmc.LOGERROR)
        raise Exception(tools.translate(32103))
    try:
        tools.unzip(pathToZip,pathToAddon)
        shutil.rmtree(tmpPath)
    except Exception as e:
        xbmc.log(msg=e.message, level=xbmc.LOGERROR)
        # shutil.rmtree(tmpPath)
        raise Exception(e.message)

def getDownloadPath(fullName, defaultBranch):
    return url_api + '/repos/' + fullName + '/zipball/' + defaultBranch

# Make a request on GitHub's API to research value in data
def getSearchResult(data):
    try:
        url = url_api + path_search
        return json.load(url_request.request(url, data, request_header))
    except Exception as e:
        xbmc.log(msg=e.message, level=xbmc.LOGERROR)
        raise Exception(tools.translate(32102))
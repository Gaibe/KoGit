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

# Github advice to use this header
request_header  = { 'Accept' : 'application/vnd.github.v3.text-match+json' }
# URL to Github API
url_api         = 'https://api.github.com'
# Path to make a search for Github
path_search     = '/search/repositories'

# Download a repository from Github
def downloadRepository(repository):
    generatedTmpPath = os.path.join(tools.tmpPath, tools.randomID())
    if not xbmcvfs.exists(generatedTmpPath + '/'):
        xbmcvfs.mkdir(generatedTmpPath)
    pathToZip = generatedTmpPath + '/' + repository.name + '.zip'
    try:
        url_request.download(pathToZip,getDownloadPath(repository.fullName,repository.defaultBranch))
    except Exception as e:
        xbmc.log(msg=e.message, level=xbmc.LOGERROR)
        raise Exception(tools.translate(32103))
    try:
        tmpPathToUnzip = os.path.join(generatedTmpPath, repository.addonPath)
        pathToAddon = os.path.join(os.path.dirname(info.__addonpath__), repository.addonName)
        tools.unzip(pathToZip,generatedTmpPath)
        os.remove(pathToZip)
        folderName = os.listdir(generatedTmpPath)[0]
        pathToDownloadedAddon = os.path.join(generatedTmpPath, folderName)
        if repository.addonPath != '':
            pathToDownloadedAddon = os.path.join(pathToDownloadedAddon, repository.addonPath)
        os.rename(pathToDownloadedAddon, pathToAddon)
    except Exception as e:
        xbmc.log(msg=e.message, level=xbmc.LOGERROR)
        raise Exception(e.message)
    shutil.rmtree(tools.tmpPath)

# Get the complete path to download repository as zip
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
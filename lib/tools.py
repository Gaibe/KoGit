import uuid
import xbmc
import xbmcaddon
import xbmcgui
from zipfile import ZipFile
from lib import info

invalidFilesCharacters = ['\\','/',':','*','?','"','<','>','|']

def errorMessage(msg=''):
    if msg=='':
        msg=translate(32002)
    else:
        xbmc.log(msg=msg, level=xbmc.LOGERROR)
    return xbmcgui.Dialog().ok(info.__addonname__ + ' : Error', msg)

def hasInvalidFilesCharacters(fileName):
    isInvalid = False
    if any(letter in fileName for letter in invalidFilesCharacters):
        isInvalid = True
    return isInvalid

def randomID():
    return str(uuid.uuid4())[:10]

def translate(id):
    return xbmcaddon.Addon().getLocalizedString(id).encode('utf-8')

def unzip(pathToFile, pathToAddon):
    try:
        zip_ref = ZipFile(pathToFile, 'r')
        zip_ref.extractall(pathToAddon)
        zip_ref.close()
    except Exception as e:
        xbmc.log(msg=e.message, level=xbmc.LOGERROR)
        raise Exception('Error on unzipping file')
import xbmcaddon
import xbmcgui
from lib import info

def errorMessage():
    return xbmcgui.Dialog().ok(info.__addonname__, translate(32002))

def translate(id):
    return xbmcaddon.Addon().getLocalizedString(id).encode('utf-8')
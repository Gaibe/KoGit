import xbmcaddon


def translate(id):
    return xbmcaddon.Addon().getLocalizedString(id).encode('utf-8')

def errorMessage():
    return xbmcgui.Dialog().ok(addonname, translate(32002))
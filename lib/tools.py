import xbmcaddon


def translate(id):
      return xbmcaddon.Addon().getLocalizedString(id).encode('utf-8')
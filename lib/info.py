import xbmcaddon

__addon__       = xbmcaddon.Addon()
__addonname__   = __addon__.getAddonInfo('name')
__addonpath__   = __addon__.getAddonInfo('path')
__setting__     = __addon__.getSetting('launch-at-startup')
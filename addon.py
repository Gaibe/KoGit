import sys
import xbmc
import xbmcgui
import gui
from lib import tools
from lib import info
from lib import github

__addonname__       = info.__addonname__
translate           = tools.translate


while True:
    index = xbmcgui.Dialog().select(__addonname__, [translate(32101)])
    # GitHub selected
    if index == 0:
        keyboard = xbmc.Keyboard('2sec', translate(32020))
        keyboard.doModal()
        if keyboard.isConfirmed():
            value_search = keyboard.getText()
            search_result = github.getSearchResult({ 'q' : value_search })
            xbmcgui.Dialog().ok(__addonname__, search_result['items'][1]['downloads_url'])
        break
    else:
        break

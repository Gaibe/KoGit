import sys
import xbmcaddon
import xbmc
import xbmcgui
import gui
from lib import tools
from lib.github import *

addon               = xbmcaddon.Addon()
addonname           = addon.getAddonInfo('name')
launchAtStartUp     = addon.getSetting("launch-at-startup")
translate           = tools.translate

# TODO : resoudre le probleme avec sys.argv dans gui.py

gui.addItem("Mabite")
gui.endGui()



# while True:
#     index = xbmcgui.Dialog().select(addonname, [translate(32001)])
#     if index == 0:
#         # GitHub selected
#         to_search = "2sec"
#         search_result = getSearchGitHub({ "q" : to_search })

#         xbmcgui.Dialog().ok(addonname, search_result["items"][1]["downloads_url"], line2, line3)
#         break
#     else:
#         break


# Start of script
# if (__name__ == '__main__'):
#     window = window()
#     window.doModal()

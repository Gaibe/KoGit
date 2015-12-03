import sys
import xbmcaddon
import xbmc
# from xbmcgui import Dialog
import xbmcgui
from urllib2 import Request, urlopen, URLError
from lib import tools
import json


addon               = xbmcaddon.Addon()
addonname           = addon.getAddonInfo('name')
launchAtStartUp     = addon.getSetting("launch-at-startup")
translate           = tools.translate

line1 = "Hello World"
line2 = "Something is writing here "
line3 = "You are using Python "


while True:
    index = xbmcgui.Dialog().select(addonname, [translate(32001)])
    if index == 0:
        # GitHub selected
        to_search = "2sec"
        request = Request("https://api.github.com/search/repositories?q=%s" % (to_search))
        try:
            response = urlopen(request)
            search_result = json.load(response)

            xbmcgui.Dialog().ok(addonname, search_result["items"][1]["downloads_url"], line2, line3)
            break
        except URLError, e:
            xbmcgui.Dialog().ok(addonname, translate(32002))
    else:
        break
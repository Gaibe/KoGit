import xbmcaddon
import xbmcgui

addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

line1 = "Hello World"
line2 = "Something is writing here"
line3 = "You are using Python"

xbmcgui.Dialog().ok(addonname, line1, line2, line3)
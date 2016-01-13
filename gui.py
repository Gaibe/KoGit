import sys
import xbmcplugin
import xbmcgui
from lib import tools

translate           = tools.translate
addon_handle        = 0 # int(sys.argv[1])


def addItem(name,iconimage=''):
    item = xbmcgui.ListItem(name,iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    xbmcgui.Dialog().ok("TAMER", sys.argv[0])
    return xbmcplugin.addDirectoryItem(handle=addon_handle,url="",listitem=item,isFolder=False)

def endGui():
    return xbmcplugin.endOfDirectory(addon_handle)


# class window(xbmcgui.Window):

#     button_width = 100
#     button_height = 20

#     button_close_label = translate(32010)
#     button_close_posx = 80
#     button_close_posy = 370

#     button_repository = [
#         "Github",
#         "Bitbucket"
#     ]
#     button_repository_posx = 50
#     button_repository_posy = 20

#     def __init__(self):
#         self.setCoordinateResolution(6)

#         # self.list = xbmcgui.ControlList (10, 10, 300, 300)
#         # self.addControl(self.list)

#         self.button_close = self.closeButton()
#         self.addControl (self.button_close)

#         for repo in self.button_repository:
#             self.button_github = xbmcgui.ControlButton(
#                     self.button_repository_posx,
#                     self.button_repository_posy,
#                     self.button_width,
#                     self.button_height,
#                     label=repo)
#             self.addControl(self.button_github)
#             self.button_repository_posy += 40

#         # self.list.addItem("Github")
    
#     # Action on click
#     def repositoryGithub(self):
#         self.setCoordinateResolution(6)

#         to_search = "2sec"
#         self.response = getSearchGitHub({ "q" : to_search })["items"]


#         self.list = xbmcgui.ControlList (10, 10, 300, 300)
#         self.addControl(self.list)
#         for req in self.response:
#             self.list.addItem(req["downloads_url"])

#         self.button_close = self.closeButton()
#         self.addControl (self.button_close)
#         ActivateWindow(self)

#     def closeButton(self):
#         return xbmcgui.ControlButton(
#                 self.button_close_posx,
#                 self.button_close_posy,
#                 self.button_width,
#                 self.button_height,
#                 label=self.button_close_label)

#     def onControl(self,control):
#         if control == self.button_close:
#             self.close()
#         elif control == self.button_github:
#             self.repositoryGithub().doModal();

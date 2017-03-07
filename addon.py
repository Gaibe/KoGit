import sys
import xbmc
import xbmcgui
from lib import tools
from lib import info
from lib import github

__addonname__       = info.__addonname__
translate           = tools.translate
dialog              = xbmcgui.Dialog()
dialogProgress      = xbmcgui.DialogProgress()

while True:
    index = dialog.select(__addonname__, [translate(32101)])
    # GitHub selected
    if index == 0:
        keyboard = xbmc.Keyboard('2sec', translate(32020))
        keyboard.doModal()
        if keyboard.isConfirmed():
            value_search = keyboard.getText()
            dialogProgress.create(__addonname__,translate(32021),'...')
            dialogProgress.update(20,translate(32021),'...')
            search_result = github.getSearchResult({ 'q' : value_search })
            dialogProgress.update(50,translate(32021),'...')
            listResult=[]
            for singleResult in search_result['items']:
                if singleResult['full_name'] != None:
                    listResult.append(singleResult['full_name'])
            dialogProgress.update(100,translate(32021),'...')
            dialogProgress.close()
            select=dialog.select(translate(32022), listResult)
            if select>=0:
                selectedResult=search_result['items'][select]
        break
    else:
        break

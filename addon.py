import sys
import xbmc
import xbmcgui
from lib import github
from lib import info
from lib import tools

__addonname__       = info.__addonname__
translate           = tools.translate
dialog              = xbmcgui.Dialog()
dialogProgress      = xbmcgui.DialogProgress()

class Main:

    def __init__(self):
        while True:
            serverSelected = dialog.select(__addonname__, [translate(32101)])
            if serverSelected >= 0:
                keyboard = xbmc.Keyboard('2sec', translate(32020))
                keyboard.doModal()
                if keyboard.isConfirmed():
                    value_search = keyboard.getText()
                    dialogProgress.create(__addonname__,translate(32021),'...')
                    dialogProgress.update(20,translate(32021),'...')
                    try:
                        # Search for results
                        if serverSelected == 0:
                            # GitHub selected
                            searchResult = github.getSearchResult({ 'q' : value_search })

                        listResults = self.getResult(searchResult)
                        while True:
                            select=dialog.select(translate(32022), listResults)
                            if select >= 0:
                                selectedResult=searchResult['items'][select]
                                confirmed = dialog.yesno(heading=__addonname__,
                                    line1='Are you sure you want to install this repository ?',
                                    yeslabel='Download', nolabel='Cancel')
                                if confirmed == True:
                                    github.downloadRepository(selectedResult)
                                    break
                            else:
                                break
                        break
                    except Exception as e:
                        xbmc.log(msg=e.message, level=xbmc.LOGERROR)
                        dialogProgress.close()
                        tools.errorMessage(e.message)
                else:
                    break
            else:
                break


    def getResult(self,searchResult):
        dialogProgress.update(50,translate(32021),'...')
        listResult=[]
        for singleResult in searchResult['items']:
            if singleResult['full_name'] != None and singleResult['private'] == False:
                displayedResult = singleResult['full_name']
                if singleResult['description'] is not None:
                    displayedResult += ' ' + singleResult['description']
                displayedResult += ' ' + singleResult['downloads_url']
                listResult.append(displayedResult.encode('utf-8', 'ignore'))
        dialogProgress.update(100,translate(32021),'...')
        dialogProgress.close()
        return listResult

if (__name__ == '__main__'):
    Main()
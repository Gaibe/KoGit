import sys
import xbmc
import xbmcgui
from lib import github
from lib import info
from lib.repositoryInfo import repositoryInfo
from lib import tools

__addonname__       = info.__addonname__
translate           = tools.translate
dialog              = xbmcgui.Dialog()
dialogProgress      = xbmcgui.DialogProgress()

class Main:

    def __init__(self):
        while True:
            indexServer = dialog.select(__addonname__, [translate(32101)])
            if indexServer >= 0:
                keyboard = xbmc.Keyboard('2sec', translate(32020))
                keyboard.doModal()
                if keyboard.isConfirmed():
                    value_search = keyboard.getText()
                    dialogProgress.create(__addonname__,translate(32021),'...')
                    dialogProgress.update(20,translate(32021),'...')
                    try:
                        # Search for results
                        if indexServer == 0:
                            # GitHub selected
                            serverSelected='github'
                            searchResult = github.getSearchResult({ 'q' : value_search })
                        dialogProgress.update(50,translate(32021),'...')
                        listResults = self.getResult(searchResult)
                        dialogProgress.update(100,translate(32021),'...')
                        dialogProgress.close()
                        while True:
                            # Display Results
                            indexResult=dialog.select(translate(32022), listResults)
                            if indexResult >= 0:
                                selectedResult=repositoryInfo(serverSelected,searchResult['items'][indexResult])
                                repoInfo = translate(32023) + ' ' + selectedResult.name\
                                 + '\n' + translate(32024) + ' ' + selectedResult.ownerName\
                                 + '\n' + translate(32025) + ' ' + selectedResult.addonName\
                                 + '\n' + translate(32026) + ' ' + selectedResult.getRepoPathToAddon()
                                modifyDownload = dialog.yesno(heading=__addonname__,
                                    line1=repoInfo,
                                    yeslabel=translate(32012),
                                    nolabel=translate(32011))
                                if modifyDownload == False:
                                    self.download(serverSelected,selectedResult)
                                    break
                                else:
                                    self.modifyRepoInfo(selectedResult)
                                    break
                            else:
                                break
                        break
                    except Exception as e:
                        xbmc.log(msg=e.message,level=xbmc.LOGERROR)
                        dialogProgress.close()
                        tools.errorMessage(e.message)
                else:
                    break
            else:
                break

    def download(self, serverSelected, selectedResult):
        dialogProgress.create(__addonname__,translate(32031),'...')
        dialogProgress.update(35,translate(32031),'...')
        if serverSelected == 'github':
            github.downloadRepository(selectedResult)
        dialogProgress.update(100,translate(32031),'...')
        dialogProgress.close()


    def getResult(self, searchResult):
        listResult=[]
        for singleResult in searchResult['items']:
            if singleResult['full_name'] != None and singleResult['private'] == False:
                displayedResult = singleResult['full_name']
                if singleResult['description'] is not None:
                    displayedResult += ' ' + singleResult['description']
                listResult.append(displayedResult.encode('utf-8', 'ignore'))
        return listResult

    def modifyRepoInfo(self, selectedResult):
        resultHasChange = False
        while True:
            selectModifyList = [translate(32025) + ' ' + selectedResult.name,
                    translate(32026) + ' ' + selectedResult.getRepoPathToAddon()]
            indexModify = dialog.select(__addonname__,selectModifyList)
            if indexModify >= 0:
                if indexModify == 0:
                    validNewName = False
                    while validNewName == False:
                        newName = dialog.input(__addonname__,selectedResult.name,xbmcgui.INPUT_ALPHANUM)
                        validNewName = True
                        if newName != '':
                            if tools.hasInvalidFilesCharacters(newName):
                                validNewName = False
                                dialog.ok(__addonname__,
                                    translate(32027) + '\n' + (', '.join(tools.invalidFilesCharacters)))
                            else:
                                resultHasChange = True
                                selectedResult.name=newName
            else:
                break
        if resultHasChange == True:
            self.download(serverSelected,selectedResult)

### Iniatilize script ###
if (__name__ == '__main__'):
    Main()
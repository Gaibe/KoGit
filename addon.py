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
#           To uncomment if repository server is added
#           indexServer = dialog.select(__addonname__, [translate(32101)])
            indexServer = 0
            if indexServer >= 0:
                keyboard = xbmc.Keyboard('2sec', translate(32020))
                keyboard.doModal()
                if keyboard.isConfirmed():
                    value_search = keyboard.getText()
                    dialogProgress.create(__addonname__,translate(32021),'...')
                    try:
                        dialogProgress.update(20,translate(32021),'...')
                        # Search for results
                        if indexServer == 0:
                            # GitHub selected
                            self.serverSelected='github'
                            searchResult = github.getSearchResult({ 'q' : value_search })
                        if dialogProgress.iscanceled():
                            dialogProgress.close()
                            continue
                        dialogProgress.update(50,translate(32021),'...')
                        listResults = self.getResult(searchResult)
                        if dialogProgress.iscanceled():
                            dialogProgress.close()
                            continue
                        dialogProgress.update(100,translate(32021),'...')
                        dialogProgress.close()
                        while True:
                            # Display Results of search
                            indexResult=dialog.select(translate(32022), listResults)
                            if indexResult >= 0:
                                self.selectedResult=repositoryInfo(self.serverSelected,searchResult['items'][indexResult])
                                modifyDownload = dialog.yesno(heading=__addonname__,
                                        line1=self.selectedResult.getRepoInfo(),
                                        yeslabel=translate(32012),
                                        nolabel=translate(32011))
                                if modifyDownload == False:
                                    self.download()
                                    break
                                else:
                                    hasDownloaded = self.modifyRepoInfo()
                                    xbmc.log(msg=str(hasDownloaded),level=xbmc.LOGERROR)
                                    if hasDownloaded == True:
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

    def download(self):
        dialogProgress.create(__addonname__,translate(32031),'...')
        dialogProgress.update(35,translate(32031),'...')
        if self.serverSelected == 'github':
            github.downloadRepository(self.selectedResult)
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

    def modifyRepoInfo(self):
        resultHasChange = False
        hasDownloaded = False
        while True:
            selectModifyList = [translate(32025) + ' ' + self.selectedResult.addonName,
                    translate(32026) + ' ' + self.selectedResult.name + '/' + self.selectedResult.addonPath,
                    translate(32011)]
            indexModify = dialog.select(__addonname__+translate(32028),selectModifyList)
            if indexModify >= 0:
                if indexModify == 0:
                    # Modify name
                    validNewName = False
                    while validNewName == False:
                        newName = dialog.input(__addonname__,self.selectedResult.addonName,xbmcgui.INPUT_ALPHANUM)
                        validNewName = True
                        if newName != '':
                            if tools.hasInvalidFilesCharacters(newName):
                                # Check if name is valid for a folder
                                validNewName = False
                                dialog.ok(__addonname__,
                                    translate(32027) + '\n' + (', '.join(tools.invalidFilesCharacters)))
                            else:
                                resultHasChange = True
                                self.selectedResult.addonName = newName
                elif indexModify == 1:
                    # Modify path
                    newPath = dialog.input(__addonname__,self.selectedResult.addonPath,xbmcgui.INPUT_ALPHANUM)
                    resultHasChange = True
                    self.selectedResult.addonPath = newPath
                elif indexModify == 2:
                    # Download repo
                    self.download()
                    hasDownloaded = True
                    break
            else:
                if resultHasChange == True:
                    # Ask if discard modification
                    discardChange = dialog.yesno(heading=__addonname__,
                            line1=translate(32029),
                            yeslabel=translate(32014),
                            nolabel=translate(32013))
                    if discardChange == True:
                        break
                else:
                    break
        return hasDownloaded

### Iniatilize script ###
if (__name__ == '__main__'):
    Main()
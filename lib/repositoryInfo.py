
class repositoryInfo:

    def __init__(self,server, data):
        if server == 'github':
            self.setInfoFromGithub(data)

    def getRepoPathToAddon(self):
        return '/' + self.addonPath + '/'

    def setInfoFromGithub(self,data):
        self.name = data['name']
        self.fullName = data['full_name']
        self.ownerName = data['owner']['login']
        self.addonName = data['name']
        self.addonPath = data['name']
        self.defaultBranch = data['default_branch']
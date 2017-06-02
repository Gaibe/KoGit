from tools import translate

class repositoryInfo:

    def __init__(self, server, data):
        if server == 'github':
            self.setInfoFromGithub(data)

    def getRepoInfo(self):
        return translate(32023) + ' ' + self.name\
         + '\n' + translate(32024) + ' ' + self.ownerName\
         + '\n' + translate(32025) + ' ' + self.addonName\
         + '\n' + translate(32026) + ' ' + self.getRepoPathToAddon()

    def getRepoPathToAddon(self):
        path = '/' + self.name + '/'
        if self.addonPath != '':
            path = os.path.join(path, repository.addonPath)
        return path

    def setInfoFromGithub(self,data):
        self.name = data['name']
        self.fullName = data['full_name']
        self.ownerName = data['owner']['login']
        self.addonName = data['name']
        self.addonPath = ''
        self.defaultBranch = data['default_branch']
        self.size = data['size']
        self.dateCreation = data['created_at']
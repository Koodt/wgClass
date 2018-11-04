#!/usr/bin/python3

class GitClass(object):
    def __init__(self, repoTarget):
        from git import Repo
        self.Repo = Repo
        self.repoTarget = repoTarget

    def dlRepo(self, url):
        self.url = url
        self._repo = self.Repo.clone_from(self.url, self.repoTarget)
        self.repoW = self.Repo(self.repoTarget)

    def createNewBranch(self, branch):
        self.branch = branch
        self.newBranch = self.repoW.create_head(self.branch)

    def selectNeededBranch(self, branch='master'):
        self.branch = branch
        self.branchSwitch = self.repoW.git.checkout(self.branch)

    def commitAndPush(self):
        pass

    @property
    def repo(self):
        if self._repo is None:
            self.dlRepo()
        return self._repo


if __name__ == '__main__':
    newBranch = 'anotherBranch'
    wgClass = GitClass('/srv/kill')
    wgClass.dlRepo('https://github.com/Koodt/wgClass.git')
    wgClass.createNewBranch(newBranch)
    wgClass.selectNeededBranch(newBranch)

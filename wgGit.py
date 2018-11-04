#!/usr/bin/python3

class GitClass(object):
    def __init__(self, repoTarget):
        from git import Repo
        self.Repo = Repo
        self.repoTarget = repoTarget

    def dlRepo(self, url, path):
        self.url = url
        self.path = path
        self._repo = self.Repo.clone_from(self.url, self.path)

    def createNewBranch(self, branch):
        self.branch = branch
        self.repoW = self.Repo(self.repoTarget)
        self.newBranch = self.repoW.create_head(self.branch)

    def selectNeededBranch(self, branch):
        self.branch = branch
        self.repoW = self.Repo(self.repoTarget)
        self.branchSwitch = self.repoW.git.checkout(self.branch)

    def selectMasterBranch(self):
        self.repoW = self.Repo(self.repoTarget)
        self.new_branch = self.repoW.heads.master.checkout()

    def commitAndPush(self, repoTarget):
        self.repoTarget = repoTarget
        self

    @property
    def repo(self):
        if self._repo is None:
            self.dlRepo()
        return self._repo


if __name__ == '__main__':
    wgClass = GitClass('/srv/kill')
    wgClass.dlRepo('https://github.com/Koodt/wgClass.git')
    wgClass.createNewBranch('morenewBranch')
    wgClass.selectNeededBranch('morenewBranch')
#    wgClass.selectMasterBranch('/srv/kill')

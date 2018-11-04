#!/usr/bin/python3

class GitClass(object):
    def __init__(self, repoTarget):
        from git import Repo
        self.Repo = Repo
        self.repoTarget = repoTarget
        self.repoW = self.Repo(self.repoTarget)

    def dlRepo(self, url):
        self.url = url
        self._repo = self.Repo.clone_from(self.url, self.repoTarget)

    def createNewBranch(self, branch):
        self.branch = branch
        self.newBranch = self.repoW.create_head(self.branch)

    def selectNeededBranch(self, branch):
        self.branch = branch
        self.branchSwitch = self.repoW.git.checkout(self.branch)

    def selectMasterBranch(self):
        self.new_branch = self.repoW.heads.master.checkout()

    def commitAndPush(self):
        pass
        
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

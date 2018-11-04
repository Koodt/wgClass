#!/usr/bin/python3

class GitClass(object):
    def __init__(self, repoPath):
        from git import Repo
        self.Repo = Repo
        self.repoPath = repoPath
        try:
            self.currentRepo = self.Repo(self.repoPath)
        except:
            pass

    def dlRepo(self, url):
        from os import path
        self.url = url
        if not path.isdir(self.repoPath):
            self._repo = self.Repo.clone_from(self.url, self.repoPath)
            self.currentRepo = self.Repo(self.repoPath)
        else:
            print('Directory \'%s\' exist' % self.repoPath)

    def createNewBranch(self, branch):
        self.branch = branch
        if self.branch not in self.currentRepo.branches:
            self.newBranch = self.currentRepo.create_head(self.branch)
        else:
            print('Branch \'%s\' exist' % self.branch)

    def selectNeededBranch(self, branch='master'):
        self.branch = branch
        self.branchSwitch = self.currentRepo.git.checkout(self.branch)

    def commitAndPush(self, commitMessage):
        self.commitMessage = commitMessage
        self.currentRepo = self.Repo(self.repoPath)
        if not self.currentRepo.is_dirty():
            self.currentCommit = self.currentRepo.git.commit('-m', self.commitMessage)
            self.currentPush = self.currentRepo.git.push()

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
#    wgClass.commitAndPush('Test commit')

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
            self.Repo.clone_from(self.url, self.repoPath)
            self.currentRepo = self.Repo(self.repoPath)
        else:
            print('Directory \'%s\' exist' % self.repoPath)

    def createNewBranch(self, branch):
        self.branch = branch
        if self.branch not in self.currentRepo.branches:
            self.currentRepo.create_head(self.branch)
        else:
            print('Branch \'%s\' exist' % self.branch)

    def selectNeededBranch(self, branch='master'):
        self.branch = branch
        if self.currentRepo.active_branch != self.branch:
            self.currentRepo.git.checkout(self.branch)
        else:
            print('Needed branch already selected')

    def commitAndPush(self, commitMessage):
        self.commitMessage = commitMessage
        if self.currentRepo.is_dirty():
            self.currentRepo.git.add('--all')
        self.currentRepo.git.commit('-m', self.commitMessage)
        self.currentRepo.git.push()

if __name__ == '__main__':
    newBranch = 'anotherBranch'
    wgClass = GitClass('/srv/kill')
    wgClass.dlRepo('https://github.com/Koodt/wgClass.git')
    wgClass.createNewBranch(newBranch)
    wgClass.selectNeededBranch(newBranch)
#    wgClass.commitAndPush('Test commit')

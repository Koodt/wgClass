#!/usr/bin/python3
import sys
from wgClass import GitClass
import argparse

parser = argparse.ArgumentParser(description='wgClass example')
parser.add_argument('-r', '--repo', action='store', dest='repoPath', help='Path to cloned repo')
#parser.add_argument('-u', '--url', action='store', dest='repoURL', help='Cloned repo URL')
parser.add_argument('-b', '--branch', action='store', dest='newBranch', help='Branch name')
parser.add_argument('-c', '--clone', action='store_true', help='Clone repo')
results = parser.parse_args()


if __name__ == '__main__':
    wgClass = GitClass(results.repoPath)
    if results.clone:
        wgClass.dlRepo('https://github.com/Koodt/wgClass.git')

    sys.exit()
    wgClass.createNewBranch(results.newBranch)
    wgClass.selectNeededBranch(results.newBranch)
    wgClass.commitAndPush('Test commit', results.newBranch)

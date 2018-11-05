#!/usr/bin/python3
import sys
from wgClass import GitClass
import argparse

parser = argparse.ArgumentParser(description='wgClass example', usage='./wgGit.py -r /srv/kill -b TestBranch -cns')
parser.add_argument('-r', '--repo', action='store', dest='repoPath', help='Path to cloned repo')
#parser.add_argument('-u', '--url', action='store', dest='repoURL', help='Cloned repo URL')
parser.add_argument('-b', '--branch', action='store', dest='newBranch', help='Branch name')
parser.add_argument('-c', '--clone', action='store_true', help='Clone repo')
parser.add_argument('-n', '--newbranch', action='store_true', help='Create new branch')
parser.add_argument('-s', '--selectbranch', action='store_true', help='Select branch')
parser.add_argument('-p', '--commitandpush', action='store_true', help='Commit and push')


results = parser.parse_args()


if __name__ == '__main__':
    wgClass = GitClass(results.repoPath)
    if results.clone:
        wgClass.dlRepo('https://github.com/Koodt/wgClass.git')
    if results.newbranch:
        wgClass.createNewBranch(results.newBranch)
    if results.selectbranch:
        wgClass.selectNeededBranch(results.newBranch)
    if results.commitandpush:
        wgClass.commitAndPush('Test commit', results.newBranch)

    sys.exit()

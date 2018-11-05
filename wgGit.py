#!/usr/bin/python3
from wgClass import GitClass
import argparse

parser = argparse.ArgumentParser(description='wgClass example')
parser.add_argument('-r', '--role', action='store', dest='khomeRole', help='select role from collector and harvester')
parser.add_argument('-f', '--file', action='store', dest='filename', nargs='?', type=argparse.FileType('r'), help='Set full path to parsing file')
results = parser.parse_args()

if __name__ == '__main__':
    newBranch = 'anotherBranch'
    wgClass = GitClass('/srv/kill')
#    wgClass.dlRepo('https://github.com/Koodt/wgClass.git')
#    wgClass.createNewBranch(newBranch)
#    wgClass.selectNeededBranch(newBranch)
    wgClass.commitAndPush('Test commit', newBranch)

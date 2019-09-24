import git_util
import sys


def delete_branches(input):
    if len(input) == 0:
        ticket = ''
    else:
        ticket = input[0]
    branches = git_util.find_branches(ticket)
    if len(branches) == 0:
        print("Not found in local")
    else:
        show_branches(branches)


def show_branches(branches):
    for branch in branches:
        if input('delete ' + branch + " (y/n)?:   ") == 'y':
            git_util.delete_branch(branch)


delete_branches(sys.argv[1:])


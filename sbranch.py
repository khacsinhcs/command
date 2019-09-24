import git_util
import sys


def switch_branch(input):
    ticket = input[0]
    branches = git_util.find_branches(ticket)
    if len(branches) == 0:
        print("Not found in local, finding in origin")
        branches = git_util.find_in_remote(ticket)
        if len(branches) == 0:
            print("Could not find branch for " + ticket + ", create new branch with command nbranch")
        else:
            show_branches(branches)
    elif len(branches) == 1:
        branch = branches[0]
        git_util.checkout(branch)
    else:
        show_branches(branches)


def show_branches(branches):
    i = 1
    for branch in branches:
        print("* [" + str(i) + '] ' + branch)
        i = i + 1

    index = input("Which do you want: ")
    git_util.checkout(branches[int(index) - 1])
    exit()


switch_branch(sys.argv[1:])


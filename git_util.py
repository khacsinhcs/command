import cmd
import re


def get_current_branch():
    result = cmd.run_command("git rev-parse --abbrev-ref HEAD")
    return result.split("\n")[0].strip()


def is_master():
    return get_current_branch() == "master"


def get_ticket_number():
    if is_master():
        print("can't get ticket number from master")
        return None
    else:
        branch = get_current_branch()
        ticket = '[A-Z]{3}-[0-9]+'
        x = re.search(ticket, branch)
        if x is None:
            return None
        return branch[x.start():x.end()]


def build_branches(comand):
    branches = cmd.run_command(comand).split("\n")
    result = []
    for branch in branches:
        trim = branch.strip()
        if len(trim) != 0:
            result.append(trim)

    return result


def find_branches(pattern):
    return build_branches("git branch | grep " + pattern)


def find_in_remote(pattern):
    return build_branches("git branch -a | grep " + pattern)


def checkout(branch):
    if 'remotes/origin/' in branch:
        cmd.run_command('git checkout ' + branch[len('remotes/origin/'):])
    else:
        cmd.run_command("git checkout " + branch)



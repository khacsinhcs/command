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

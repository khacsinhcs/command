import cmd
import sys
import git_util

JENKINS = "http://jenkins.dev.idnow.de/"


def open_jenkins(path):
    cmd.run_command("open " + JENKINS + path)


def release(part):
    print("  BranchOrTag: " + git_util.get_current_branch())
    ticket = git_util.get_ticket_number()
    if ticket is not None:
        print("   TagVersion: " + ticket.lower() + '-rc.')
    if part == "ai":
        open_jenkins("view/AutomatedProduct/job/Automated%20Product%20Release/build")
    else:
        open_jenkins("view/Releases/job/Release/build")


def deploy(part):
    if part == "ai":
        open_jenkins("view/AutomatedProduct/job/DEPLOY_TPP_DEV2/build")
    else:
        open_jenkins("view/DEV/job/Deploy%20Dev2/build")


def __main___job(arr):
    if len(arr) == 2:
        job = arr[0]
        if job == 'release':
            release(arr[1])
        else:
            deploy(arr[1])
    else:
        open_jenkins("")


__main___job(sys.argv[1:])

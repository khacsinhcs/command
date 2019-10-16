import cmd
import sys
import git_util

JENKINS = "http://jenkins.dev.idnow.de/"


def open_jenkins(path):
    cmd.run_command("open " + JENKINS + path)


def release(part):
    branch = git_util.get_current_branch()
    print("  BranchOrTag: " + branch)
    cmd.copy2clip(branch)
    ticket = git_util.get_ticket_number()
    if ticket is not None:
        print("   TagVersion: " + ticket.lower() + '-rc.')
    if part == "ai":
        open_jenkins("view/AutomatedProduct/job/Release%20Automated%20Product/build")
    else:
        open_jenkins("view/Releases/job/Release/build")


def deploy(part):
    if part == "ai":
        open_jenkins("view/AutomatedProduct/job/Deploy%20Automated%20Product%20Dev2/build")
    else:
        open_jenkins("view/DEV/job/Deploy%20Dev2/build")


def unit_test():
    project = cmd.run_command("pwd -P").split('/')[-1].replace('\n', '')
    branch = git_util.get_current_branch().replace('/', '%252F')
    link = 'job/idnowgmbh/job/' + project + '/job/' + branch
    print(link)
    open_jenkins(link)


def __main___job(arr):
    if len(arr) == 1:
        job = arr[0]
        project = cmd.run_command("pwd -P").split('/')[-1].replace('\n', '')
        if job == 'test':
            unit_test()
        elif job == 'release':
            if 'ai' in project:
                release('ai')
            else:
                release('core')
        else:
            if 'ai' in project:
                deploy('ai')
            else:
                deploy('core')
        exit()
    if len(arr) == 2:
        job = arr[0]
        if job == 'release':
            release(arr[1])
        else:
            deploy(arr[1])
    else:
        open_jenkins("")


__main___job(sys.argv[1:])

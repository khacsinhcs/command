import sys

import cmd
import git_util


def start(repo, ticket):
    cmd.execute('watson stop')
    if ticket is None:
        cmd.execute('watson start ' + repo)
    else:
        cmd.execute('watson start ' + repo + ' +' + ticket)


def start_tracking():
    ticket_number = git_util.get_ticket_number()
    repo = git_util.get_repo_name()
    start(repo, ticket_number)


def stop_tracking():
    cmd.execute('watson stop')


def __main__(input):
    if 'start' in input:
        start_tracking()

    if 'stop' in input:
        stop_tracking()


__main__(sys.argv[1:])


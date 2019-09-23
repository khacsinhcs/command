import sys
import os
import git_util

JIRA = "https://idnowgmbh.atlassian.net"


def run_command():
    if len(sys.argv) == 1:
        ticket = git_util.get_ticket_number()
        if ticket is None:
            os.system("open " + JIRA)
        else:
            url = JIRA + "/browse/" + ticket
            os.system("open " + url)
        exit()

    issue = sys.argv[1]
    url = JIRA

    if issue == "my":
        url = url + "/secure/RapidBoard.jspa?rapidView=68&projectKey=SGN&assignee=5ba892e01c4dd76faa1392d5"
    elif issue == "board":
        url = url + "/secure/RapidBoard.jspa?rapidView=68&projectKey=SGN"
    else:
        url = url + "/browse/SGN-" + issue

    os.system("open " + url)


run_command()

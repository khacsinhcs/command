import cmd

JENKINS = "http://jenkins.dev.idnow.de/"

def open_jenkins(path):
    cmd.run_command("open " + JENKINS + path)



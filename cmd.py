import subprocess
import os
import pyperclip


def run_command(command):
    p = subprocess.Popen(command,
                         stdout=subprocess.PIPE,
                         shell=True)
    (output, err) = p.communicate()
    p.wait()
    return output


def execute(command):
    os.system(command)


def copy2clip(txt):
    pyperclip.copy(txt)


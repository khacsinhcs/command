import subprocess


def run_command(command):
    p = subprocess.Popen(command,
                         stdout=subprocess.PIPE,
                         shell=True)
    (output, err) = p.communicate()
    p.wait()
    return output

import os
import cmd
import sys

port = {
    'ai': '4000',
    'application': '9000',
    'web': '7000',
    'customerportal': '11000',
    'gateway': '5000'
}


def start_service():
    path = cmd.run_command('pwd')
    for key in port.keys():
        if key in path:
            command = 'sbt clean compile stage && ./target/universal/stage/bin/' + key + ' -Dhttp.port=' + port[key]
            os.system(command)


def __main__(input):
    start_service()


__main__(sys.argv[1:])

import sys
import cmd

username = 'sle'
input = sys.argv[1:]
name = input[0] + '/' + username + '/SGN-' + input[1].upper()
for text in input[2:]:
    name = name + '_' + text

cmd.run_command('git checkout master')
cmd.run_command('git pull')
cmd.run_command('git checkout -b ' + name)
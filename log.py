import cmd
import sys

GRAYLOG = 'https://graylog01.dev.idnow.de/'

streams = {
    'dev': '59355afae8288655e4032f29',
    'dev2': '5b55ecc346e0fb0017337a72',
    'dev3': '5bfd8d89dc0e82633d6648e1',
    'dev4': '5bfdbe0fdc0e82633d667db5',
    'test': '59355b86e8288655e4032fc2',
    'tst': '59355b86e8288655e4032fc2',
    'test3': '59355c3ce8288655e403308d',
    'tst3': '59355c3ce8288655e403308d'
}


prefix = {
    'DV2': 'dev2',
    'DV3': 'dev3',
    'TST': 'test',
    'TS3': 'test3'
}

def open_path(path):
    cmd.run_command('open ' + GRAYLOG + path)


def open_stream(stream):
    stream_key = streams.get(stream)
    if stream_key is None:
        print("Could not find stream " + stream)
    else:
        open_path("streams/" + stream_key + "/search")


def open_ident(token):
    pre_token = token.split('-')[0]
    env = prefix.get(pre_token)
    if env is None:
        print("Unknow host " + env)
    else:
        stream_key = streams.get(env)
        open_path("streams/" + stream_key + "/search?q=internalToken%3A" + token + '\&relative=604800')


def __main_job__(input):
    if len(input) == 0:
        open_path("streams")
    else:
        first = input[0]
        if '-' in first:
            open_ident(first)
        else:
            open_stream(first)


__main_job__(sys.argv[1:])

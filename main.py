import base64
import sys
from typing import List


def app_help():
    return 'usage: b64ed [-f | -e | -d | -h | help | man] [stringFile]\n' \
           '\t-f -> Encode file in base64. If you use this option, it is recommended\n' \
           '\t      to use `pbcopy` due to large result:\n' \
           '\t\t    example: base64ed -f /path/to/file | pbcopy\n' \
           '\t-e -> Encode string in base64\n' \
           '\t-d -> Decode base64 string\n' \
           '\t-h/help/man -> Print this help.\n' \
           '\tstringFile -> String or path to encode/decode. Mandatory with -e/d/f options.'


def main():
    arguments: List[str] = sys.argv
    if len(arguments) > 1:
        if arguments[1] in ['-h', 'help', 'man']:
            print(app_help())
        elif arguments[1] in ['-f', '-e', '-d'] and len(arguments) > 2:
            result: str
            if arguments[1] == '-f':
                # TODO catch open/read file errors
                # TODO extract file image from base64 file/text
                result = base64.b64encode(open(arguments[2], "rb").read()).decode('utf-8')
            elif arguments[1] == '-e':
                result = base64.encodebytes(bytes(arguments[2], encoding='utf8')).decode('utf-8"')
            else:
                result = base64.decodebytes(bytes(arguments[2], encoding='utf8')).decode('utf-8')
            print(result.replace('\n', ''), end='')
        else:
            print(f'ERROR -> Invalid arguments.\n{app_help()}')
    else:
        print(f'ERROR -> You must specify at least one argument.\n{app_help()}')


if __name__ == '__main__':
    main()

import base64
import sys


def app_help():
    return 'usage: ./main.py [-e | -d | -h | help | man] [stringFile]\n' \
           '\t-e -> Encode string in base64\n' \
           '\t-d -> Decode base64 string\n' \
           '\t-h/help/man -> Print this help.\n' \
           '\tstringFile -> String to encode/decode. Mandatory with -e/d options.'


def main():
    arguments = sys.argv
    if len(arguments) > 1:
        if arguments[1] in ['-h', 'help', 'man']:
            print(app_help())
        elif arguments[1] in ['-e', '-d'] and len(arguments) > 2:
            if arguments[1] == '-e':
                print(base64.encodebytes(bytes(arguments[2], encoding='utf8')).decode('utf-8"'))
            if arguments[1] == '-d':
                print(base64.decodebytes(bytes(arguments[2], encoding='utf8')).decode('utf-8'))
        else:
            print(f'ERROR -> Invalid arguments.\n{app_help()}')
    else:
        print(f'ERROR -> You must specify at least one argument.\n{app_help()}')


if __name__ == '__main__':
    main()

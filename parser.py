import sys
from comment_parser import comment_parser

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def get_filename():
    if (len(sys.argv) > 1):
       filename = sys.argv[1]
    else:
       filename = input( bcolors.OKBLUE + "Please enter the full path of the file:" + bcolors.ENDC)
    return filename
 

def parse_comments():
    try:
        filename = get_filename()
        comments = comment_parser.extract_comments(filename)
        comm = ''
        if len(comments) > 0:

            print(bcolors.OKGREEN + 'I\'ve found the following comments in your file:'+ bcolors.ENDC)
            print("="*25)
            for c in comments:
                comm = comm + c.text()
                print(c.text())
            print("="*25)
            words_list = comm.split()
            print(bcolors.BOLD + bcolors.WARNING + "Number of words: " + bcolors.ENDC + str(len(words_list)))
    except FileNotFoundError:
        print(bcolors.FAIL + 'Error: File not found!' + bcolors.ENDC)
    except comment_parser.UnsupportedError:
        print(bcolors.FAIL + 'Error: Unsupported file type!' + bcolors.ENDC)


if __name__ == '__main__':
    parse_comments()

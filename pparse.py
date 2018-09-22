#!/usr/bin/env python3

'''pparse will accept file,text blob, or url string as input. pparse will translate found ProofPoint URL's, replace them, and output to file or stdout
'''
__author__ = ["Matt Rosenberg"]
__credits__ = ["Matt Rosenberg"]
__license__ = "GNU GPL v3"
__version__ = "0.1"
__maintainer__ = ["Matt Rosenberg"]
__email__ = ["wirebandit@protonmail.com"]
__status__ = "Development"

import argparse
import logging
import re
from urllib.parse import parse_qs, unquote, urlparse


## SECTION - Logging

# Set logging level
if debug:
    debug_level = 'DEBUG'
else:
    debug_level = 'INFO'

# Create basic logging
logging.basicConfig(
        level=debug_level
        filename=debug_file,
        filemode='a',
        format='%(asctime)s:%(levelname)s:%(message)s')

## SECTION - Functions

def translate_url(data):
    try:
        logging.DEBUG('Decoding URL..')
        decoded = unquote(parse_qs(urlparse(url).query)['u'][0].translate(str.maketrans('-_', '%/')))
        logging.INFO('Decoded URL: {}'.format(decoded))
        return decoded
    except Exception as e:
        logging.CRITICAL('Error while parsing URL: {}'.format(e))



def parse_text(data):
    logging.DEBUG('URL Found in string. Making attempt to decode.')
    regex = re.compile('https://urldefense\.proofpoint\.com/v\d/url\?\S+=', re.IGNORECASE)
    cleaned_string = re.sub(regex, lambda m: translate_url(m.group()), data)
    return cleaned_string


def findall_url(data):
    regex = re.compile('https://urldefense\.proofpoint\.com/v\d/url\?\S+=', re.IGNORECASE)
    while True:
        if re.search(regex, data):
            data = parse_text(data)
            continue
        else:
            break
    return data


def write_out():
    #TODO add function to write to file


def main(arguments):

    # Setup arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', dest='in_file', help='File to parse')
    parser.add_argument('-b', '--blob', dest='in_blob', help='Accepts a blob of text surround in quotes')
    parser.add_argument('-u', '--url', dest='in_url', help='Url to parse')
    parser.add_argument('-o', '--outfile', dest='out_file', help='Filename of output file')
    parser.add_argument('-O', '--overwrite', dest='overwrite', default=False, action='store_true', help='Overwrites existing file. Use with -f')
    parser.add_argument('--debug',dest='debug', default=False, action='store_true' )
    parser.add_argument('--debug_file', dest='debug_file', default='pparse.log', help='Filename of debuglog')


    args = parser.parse_args(arguments)

    # TODO perform functions on input
    if in_file:
        pass
    elif in_blob:
        pass
    elif in_url:







if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
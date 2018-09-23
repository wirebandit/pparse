#!/usr/bin/env python3

"""
pparse will accept file,text blob, or url string as input. pparse will translate found ProofPoint URL's, replace them, and output to file or stdout
"""
__author__ = ["Matt Rosenberg"]
__credits__ = ["Matt Rosenberg"]
__license__ = "GNU GPL v3"
__version__ = "0.2"
__maintainer__ = ["Matt Rosenberg"]
__email__ = ["wirebandit@protonmail.com"]
__status__ = "Development"

import argparse
import logging
import re
from urllib.parse import parse_qs, unquote, urlparse
import sys

# Global Vars
regex = re.compile('https://urldefense\.proofpoint\.com/v\d/url\?\S+=', re.IGNORECASE)


## SECTION - Functions

def translate_url(data):
    try:
        logging.debug('Decoding URL..')
        decoded = unquote(parse_qs(urlparse(data).query)['u'][0].translate(str.maketrans('-_', '%/')))
        logging.info('Decoded URL: {}'.format(decoded))
        return decoded
    except Exception as e:
        logging.error('Error while parsing URL: {}'.format(e))
        print('Error: {}'.format(e))


def parse_text(data):
    logging.debug('URL Found in string. Making attempt to decode.')
    cleaned_string = re.sub(regex, lambda m: translate_url(m.group()), data)
    return cleaned_string


def findall_url_write(data, fh):
    while True:
        if re.search(regex, data):
            data = parse_text(data)
            continue
        else:
            try:
                fh.write(data)
                break
            except IOError:
                logging.error('Error: {}'.format(e))
                print('Error: {}'.format(e))


# def write_out():
# TODO add function to write to file

def main(arguments):
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', dest='in_file', help='File to parse')
    parser.add_argument('-b', '--blob', dest='in_blob', help='Accepts a blob of text surround in quotes')
    parser.add_argument('-u', '--url', dest='in_url', help='Url to parse')
    parser.add_argument('-o', '--outfile', dest='out_file', help='Filename of output file')
    parser.add_argument('-O', '--overwrite', dest='overwrite', default=False, action='store_true',
                        help='Overwrites existing file. Use with -f')
    parser.add_argument('--debug', dest='debug', default=False, action='store_true')
    parser.add_argument('--debug_file', dest='debug_file', help='Filename of debuglog')

    args = parser.parse_args()

    ## SECTION - Logging
    # Set logging level
    if args.debug:
        debug_level = logging.DEBUG
    else:
        debug_level = logging.INFO

    if not args.debug_file:
        debug_file = 'pparse.log'

    # Create basic logging
    logging.basicConfig(
            level=debug_level,
            filename=debug_file,
            filemode='a',
            format='%(asctime)s:%(levelname)s:%(message)s')

    # TODO perform functions on input
    logging.info("""
    ============================== START ==============================
    """)
    if args.in_file:
        # Open File and read contents to list 'data'
        try:
            logging.info('Opening input file: {}'.format(args.in_file))
            fh = open(args.in_file)
            data_list = []
            data_list = [l for l in fh.readlines() if l not in data_list]

        except IOError as e:
            logging.error('Error opening {}: {}'.format(args.in_file, e))
            print('Error opening {}: {}'.format(args.in_file, e))
        finally:
            try:
                fh.close()
            except Exception as e:
                logging.error('unable to close file')
                print('Error: {}'.format(e))
        # Open file to write out
        try:
            if args.overwrite:
                fh = open(args.in_file, 'w')
                filename = args.in_file
            elif args.out_file:
                fh = open(args.out_file, 'w')
                filename = args.out_file
            for line in data_list:
                logging.debug('Filename set to {}'.format(filename))
                findall_url_write(line, fh)
                logging.info('Succcessfully wrote to {}'.format(filename))
        except Exception as e:
            logging.error('ERROR Writing File {}: {}'.format(filename, e))
            print('Error: {}'.format(e))
        finally:
            fh.close()
            logging.debug('Closing file')
            logging.info("""
            ============================== END ==============================
            """)
    elif args.in_blob:
        pass
    elif args.in_url:
        pass


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
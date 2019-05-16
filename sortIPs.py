#!/usr/bin/env python
#
# sortIPs.py
# A script to read IP addresses from a text file, sort in
# ascending order, and output a file containing that list 
# with duplicate entries removed

import sys,argparse,ipaddress

# Function Defs
def sortIPs():
    iplist = args.file.readlines()
    uniq = list(set(iplist))
    ips = sorted(ipaddress.ip_address(line.strip()) for line in uniq)
    ipsorted = '\n'.join(map(str, ips))
    with open('SortedIPs.txt', 'w') as f:
        print(ipsorted, file=f)

# CLI arguments & arg parser
ex = '''example:
python sortIPs.py file.txt'''
parser = argparse.ArgumentParser(prog='sortIPs',
                                description='Outputs a file containing sorted list of IPs.',
                                epilog=ex,
                                formatter_class=argparse.RawDescriptionHelpFormatter,
                                )
parser.add_argument('file', type=argparse.FileType('r'))
parser.set_defaults(func=sortIPs)
args = parser.parse_args()

def main():
    args.func()

if __name__ == "__main__":
    sys.exit( main() )

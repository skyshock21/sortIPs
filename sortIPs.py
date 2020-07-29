#!/usr/bin/python3
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

def sanitizeIPs():
    #TO-DO replace . with [.]
    #TO-DO replace : with [:]
    iplist = args.file.readlines()
    uniq = list(set(iplist))
    ips = sorted(ipaddress.ip_address(line.strip()) for line in uniq)
    ipsorted = '\n'.join(map(str, ips))
    #TO-DO sanitize ipsorted var 
    ipsanitized = ipsorted.replace(".", "[.]").replace(":", "[:]")
    with open('IOCs.txt', 'w') as f:
        print(ipsanitized, file=f)

# CLI arguments & arg parser
ex = '''example:
python3 sortIPs.py file.txt
python3 sortIPs.py -x file.txt'''
parser = argparse.ArgumentParser(prog='sortIPs',
                                description='''Outputs a sorted list of IPs or IOCs''',
                                epilog=ex,
                                formatter_class=argparse.RawDescriptionHelpFormatter,
                                )
parser.add_argument('file', type=argparse.FileType('r'))
parser.add_argument('-x', help='Sanitized IOC output', action='store_true')
parser.set_defaults(func=sortIPs)
args = parser.parse_args()

def main():
    if args.x:
        sanitizeIPs()
    else:
        args.func()

if __name__ == "__main__":
    sys.exit( main() )

#!/usr/local/bin/python2.7
"""list ISY vars demo app
 
Usage: %(program)s [options] [localhost:localport [remotehost:remoteport]]
 
Options:
 
    --list

"""

import ISY
import sys

import getopt



def list_vars(myisy) :
    fmt = "%-4s : %-19s%-5s\t%-5s\t%s"
    print fmt % ( "ID", "NAME", "VAL", "INIT", "DATE" )
    for var in myisy.var_iter() :
        print fmt % ( var.id, var.name, var.value, var.init, var.ts )

def usage(code, msg=''):
    print >> sys.stderr, __doc__ % globals()
    if msg:
        print >> sys.stderr, msg
    sys.exit(code)

class Options:
    debug = 0

def parseargs():
    try:
        opts, args = getopt.getopt(
            sys.argv[1:], "v:lhd:",
            ['var=', 'list', 'help', 'debug'])
    except getopt.error, e:
        usage(1, e)
 
    options = Options()
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            usage(0)
        elif opt in ('-l', '--list'):
            options.list = 1
        elif opt in ('-d', '--debug'):
            options.debug = arg 

    return options

if __name__ == '__main__':

    options = parseargs()
    myisy = ISY.Isy( debug=options.debug )

    list_vars(myisy)
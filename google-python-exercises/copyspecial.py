#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def copying(dir1, todir):
    list_dir = os.listdir(dir1)
    for files in list_dir:
	path = os.path.join(dir1, files)
	path1 = os.path.abspath(path)
	if not os.path.abspath(dir2):
	    os.mkdir(dir2)
	path2 = os.path.abspath(dir2)
	shutil.copy(path1, path2)
    return

def zipfile(dir1, tozip):
    list_dir = os.listdir(dir1)
    cmd = 'zip - j' + tozip 
    for files in list_dir:
	path1 = os.path.abspath(os.path.join(dir1, files))
	(status, output) = commands.getstatusoutput(cmd + path1)
	if status:
	    print output
	    sys.exit(1)

def main():
    # This basic command line argument parsing code is provided.
    # Add code to call your functions below.

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
        sys.exit(1)

    # todir and tozip are either set from command line
    # or left as the empty string.
    # The args array is left just containing the dirs.
    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    tozip = ''
    if args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]

    if len(args) == 0:
        print "error: must specify one or more dirs"
        sys.exit(1)

    # +++your code here+++
    # Call your functions
#    if dir1 in args:
#	files = os.listdir(dir1)
    if todir:
	copying(dir1, todir)
    if tozip:
	zipfile(dir1, tozip)
	
if __name__ == "__main__":
    main()
  
if __name__ == "__main__":
  main()

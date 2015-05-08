import os, glob, pprint

print os.getcwd()

print os.path.join(os.path.expanduser('~'),'dir','subdir','k.py')

pathname = "/Users/dir/subdir/k.py"

(directory,filename) = os.path.split(os.path.realpath('argumentPass.py'))
print 'Directory - ', directory
(shortname,extension) = os.path.splitext(filename)
print 'Extension - ', extension


print glob.glob('*.py')

metadata = os.stat('argumentPass.py')

print 'All py files here - ', metadata

print os.path.realpath('argumentPass.py')
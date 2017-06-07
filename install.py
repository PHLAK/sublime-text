#!/usr/bin/env python3

from glob import glob

import os

workingdir = os.path.dirname(os.path.realpath(__file__))
sublime_config_dir = os.path.join(os.path.expanduser('~'), '.config/sublime-text-3/Packages/User')

settings = glob(os.path.join(workingdir, 'config/*.sublime-*'))
snippets = glob(os.path.join(workingdir, 'snippets/*.sublime-*'))
keymaps = glob(os.path.join(workingdir, 'keymaps/*.sublime-*'))

files = settings + snippets + keymaps

def symlinkFile(path):
    """Symlink a single config file"""

    basename = os.path.basename(path)
    livepath = os.path.join(sublime_config_dir, basename)

    if os.path.isfile(livepath) and not os.path.islink(livepath):
        print('Deleting existing file ' + basename + ' ... ', end='')
        os.remove(livepath)
        print('DONE')

    if not os.path.islink(livepath):
        print('Symlinking ' + basename + ' ... ', end='')
        os.symlink(path, livepath)
        print('DONE')

def main():
    """Main execution function"""

    if not os.path.isdir(sublime_config_dir):
        print('No config directory found at ' + sublime_config_dir + ', is Sublime Text installed?')
        exit(1)

    for path in files:
        symlinkFile(path)

if __name__ == '__main__':
    main()

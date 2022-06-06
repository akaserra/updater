# Import modules

import os
import time
import shutil
import urllib.request

FILE_Version = urllib.request.urlopen('https://raw.githubusercontent.com/akaserra/updater/main/Version/Version.txt').read().decode('utf8').splitlines()[0]  # Raw of Version.txt repository file
FILE_Changelogs = urllib.request.urlopen('https://raw.githubusercontent.com/akaserra/updater/main/Version/Changelogs.txt').read().decode('utf8')  # raw of changelog.txt repository file
FILE_Link = 'https://codeload.github.com/akaserra/updater/zip/refs/heads/main'  # file download link
FILE_Path = 'updater-main.zip'  # Name of the .zip file

# Checking version of file


def version():
    print('I\'m looking for new updates...')
    time.sleep(2)
    if FILE_Version == '3':
        print('No available updates.')
        input('Press enter to continue...')
    else:
        sc = input('Update available. Update now? y/n: ')
        if sc == 'y'.lower():
            print('\nDownloading update...')
            urllib.request.urlretrieve(FILE_Link, FILE_Path)
            print('Unpacking archive...')
            shutil.unpack_archive(FILE_Path, 'Updated Version ' + FILE_Version)
            os.remove(FILE_Path)
            time.sleep(3)
            print('Update installed.')
            input('Press enter for see the changelogs...')
            print('\nChangelogs:\n' + FILE_Changelogs + '\n')
            time.sleep(3)
            input('Press enter to continue...')
        elif sc == 'n'.lower():
            print('Ok.')
            input('Press enter to continue...')
        else:
            print('You can write only y or n.')
            input('Press enter to continue...')
            version()


version()

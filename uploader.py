import sys
import os
import tarfile
import shutil

version = os.environ['GITHUB_REF'].split('/')[-1]
print(f'version: {version}')

_, os_name, token = sys.argv
print('token length: ', len(token))
osn = os_name.split('-')[0]

folder_name = os.path.realpath('./dist/Ninja-Preview/')

# Download Qmlview archive for os
# extract to folder
# copy all those contents to folder_name, skipping the existing ones

# Build archives
if os_name == 'windows-latest':
    # zip file
    old_file = shutil.make_archive('Ninja_Preview', 'zip', folder_name)
    filename = f'qmlview_{version}_{osn}.zip'
    os.rename(old_file, filename)

else:
    # tar.gz file
    old_file = shutil.make_archive('Ninja_Preview', 'gztar', folder_name)
    filename = f'qmlview_{version}_{osn}.tar.gz'
    os.rename(old_file, filename)


print(f'filename: {filename}')

with open('token.txt', 'w') as tok:
    tok.write(token)
    print('Finished writing token file')

# Login to GH
cmd = 'gh auth login --with-token < token.txt'
os.system(cmd)
print('Authenticated')
cmd1 = f'gh release upload {version} {filename}'
os.system(cmd1)
print('All Done')

import sys
import os
import tarfile
import shutil
import glob

version = os.environ['GITHUB_REF'].split('/')[-1]
print(f'version: {version}')

_, os_name, token = sys.argv
print('token length: ', len(token))
osn = os_name.split('-')[0]
cwd = os.path.realpath('.')

folder_name = os.path.realpath('./dist/Ninja-Preview/')

# Download Qmlview archive for os
# extract to folder
# copy all those contents to folder_name, skipping the existing ones


# Login to GH
with open('token.txt', 'w') as tok:
    tok.write(token)
    print('Finished writing token file')

cmd = 'gh auth login --with-token < token.txt'
os.system(cmd)
print('Authenticated')


# Build archives
if os_name == 'windows-latest':
    # Download Qmlview archive for os
    os_cmd = 'gh release download --pattern "*.zip"'
    os.system(os_cmd)
    print('done wit download')
    print(os.listdir(cwd))
    # extract to folder
    arch = glob.glob('*.zip')[0]
    shutil.unpack_archive(arch, extract_dir=folder_name)
    # copy all those contents to folder_name, skipping the existing ones
    print('done wit unpack')
    print(os.listdir(folder_name))
    # instead of a zip make Inno setup file
    # zip file
    old_file = shutil.make_archive('Ninja_Preview', 'zip', folder_name)
    filename = f'Ninja_Preview_{version}_{osn}.zip'
    os.rename(old_file, filename)

else:
    # Download Qmlview archive for os
    os_cmd = 'gh release download --pattern "*.tar.gz"'
    os.system(os_cmd)
    print('done wit download')
    print(os.listdir(cwd))
    # extract to folder
    arch = glob.glob('*.tar.gz')
    shutil.unpack_archive(arch, extract_dir=folder_name)
    print('done wit unpack')
    print(os.listdir(folder_name))
    # copy all those contents to folder_name, skipping the existing ones
    # tar.gz file
    old_file = shutil.make_archive('Ninja_Preview', 'gztar', folder_name)
    filename = f'Ninja_Preview_{version}_{osn}.tar.gz'
    os.rename(old_file, filename)


print(f'filename: {filename}')


cmd1 = f'gh release upload {version} {filename}'
os.system(cmd1)
print('All Done')

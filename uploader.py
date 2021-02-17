import sys
import os
import tarfile
import shutil
import glob
import subprocess


version = os.environ['GITHUB_REF'].split('/')[-1]
print(f'version: {version}')

_, os_name, token = sys.argv

osn = os_name.split('-')[0]
cwd = os.path.realpath('.')

folder_name = os.path.realpath('./dist/Ninja-Preview/')
dist_folder = os.path.realpath('./dist/')

# Download Qmlview archive for os
# extract to folder
# copy all those contents to folder_name, skipping the existing ones


def change_iss():
    with open('ninja_preview_template.iss', 'r') as iss_file:
        conts = iss_file.read()
        # version number
        conts = conts.replace('{{version_number}}', version[1:])
        # curr dir
        conts = conts.replace('{{curr_dir}}', cwd)

        with open('ninja_preview_setup.iss', 'w') as iss_write:
            iss_write.write(conts)


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
    os_cmd = 'gh release download --repo'
    os_cmd += ' github.com/amoh-godwin/Qmlview --pattern "*.zip"'
    os.system(os_cmd)
    print('done with download of Qmlviews')
    # extract to folder
    arch = glob.glob('qmlview*.zip')[0]
    shutil.unpack_archive(arch, extract_dir=folder_name)
    # copy all those contents to folder_name, skip exitsting
    print('done with unpack')
    # instead of a zip make Inno setup file
    # Extract inno setup
    shutil.unpack_archive(os.path.join(cwd, 'inno.zip'))
    print('done unpacking inno setup')
    # Inno setup workings
    change_iss()
    inno_script = os.path.join(cwd, 'ninja_preview_setup.iss')
    os.chdir('inno')
    inno_cmd = f'iscc "{inno_script}"'
    out = subprocess.run(inno_cmd, capture_output=True)
    print('Inno script done changing back to directory')
    # change directory back
    os.chdir('..')

    # rename
    try:
        old_file = os.path.join(cwd, 'dist',
         f"Ninja-Preview-{version[1:]}-setup.exe")

        filename = os.path.join(cwd, 'dist',
         f'Ninja_Preview_{version}_{osn}-setup.exe')

        os.replace(old_file, filename)

    except:
        print('failed trying something else')
        print(os.listdir(dist_folder))
        old_file = os.path.join(cwd, 'dist',
         f"Ninja-Preview-{version[1:]}-setup")

        filename = os.path.join(cwd, 'dist',
         f'Ninja_Preview_{version}_{osn}-setup.exe')

        os.replace(old_file, filename)

else:
    # Download Qmlview archive for os
    os_cmd = 'gh release download --repo'
    os_cmd += ' github.com/amoh-godwin/Qmlview --pattern "*.tar.gz"'
    os.system(os_cmd)
    print('done with download of Qmlview')
    # extract to folder
    arch = glob.glob('qmlview*.tar.gz')[0]
    shutil.unpack_archive(arch, extract_dir=folder_name)
    print('done with unpack')
    # copy all those contents to folder_name, skip existing
    # tar.gz file
    old_file = shutil.make_archive('Ninja_Preview', 'gztar',
     root_dir=dist_folder, base_dir=folder_name)
    filename = os.path.join(dist_folder,
     f'Ninja_Preview_{version}_{osn}.tar.gz')
    os.replace(old_file, filename)


print(f'filename: {filename}')


cmd1 = f'gh release upload {version} {filename}'
os.system(cmd1)
print('All Done')

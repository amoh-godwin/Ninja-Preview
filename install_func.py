import os
import platform


def install_font():
    os_name = platform.system()

    if os_name == 'Windows':
        home_path = os.environ["WINDIR"]
        chk_path = os.path.join(home_path, 'Fonts')

        if os.path.exists(chk_path):
            # skip
            pass

        else:
            os.mkdir(chk_path)
            os.system('install_fonts.bat')

    else:
        # I hope this works for both Mac and Linux
        home_path = os.environ["HOME"]
        chk_path = os.path.join(home_path, '.local/share/fonts')

        if os.path.exists(chk_path):
            # skip
            pass

        else:
            os.mkdir(chk_path)
            os.system('./install_fonts.sh')

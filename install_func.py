import os

def install_font():
    home_path = os.environ["HOME"]
    chk_path = os.path.join(home_path, '.local/share/fonts')
    if os.path.exists(chk_path):
        # skip
        pass
    else:
        os.mkdir(chk_path)
        os.system('./install_fonts.sh')

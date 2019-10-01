# -*- mode: python -*-

block_cipher = None


a = Analysis(['C:\\Users\\GODWIN\\Documents\\GitHub\\Ninja-Preview\\Ninja-preview.py'],
             pathex=['C:\\Users\\GODWIN\\Documents\\GitHub\\Ninja-Preview'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Ninja-preview',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
	  icon='C:\\Users\\GODWIN\\Documents\\GitHub\\Ninja-Preview\\UI\\icons\\logo.ico' )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='Ninja-preview')

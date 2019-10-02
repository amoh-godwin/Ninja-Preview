# -*- mode: python -*-

block_cipher = None


a = Analysis(['H:\\GitHub\\Ninja-Preview\\Ninja-preview.py'],
             pathex=['H:\\GitHub\\Ninja-Preview'],
             binaries=[],
             datas=[("H:\\GitHub\\Ninja-Preview\\resource.rcc", ".")],
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
	  icon='H:\\GitHub\\Ninja-Preview-UI\\UI\\icons\\logo.ico' )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='Ninja-preview')

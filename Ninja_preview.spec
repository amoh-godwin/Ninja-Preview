# -*- mode: python ; coding: utf-8 -*-


block_cipher = None
import os


wd = os.path.realpath('.')
icon_path = os.path.join(wd, 'resources', 'icons', 'logo.ico')

print(f'wd: {wd}, icon_path: {icon_path}')


a = Analysis(['Ninja_preview.py'],
             pathex=[wd],
             binaries=[],
             datas=[(os.path.join(wd, 'UI'), '.')],
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
          name='Ninja-Preview',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          icon=icon_path,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Ninja-Preview')

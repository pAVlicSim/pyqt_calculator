# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

add_datas = [("qss_file/myStyle.qss", "qss_file"),
             ("icon_file/calculator_icon.png", "icon_file"),
             ("icon_file/favicon.ico", "icon_file"),
             ("icon_file/arithmometer_01.jpg", "icon_file")]


a = Analysis(['main_calculator.py'],
             pathex=['C:\\Users\\Pavel\\PycharmProjects\\new_calculator'],
             binaries=[],
             datas=add_datas,
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='CoolCalculator',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='icon_file/calc-icon.ico')

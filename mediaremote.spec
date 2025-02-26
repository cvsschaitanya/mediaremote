# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['src/server/app.py'],
    pathex=['src/server'],
    binaries=[],
    datas=[],
    hiddenimports=[
        'eventlet',
        'flask_socketio',
        'flask_cors',
        'pyautogui',
        'qrcode',
        'PIL',
        'pygetwindow',
        'pyscreeze',
        'pymsgbox',
        'pytweening',
        'pyperclip',
        'mouseinfo',
        'rubicon',
        'simple_websocket',
        'wsproto',
        'h11',
        'bidict',
        'engineio',
        'socketio',
        'blinker',
        'jinja2',
        'werkzeug',
        'click',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='mediaremote',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

import sys
from cx_Freeze import setup, Executable

path = sys.path
# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os", "pygame","json","sys","random" ],
                     "include_files": ["content","pictures","labyrinth.json"],
                     "excludes": ["tkinter"],
                     "path": path, "optimize": 0}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
icone = None
if sys.platform == "win32":
	base = "Win32GUI"
	icone = "icone.ico"

setup(name="McGyverEscape.exe",
      version="0.1",
      description="Mac gyver rules",
      options={"build_exe": build_exe_options},
      executables=[Executable("mainscript.py", base=base,icon=icone)]
      )
import sys
from cx_Freeze import setup, Executable

path = sys.path

packages=["os","pygame","json","sys","random"]
include_files = ["content","pictures","labyrinth.json"]
excludes=["tkinter"]
optimize = 2

build_exe_options = {"packages": packages,
                     "include_files": include_files,
                     "excludes": excludes,
                     "path": path,
                     "optimize": optimize}



base = None
icone = None
if sys.platform == "win32":
   base = "Win32GUI"
   icone = "icone.ico"



setup(name="McGyverEscape",
      version="0.1",
      description="Mac gyver rules",
      options={"build_exe": build_exe_options},
      executables=[Executable("mainscript.py", base=base,icon=icone)]
      )
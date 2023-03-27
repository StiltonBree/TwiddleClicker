import cx_Freeze, sys

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("main.py", base=base, targetName="twiddle.exe")]

cx_Freeze.setup(
    name="twiddle.exe",
    options={"build_exe": {"packages": ["pygame"], "include_files": [
        "hamrocks.png",
    ]}},
    version="1.0",
    description="Praying this works on windows",
    executables=executables
)
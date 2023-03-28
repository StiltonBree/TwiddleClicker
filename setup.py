import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name="Twiddle Clicker",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["hamrocks.png"]}},
    executables = executables

    )
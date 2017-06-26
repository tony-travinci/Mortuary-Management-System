from cx_Freeze import setup, Executable
exe = Executable(
    script=r"C:\Users\Andy\PycharmProjects\MorgueSys\mysqLogin.py",
    base="Win32GUI",
    )

setup(
    name = "TESTApp",
    version = "0.1",
    description = "An example",
    executables = [exe]
    )
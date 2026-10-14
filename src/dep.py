### Dependances dealing file

import subprocess

#Installs with subprocess the necessary modules used by the game
def install(module):
    subprocess.check_call(['pip', 'install', module])
    print(f"The module {module} has been installed")

#Try modules
def module_init():
    try:
        import pyglet
        print("Pyglet is already installed.")
    except ImportError:
        print("Pyglet is not installed")
        print("Installing Pyglet ...")
        install(pyglet)

    try:
        import numpy
        print("Numpy is already installed")
    except ImportError:
        print("Numpy is not installed")
        print("Installing Numpy ...")
        install(numpy)
    print("Good to go !")
    return 0
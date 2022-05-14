# -------------------------------------------------- #
#   Build script - Rider Japanese Translate Plugin   #
# -------------------------------------------------- #
import os
import shutil
import zipfile
import pathlib


def main():
    print("Making the library jar.")
    make_lib_jar()
    print("Making the plugin archive.")
    make_plugin_jar()
    print("Build success! Plugin archive was created in '{0}'.".format(pathlib.Path("./rider-jpn.zip").resolve()))


def make_lib_jar():
    os.chdir(os.path.dirname(__file__) + "/src/rider-jpn/lib")
    shutil.make_archive('rider-jpn', format='zip', root_dir='rider-jpn')
    if os.path.exists("rider-jpn.jar"):
        os.remove("rider-jpn.jar")
    os.rename("rider-jpn.zip", "rider-jpn.jar")
    os.chdir(os.path.dirname(__file__))


def make_plugin_jar():
    os.chdir(os.path.dirname(__file__))
    if os.path.exists("rider-jpn.zip"):
        os.remove("rider-jpn.zip")
    with zipfile.ZipFile("rider-jpn.zip", "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.write("./src/rider-jpn/lib/rider-jpn.jar", "rider-jpn/lib/rider-jpn.jar")


if __name__ == "__main__":
    main()

# -------------------------------------------------- #
#   Patch script - Rider Japanese Translate Plugin   #
# -------------------------------------------------- #
import os
import sys
import glob
import zipfile
import pathlib


def main():
    if len(sys.argv) < 2:
        print("usage: patch.py <path/to/target.zip>")
        return

    if not os.path.exists("tmp/"):
        os.makedirs("tmp/")
        
    print("Getting lib jar from '{0}' ...".format(sys.argv[1]))
    jar_path = get_lib_jar(sys.argv[1])
    print("Patching into lib jar...")
    patch_lib_jar(jar_path)
    print("Making the plugin zip file...")
    make_plugin_zip(jar_path)
    print("Cleaning...")
    clean(jar_path)
    print("Patch success! Plugin archive was created in '{0}'.".format(pathlib.Path("./rider-jpn.zip").resolve()))


def patch_lib_jar(patch_jar):
    if os.path.exists("{0}.original".format(patch_jar)):
        os.remove("{0}.original".format(patch_jar))
    os.rename(patch_jar, "{0}.original".format(patch_jar))

    with zipfile.ZipFile(patch_jar, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        # Add rider-jpn files
        for rider_msg in glob.glob("src/rider-jpn/lib/rider-jpn/messages/*"):
            msg_name = os.path.basename(rider_msg)
            zf.write(rider_msg, "messages/{0}".format(msg_name))
        for rider_msg in glob.glob("src/rider-jpn/lib/rider-jpn/META-INF/*"):
            msg_name = os.path.basename(rider_msg)
            zf.write(rider_msg, "META-INF/{0}".format(msg_name))

        # Add original translation plugin files
        with zipfile.ZipFile("{0}.original".format(patch_jar), "r", compression=zipfile.ZIP_DEFLATED) as original_zf:
            for info in original_zf.infolist():
                if not info.filename.startswith("META-INF") and not info.file_size == 0:
                    zf.writestr(info.filename, original_zf.read(info))



def get_lib_jar(name):
    jar_name = os.path.splitext(os.path.basename(name))[0]

    if os.path.exists("tmp/{0}.jar".format(jar_name)):
        os.remove("tmp/{0}.jar".format(jar_name))
    
    with zipfile.ZipFile(name, "r") as zf:
        fh = open("tmp/{0}.jar".format(jar_name), mode="wb")
        fh.write(zf.read("{0}/lib/{0}.jar".format(jar_name)))
    return "tmp/{0}.jar".format(jar_name)


def make_plugin_zip(lib_jar):
    if os.path.exists("rider-jpn.zip"):
        os.remove("rider-jpn.zip")
    with zipfile.ZipFile("rider-jpn.zip", "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.write(lib_jar, "rider-jpn/lib/rider-jpn.jar")


def clean(lib_jar_path):
    os.remove(lib_jar_path)
    os.remove(lib_jar_path + ".original")
    os.removedirs("tmp")


if __name__ == "__main__":
    main()

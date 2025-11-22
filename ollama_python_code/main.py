# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import ollama
import streamlit
import platform

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def get_ubuntu_version_platform():
    """
    Retrieves the Ubuntu version using the platform module.
    Returns a tuple (distribution_name, version, codename) if successful,
    otherwise returns None.
    """
    try:
        # platform.linux_distribution() is deprecated in Python 3.8+
        # Use platform.freedesktop_os_release() or parse /etc/os-release instead
        # For older Python versions, this might still work.
        # Alternatively, you can use platform.uname() and parse the version string.
        # This example focuses on a more robust approach for modern Python.

        # Read /etc/os-release for distribution information
        with open("/etc/os-release", "r") as f:
            os_release_info = {}
            for line in f:
                key, value = line.strip().split("=", 1)
                os_release_info[key] = value.strip('"')

        name = os_release_info.get("NAME")
        version_id = os_release_info.get("VERSION_ID")
        version_codename = os_release_info.get("VERSION_CODENAME")

        if name == "Ubuntu" and version_id and version_codename:
            return (name, version_id, version_codename)
        else:
            return None
    except FileNotFoundError:
        print("Error: /etc/os-release not found. This might not be a Linux system or the file is missing.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print(ollama.list())
    print(streamlit.__version__)

    ubuntu_info = get_ubuntu_version_platform()
    if ubuntu_info:
        print(f"Distribution: {ubuntu_info[0]}")
        print(f"Version: {ubuntu_info[1]}")
        print(f"Codename: {ubuntu_info[2]}")
else:
    print("Could not determine Ubuntu version.")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import os

def reboot_computer():
    if os.name == 'nt':  # For Windows
        os.system('shutdown /r /t 1')
    elif os.name == 'posix':  # For Linux and macOS
        os.system('sudo reboot')
    else:
        print("Unsupported operating system")

if __name__ == "__main__":
    reboot_computer()

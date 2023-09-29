import os

def restart_computer():
    if os.name == 'nt':  # For Windows
        os.system('shutdown /r /f /t 1')
    elif os.name == 'posix':  # For Linux and macOS
        os.system('sudo reboot now')
    else:
        print("Unsupported operating system")

if __name__ == "__main__":
    restart_computer()

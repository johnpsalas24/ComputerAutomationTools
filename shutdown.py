import os

def shutdown_computer():
    if os.name == 'nt':  # For Windows
        os.system('shutdown /s /f /t 1')
    elif os.name == 'posix':  # For Linux and macOS
        os.system('sudo shutdown -h now')
    else:
        print("Unsupported operating system")

if __name__ == "__main__":
    shutdown_computer()

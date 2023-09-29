import os

def reset_computer():
    if os.name == 'nt':  # For Windows
        print("Windows does not support reset operation.")
    elif os.name == 'posix':  # For Linux and macOS
        os.system('sudo systemctl isolate multi-user.target')
    else:
        print("Unsupported operating system")

if __name__ == "__main__":
    reset_computer()

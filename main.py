import sys
import os


def main():
    print("This is the main script.")
    print("\n-\n")
    print(f"Current working directory: {os.getcwd()}")
    print(f"Python version: {sys.version}")
    print("\n-\n")
    print(f"Virtual environment location: {os.path.dirname(sys.executable)}")
    print("\n-\n")
    print("Checking dependencies...\n")
    try:
        import numpy as np
        print(f"NumPy version: {np.__version__}")
    except ImportError:
        print("NumPy is not installed or wrong. Please install it to proceed.")
        sys.exit(1)
    try:
        import cv2
        print(f"OpenCV version: {cv2.__version__}")
    except ImportError:
        print("OpenCV is not installed or wrong. Please install it to proceed.")
        sys.exit(1)
    try:
        import matplotlib
        print(f"Matplotlib version: {matplotlib.__version__}")
    except ImportError:
        print("Matplotlib is not installed or wrong. Please install it to proceed.")
        sys.exit(1)
    print("\n-\n")
    print("All dependencies are installed correctly.")
    print("\n-\n")
    print("You can now run other scripts like syscheck.py or Class1/main.py to verify the setup.")


if __name__ == '__main__':
    main()

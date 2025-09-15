import sys
import os
try:
    import numpy as np
except ImportError:
    print("NumPy is not installed or wrong. Please install it to proceed.")
    sys.exit(1)
try:
    import cv2
except ImportError:
    print("OpenCV is not installed or wrong. Please install it to proceed.")
    sys.exit(1)


# write venv locationn
def where_venv():
    return os.path.dirname(sys.executable)


def write_info():
    print(f"Virtual environment location: {where_venv()}")
    print("Hello, World!")
    print(f"Current working directory: {os.getcwd()}")
    print(f"Python version: {sys.version}")
    print(f"NumPy version: {np.__version__}")
    print(f"OpenCV version: {cv2.__version__}")


def main():
    write_info()


if __name__ == '__main__':
    main()

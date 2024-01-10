import sys
import os

sys.path.insert(0, "%s/src/" % os.path.dirname(os.path.realpath(__file__)))
from src import main

if __name__ == "__main__":
    main.main()

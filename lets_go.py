
import os

import sys

os.system("sudo scutil --set ComputerName \""+sys.argv[1]+"\"")


print(sys.argv[1])


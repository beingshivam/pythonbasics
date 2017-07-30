import sys
import os

if len(sys.argv) == 1:
    print("Error, Not sufficient arguments")
    sys.exit(1)

if len(sys.argv) >= 1:
    file_name = sys.argv[1]

    if not os.path.isfile(file_name):
     with open(file_name, "w") as f:
      f.write("written file \n")
    if not os.path.isfile(file_name):
     with open(file_name, "a") as f:
      f.write("new line added")
#create TODO app

# Python program that creates 10 duplicates of the Python script itself

import os
import shutil
import sys
import glob

print("You are attacked.")

# src f
src = sys.argv[0]


# create duplicate of the file at the destination,
# with the name of "virus*"
for i in range(0, 10):
    # dest contains the path of the destination file
    dest_path = os.path.dirname(sys.argv[0])
    dest = os.path.join(dest_path, "virus"+str(i)+".py")

    path = shutil.copyfile(src,dest)

print("This is a trick !!!")

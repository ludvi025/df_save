import subprocess as sub
import os

os.chdir('data/save')
print("Downloading save...")
sub.call(["git","pull"])
input("Done. Press enter to finish...")

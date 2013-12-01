import subprocess as sub
import os
import time

os.chdir('data/save')
print("Adding all saves to staging area...")
sub.call(["git","add","*"])
print("Committing...")
sub.call(["git","commit","-m",time.ctime()])
sub.call(["git","push","origin","master"])
print("Finished")

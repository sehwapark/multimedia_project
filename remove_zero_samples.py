import os

path = '/none/sehwa/aligned-images/'
subdirs = os.listdir(path)

for subdir in subdirs:
    files = os.listdir(path+subdir)
    if len(files) == 0:
        print subdir
        os.rmdir(path+subdir)

for subdir in subdirs:
    files = os.listdir(path+subdir)
    if len(files) == 0:
        print subdir



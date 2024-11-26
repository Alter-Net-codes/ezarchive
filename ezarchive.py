import sys
import os
import platform

def zip(path):
  os.system(f'zip -r archive.zip {path}')

def tarball(path):
  os.system(f'tar -czf archive.tar.gz {path}')
  
if __name__ == "__main__":
    if len(sys.argv) > 2:
      path = sys.argv[1]
      type = sys.argv[2]
      if type == "zip":
        zip(path)
      else:
        tarball(path)
    else:
        print("Please provide a path as an argument.")

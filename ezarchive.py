import sys

def zip(path):
  #add code later

def tarball(path):
  #add code later

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

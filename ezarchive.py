import sys
import os
import argparse

def zip_archive(path):
    os.system(f'zip -r archive.zip "{path}"')

def tarball(path):
    os.system(f'tar -czf archive.tar.gz "{path}"')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create zip or tar.gz archives.")
    parser.add_argument("-C", "--path", required=True, help="Path to the directory or file to archive.")
    parser.add_argument("-t", "--type", choices=["zip", "tar"], default="zip", help="Type of archive to create. Default is zip.")
    
    args = parser.parse_args()
    
    path = args.path
    archive_type = args.type

    if not os.path.exists(path):
        print(f"Error: The path '{path}' does not exist.")
        sys.exit(1)

    if archive_type == "zip":
        zip_archive(path)
    elif archive_type == "tar":
        tarball(path)

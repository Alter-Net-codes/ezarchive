import sys
import os
import argparse
import zipfile
import tarfile
from pathlib import Path

def create_zip_archive(path, output='archive.zip'):
    path = Path(path)
    with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as zipf:
        if path.is_dir():
            for root, dirs, files in os.walk(path):
                for file in files:
                    file_path = Path(root) / file
                    # Arcname ensures the directory structure is preserved
                    arcname = file_path.relative_to(path.parent)
                    zipf.write(file_path, arcname)
        else:
            zipf.write(path, path.name)
    print(f"Created zip archive: {output}")

def create_tar_archive(path, output='archive.tar.gz'):
    path = Path(path)
    with tarfile.open(output, 'w:gz') as tar:
        tar.add(path, arcname=path.name)
    print(f"Created tar.gz archive: {output}")

def main():
    parser = argparse.ArgumentParser(description="Create zip or tar.gz archives.")
    parser.add_argument("-C", "--path", required=True, help="Path to the directory or file to archive.")
    parser.add_argument("-t", "--type", choices=["zip", "tar"], default="zip", help="Type of archive to create. Default is zip.")
    
    args = parser.parse_args()
    
    path = args.path
    archive_type = args.type

    # Resolve the absolute path
    path = Path(path).resolve()

    if not path.exists():
        print(f"Error: The path '{path}' does not exist.")
        sys.exit(1)

    try:
        if archive_type == "zip":
            create_zip_archive(path)
        elif archive_type == "tar":
            create_tar_archive(path)
    except Exception as e:
        print(f"An error occurred while creating the archive: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

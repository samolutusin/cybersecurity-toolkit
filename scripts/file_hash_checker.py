import hashlib
from pathlib import Path


def calculate_sha256(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while chunk := file.read(4096):
            sha256.update(chunk)

    return sha256.hexdigest()


file_path = input("Enter the path to a file you own: ")

path = Path(file_path)

if path.is_file():
    file_hash = calculate_sha256(path)
    print(f"SHA-256: {file_hash}")
else:
    print("File not found.")

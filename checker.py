import os
import hashlib
from marshal import load

def create_baseline():
    with open("/home/adhyan/my_integrity_checker/baseline.txt", "w") as f1:
        for root, dirs, files in os.walk("/home/adhyan/my_integrity_checker/target_files"):
            for file in files:
                path = os.path.join(root, file)
                with open(path, "rb") as f:
                    hash_obj = hashlib.sha256()
                    while True:
                        chunks = f.read(4096)
                        if not chunks:
                            break
                        hash_obj.update(chunks)
                f1.write(path + ": " + hash_obj.hexdigest() + "\n")


def check_integrity():
    old_data = {}

    with open("/home/adhyan/my_integrity_checker/baseline.txt", "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            path, hash_val = line.split(": ", 1)
            old_data[path] = hash_val

    #print(old_data)

    new_data = {}

    for root, dic, file in os.walk("/home/adhyan/my_integrity_checker/target_files"):
        for f1 in file:
            path = os.path.join(root, f1)
            with open(path, "rb") as f:
                hash_obj = hashlib.sha256()
                while True:
                    chunk = f.read(4096)
                    if not chunk:
                        break
                    hash_obj.update(chunk)
                new_data[path] = hash_obj.hexdigest()

    #print(new_data)
    changes_detected = False
    for path in old_data:

        if path in new_data:
            if old_data[path] != new_data[path]:
                print("File is modified", path)
                changes_detected = True
        elif path not in new_data:
            print("File is deleted", path)
            changes_detected = True

    for path in new_data:
        if path not in old_data:
            print("New file created", path)
            changes_detected=True

    if not changes_detected:
        print("No changes detected")


mode= input("Mode(init,check): ")

if mode=="init":
    create_baseline()
elif mode=="check":
    check_integrity()
else:
    print("Invalid input")
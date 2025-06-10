import os
import shutil
import hashlib
import time

SOURCE_DIR = "source_folder"
DEST_DIR = "destination_folder"

# Create destination folder if it doesn't exist
os.makedirs(DEST_DIR, exist_ok=True)

# Calculate the SHA256 hash of a file
def hash_file(filepath):
    hash_sha = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha.update(chunk)
    return hash_sha.hexdigest()

# Sync one file if it’s new or changed
def sync_file(src_file, dst_file):
    if not os.path.exists(dst_file):
        print(f"[NEW] Copying: {src_file} → {dst_file}")
        shutil.copy2(src_file, dst_file)
    else:
        if hash_file(src_file) != hash_file(dst_file):
            print(f"[UPDATED] Updating: {src_file} → {dst_file}")
            shutil.copy2(src_file, dst_file)

# Sync all files in the directory
def sync_directories():
    for root, dirs, files in os.walk(SOURCE_DIR):
        rel_path = os.path.relpath(root, SOURCE_DIR)
        dest_root = os.path.join(DEST_DIR, rel_path)
        os.makedirs(dest_root, exist_ok=True)

        for file in files:
            src_path = os.path.join(root, file)
            dest_path = os.path.join(dest_root, file)
            sync_file(src_path, dest_path)

# Keep syncing periodically
def run_sync(interval=5):
    print(f"📂 Watching '{SOURCE_DIR}' for changes...")
    try:
        while True:
            sync_directories()
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\n⏹️ Sync stopped by user.")

if __name__ == "__main__":
    run_sync()


"""
file_watcher_backup.py

Watches a target directory for file changes and automatically backs up
modified or newly created files to a backup directory.
"""

import time
import logging
import shutil
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Logging setup
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(message)s')

# Define paths
WATCH_DIR = Path("watched")
BACKUP_DIR = Path("backup")
BACKUP_DIR.mkdir(exist_ok=True)

class BackupHandler(FileSystemEventHandler):
    """Handles file creation/modification events by backing up the file."""

    def on_modified(self, event):
        self._backup_file(event)

    def on_created(self, event):
        self._backup_file(event)

    def _backup_file(self, event):
        if event.is_directory:
            return
        src_path = Path(event.src_path)
        dest_path = BACKUP_DIR / src_path.name
        try:
            shutil.copy2(src_path, dest_path)
            logging.info(f"Backed up: {src_path.name}")
        except Exception as e:
            logging.error(f"Failed to backup {src_path.name}: {e}")

def start_watcher():
    observer = Observer()
    event_handler = BackupHandler()
    observer.schedule(event_handler, str(WATCH_DIR), recursive=False)
    observer


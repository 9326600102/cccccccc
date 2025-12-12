import os
import subprocess
import sys

def download(url, filename, report_hook=None):
    """Download a file using wget, bypassing urlretrieve."""
    print(f"Downloading {url} to {filename}")
    result = subprocess.run(["wget", "-O", filename, url], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error downloading {url}: {result.stderr}")
        sys.exit(1)
    if report_hook:
        filesize = os.path.getsize(filename)
        report_hook(0, 1024, filesize)
        report_hook(filesize // 1024, 1024, filesize)
        report_hook(filesize // 1024, filesize % 1024, filesize)
    return filename, None

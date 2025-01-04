from pathlib import Path
from shutil import copyfile
from threading import Thread

threads = []

def copy_files(el, transfer_directory="dist"):
    ext = el.suffix[1:]
    ext_folder = Path(transfer_directory) / ext
    ext_folder.mkdir(exist_ok=True, parents=True)
    copyfile(el, ext_folder / el.name)

def start_thread(func, *args):
    th = Thread(target=func, args=args)
    th.start()
    threads.append(th)

def transfer_files(rubbish_directory="picture", transfer_directory="dist"):
    for el in Path(rubbish_directory).iterdir():
        if el.is_dir():
            start_thread(transfer_files, el, transfer_directory)
        elif el.is_file():
            start_thread(copy_files, el, transfer_directory)

transfer_files()
for thread in threads:
    thread.join()


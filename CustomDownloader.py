from tkinter import *
from tkinter import ttk
import requests
import threading

root = Tk()
root.geometry("600x200")
root.title("Downloader")
root.resizable(False, False)
l1 = Label(root, text="Custom Downloader", font="arial 18 bold")
l1.grid(row=2, column=1)
s1 = StringVar()
l2 = Label(root, text="Paste Your Link Here: ", font="arial 10")
l2.grid(row=3, column=1)
link = Entry(root, textvariable=s1, width=100, border=2)
link.grid(row=4, column=1)
progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress.grid(row=8, column=1)
b1 = Button(root, text="Download")
b1.grid(row=10, column=1)
def start_download():
    url = s1.get()
    progress["value"] = 0
    b1["state"] = "disabled"
    download_thread = threading.Thread(target=download_file, args=(url,))
    download_thread.start()

def update_progress(total_size, downloaded_size):
    progress_percentage = (downloaded_size / total_size) * 100
    progress["value"] = progress_percentage

def download_file(url):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get("content-length", 0))
    downloaded_size = 0
    with open("downloaded_file", "wb") as f:
        for data in response.iter_content(chunk_size=1024):
            f.write(data)
            downloaded_size += len(data)
            root.after(10, update_progress, total_size, downloaded_size)
            b1["state"] = "normal"
            progress["value"] = 100


root.mainloop()
import os
from datetime import datetime
folder = r"C:\Users\Public\Pictures\Sample Pictures"
location = input("Photo location: ")
files = os.listdir(folder)
for filename in files:
    if not filename.startswith("."):
        file = os.path.join(folder, filename)
        m_time = os.path.getmtime(file)
        print(str(file[-4:0]))
        real_time = datetime.fromtimestamp(m_time)
        f_time = datetime.strftime(real_time, "%y%B%d_%H%M%S")
        num = int(files.index(filename))+ 1
        new_filename = num + f_time + "_" + location + file[-4:]
        new_file = os.path.join(folder, new_filename)
        os.rename(file, new_file)
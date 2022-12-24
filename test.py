import glob
import os

files = glob.glob('./images/*')
latest_file = max(files, key=os.path.getctime)

print(latest_file)
print(os.path.basename(latest_file))
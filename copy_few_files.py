# Copy few files using Shutil

import shutil
import os

filenames_to_copy = ['01042023.txt', '02042023.txt', '03042023.txt']

for file in filenames_to_copy:
    source = os.path.join('Data', file)
    destination = os.path.join('copy_few_files', file)
    shutil.copyfile(source, destination)


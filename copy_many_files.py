# Copy multiple files using REGEX and Shutil
# Scenario : Lets copy all files of August

import shutil
import re
import os

pattern = r'\d\d08\d+'
source_directory = 'data'
destination = os.path.join('copy_many_files')

for file in os.listdir(source_directory):
    if re.match(pattern, file):
        shutil.copyfile(os.path.join(source_directory, file), os.path.join(destination, file))



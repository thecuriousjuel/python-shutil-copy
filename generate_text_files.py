from datetime import datetime
from datetime import timedelta
import os

now = datetime.now()

for i in range(300):
    now.strftime('%d%m%Y')
    now += timedelta(days=1)
    date = now.strftime('%d%m%Y')
    filename = date + '.txt'
    with open(os.path.join('data', filename), mode='w') as fp:
        fp.write(f'This is file {filename}')

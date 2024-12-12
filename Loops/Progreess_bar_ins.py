# pip install --upgrade progressbar --user
import time
import time
import progressbar
bar = progressbar.ProgressBar()
print(bar)

for i in bar(range(50)):
    time.sleep(2)
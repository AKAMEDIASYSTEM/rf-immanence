#!/usr/bin/env python
import time
from subprocess import call

ts = time.strftime("%Y-%m-%dt%H%M") # for filename
command = 'rtl_power -f 420M:500M:5k -i 1s -e 10m '+ts+'.csv'
call(command.split(), shell=False)
command2 = 'python heatmap.py '+ts+'.csv '+ts+'.png'
call(command2.split(),shell=False)

command3 = 'cp '+ts+'.png /media/usb0/rf-scans/'
call(command3.split(),shell=False)
# also duplicate so that the latest image is updated
command4 = 'mv '+ts+'.png /media/usb0/rf-scans/latest.png'

print 'done with %s' % ts

'''
formulate filename from datetime
make sure rtl_power is over
cause rtl_power to be run

also, make rtl_power results into a json object?
also, cp the json over into a www directory, so it can be served locally?

service: restart script 5 seconds after termination and 100 seconds after boot




to symlink the .service and .target files, go to /etc/systemd/system/ and then
ln -s ~/rf-immanence/scripts/rf.timer rf.timer
ln -s ~/rf-immanence/scripts/rf.service rf.service
...now git pull should update the active service files


'''
#!/usr/bin/env python
import time
from subprocess import call

ts = time.strftime("%Y-%m-%dt%H%M") # for filename
command = 'rtl_power -f 420M:500M:5k -i 1s -e 1h '+ts+'.csv'
call(command.split(), shell=False)
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
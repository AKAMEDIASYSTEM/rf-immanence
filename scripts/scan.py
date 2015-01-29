#!/usr/bin/env python
import time

ts = time.strftime("%Y%m%d-%H%M%S")


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
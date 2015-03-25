#!/usr/bin/env python
import time
from subprocess import call
from subprocess import check_output

ts = time.strftime("%Y-%m-%dt%H%M") # for filename
command = 'rtl_power -f 42M:1300M:5k -i 5s'
print 'issuing command'
d = check_output(command.split(), shell=False)
d = d.split('\n')
for g in d:
    print 'now i see %s' % g
# generate heatmap from output
# command2 = 'python ~/rtl-sdr-misc/heatmap/heatmap.py '+ts+'.csv '+ts+'.png'
# call(command2.split(),shell=False)

# command3 = 'cp '+ts+'.png /media/usb0/rf-scans/'
# call(command3.split(),shell=False)
# also duplicate so that the latest image is updated
# command4 = 'mv '+ts+'.png /media/usb0/rf-scans/latest.png'
# call(command4.split(),shell=False)
# print 'done with %s' % ts


'''
from rtl_power docs
-f lower:upper:bin_size [Hz]
Set a frequency range. Values can be specified as an integer (89100000), a float (89.1e6) or as a metric suffix (89.1M). The bin size may be adjusted to make the math easier. Valid bin sizes are between 0.1Hz and 2.8MHz. Ranges may be any size.

-i <integration_interval>
Collect data for this amount of time, report it and repeat. Supports 's/m/h' as a units suffix. Default is 10 seconds. Minimum time is 1 second, but for extremely large ranges it may take more than 1 second to perform the entire sweep. Undefined behavior there.

-e <exit_timer>
Run for at least this length of time and exit. Default is forever. Like the other times, this supports 's/m/h' units.

-1
Enable single-shot mode, default disabled. Perform a single integration interval, report and exit. It is not necessary to use -e with this option.

-d <index>
When using multiple dongles, this indicated which. You can also identify dongles by the text in the serial number field of the EEPROM.

-g <gain>
A floating point gain value. The dongle will use the closest gain setting available.

-p <error>
Correct for the parts-per-million error in the crystal. This will override a ppm value retrieved from eeprom.

-w <window>
The window is a shaping function applied to the data before the FFT. Each will emphasize or deemphasize certain aspects. The default is none (aka boxcar, rectangular). Options include: hamming, blackman, blackman-harris, hann-poisson, bartlett, and youssef.

-c <crop_percent>
The crop sets how much of the bandwidth should be discarded. 0% discards nothing, 100% discards everything. 
The edges of the spectrum are lower quality than the middle. 
There is less sensitivity, gain roll-off and out-of-band aliasing. 
Higher values of crop will produce a better spectrum, but do so more slowly. 
Values may be a decimal (-c 0.1) or a percent (-c 10%). Default crop is 0%, suggested crop is between 20% and 50%.
This setting has no effect on bins larger than 1MHz.

-F 0 | 9
Not exactly the best named option, this configures the downsampler and the downsample filters.
Downsampling is only used when the total bandwidth range is under 1MHz. (Like in the radar example above.)
Omitting the -F option uses the default downsampler, rectangular.
This downsampler is very fast but has bad spectral leakage.

Filters with minimal leakage are -F 0 and -F 9. 0 is a plain filter, but has bad droop at the edges of the spectrum. 9 uses the same filter as 0, but has a 9-point FIR filter to correct the droop. Rectangular needs the least cpu, 0 needs more, and 9 most of all. It is suggested to use 0 with -c 50%.

-P
Enables peak hold. The default behavior is to average across time. Peak hold uses the maximum value across time. Note that averaging improves the SNR, and peak hold will tend to make a spectrum look much worse.

-D
Enable direct sampling. Requires that you have first modified the dongle for direct sampling.

-O
Enable offset tuning. Only applies to E4000 tuners.

Output Format
Rtl_power produces a compact CSV file with minimal redundancy. The columns are:
date, time, Hz low, Hz high, Hz step, samples, dB, dB, dB, ...
Date and time apply across the entire row. The exact frequency of a dB value can be found by (hz_low + N * hz_step).
The samples column indicated how many points went into each average.
'''
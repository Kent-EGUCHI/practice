import statistics
import math
import numpy

#with open('/home/eguchi/ownCloud/Documents/raspberrypi/time_readadc_spidev',) as rf:
#    t = rf.readlines()
t = numpy.loadtxt('/home/eguchi/ownCloud/Documents/raspberrypi/time_readadc_spidev')
with open('/home/eguchi/ownCloud/Documents/raspberrypi/avg_std_readadc_spidev', mode = 'w') as wf:
    print("avg",statistics.mean(t),file=wf)
    print("stdev",statistics.stdev(t),file=wf)
    print("var",math.sqrt(numpy.var(t,ddof=1)),file=wf)


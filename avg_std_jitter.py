import statistics
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
#import japanize_matplotlib
from matplotlib.ticker import ScalarFormatter

from matplotlib import font_manager

#font_manager.fontManager.addfont("/home/eguchi/.fonts/ipaexg.ttf")
#matplotlib.rc('font', family="IPAGothic")

#matplotlib.use('Agg')

import seaborn as sns
# グラフの設定
sns.set(
    context='talk',  # スライドに合ったフォントサイズ・線幅
    style='white',  # 背景白，グリッドなし
    palette='plasma',  # あらきお気に入りのカラースキーム
    font='sans-serif',  # フォント指定
    font_scale=1,  # フォントスケール指定（これを変えるとcontextで決まるプリセットを更にいじれる）
    #rc={'text.usetex': True}  # LaTeX書式を使えるように
)

jitter = []
interval = 0.00005
sample = 100000
width = 0.1
bin_num = 100
y_limit = 10000

#with open('/home/eguchi/ownCloud/Documents/raspberrypi/time_readadc_spidev',) as rf:
#    t = rf.readlines()
t = np.loadtxt('/home/eguchi/ownCloud/Documents/raspberrypi/adc_photor/spidev_output_interval='+str(interval)+'s_sample='+str(sample))
#t = np.loadtxt('E:/owncloud/Documents/raspberrypi/adc_photor/spidev_output_interval='+str(interval)+'s_sample='+str(sample))
#with open('/home/eguchi/ownCloud/Documents/raspberrypi/time_vs_bit/spidev_output_interval_0.0005.txt', mode = 'w') as wf:
#    print("avg",statistics.mean(t),file=wf)
#    print("stdev",statistics.stdev(t),file=wf)
#    print("var",math.sqrt(numpy.var(t,ddof=1)),file=wf)

#print(np.shape(t)[0])
for i in range(np.shape(t)[0]-1):
    jitter.append(t[i+1][0]-t[i][0])

for i in range(np.shape(jitter)[0]):
    jitter[i] = jitter[i] - interval

with open('/home/eguchi/ownCloud/Documents/raspberrypi/time_vs_bit/std_avg_spidev_output_interval_'+str(interval), mode = 'w') as wf:
#with open('E:/owncloud/Documents/raspberrypi/adc_photor_jitter/jitter_std_avg_interval_'+str(interval), mode = 'w') as wf:
    print("interval",'{:e}'.format(interval),file=wf)
    print("jitter_avg",statistics.mean(jitter),file=wf)
    print("stdev_sample",statistics.stdev(jitter),file=wf)
    print("stdev_unbiased",math.sqrt(np.var(jitter,ddof=1)),file=wf)
    print("max of jitter", max(jitter),file = wf)
    print("min of jitter", min(jitter),file = wf)
    print("median of jitter",statistics.median(jitter), file= wf )

fig, ax = plt.subplots(figsize = (9,6)) #アスペクト比
ax.xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax.set_xlabel("jitter (s)")

ax.ticklabel_format(  # 指数表記
    style="sci",
    scilimits=(0, 0),
    axis="x"
)
ma = max(jitter)
mi = min(jitter)
#print(ma)

#ax.set_ylim(0,y_limit)

ax = plt.hist(
    jitter,
    bins=bin_num,
    range=(-1*width,width),
    #range=(mi,ma),
)


#plt.savefig('E:/owncloud/Documents/raspberrypi/adc_photor/jitter_hist_interval='+str(interval)+'s_sample='+str(sample)+'.png')
#plt.savefig('E:/owncloud/Documents/raspberrypi/figure/jitter_hist_interval='+str(interval)+'s_sample='+str(sample)+'width='+str(width)+'.png')
plt.savefig('/home/eguchi/ownCloud/Documents/raspberrypi/figure/jitter_hist_interval='+str(interval)+'s_sample='+str(sample)+'width='+str(width)+'.png')
#plt.savefig('E:/owncloud/Documents/raspberrypi/adc_photor_jitter/jitter_wide_hist_interval='+str(interval)+'s_sample='+str(sample)+'.png')
#plt.hist(sample_rate)

plt.show()

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

matplotlib.use('Agg')

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
interval = 0.0005
sample = 100000

#with open('/home/eguchi/ownCloud/Documents/raspberrypi/time_readadc_spidev',) as rf:
#    t = rf.readlines()
#t = np.loadtxt('/home/eguchi/ownCloud/Documents/raspberrypi/time_vs_bit/spidev_output_interval_'+str(interval)+'.txt')
t = np.loadtxt('E:/owncloud/Documents/raspberrypi/adc_photor/jitter_output_interval='+str(interval)+'s_sample='+str(sample))
#with open('/home/eguchi/ownCloud/Documents/raspberrypi/time_vs_bit/spidev_output_interval_0.0005.txt', mode = 'w') as wf:
#    print("avg",statistics.mean(t),file=wf)
#    print("stdev",statistics.stdev(t),file=wf)
#    print("var",math.sqrt(numpy.var(t,ddof=1)),file=wf)

#print(np.shape(t)[0])
for i in range(np.shape(t)[0]):
    jitter.append(t[i][0]-t[i-1][0])

jitter = jitter - interval

#with open('/home/eguchi/ownCloud/Documents/raspberrypi/time_vs_bit/std_avg_spidev_output_interval_'+str(interval), mode = 'w') as wf:
with open('E:/owncloud/Documents/raspberrypi/adc_photor/jitter_std_avg_interval_'+str(interval), mode = 'w') as wf:
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

plt.text(2.0,3.0,'(a)')

ax.ticklabel_format(  # 指数表記
    style="sci",
    scilimits=(0, 0),
    axis="x"
)
#ma = max(jitter)
#print(ma)

ax.set_ylim(0,6000)

ax = plt.hist(
    jitter,
    bins=100,
    range=(0,0.00001),
    #range=(0,ma),
)


#plt.savefig('E:/owncloud/Documents/raspberrypi/adc_photor/jitter_hist_interval='+str(interval)+'s_sample='+str(sample)+'.png')
plt.savefig('E:/owncloud/Documents/raspberrypi/adc_photor/jitter_hist_interval='+str(interval)+'s_sample='+str(sample)+'.png')
#plt.hist(sample_rate)

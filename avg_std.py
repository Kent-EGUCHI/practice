import statistics
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
#import japanize_matplotlib
from matplotlib.ticker import ScalarFormatter

from matplotlib import font_manager

font_manager.fontManager.addfont("/home/eguchi/.fonts/ipaexg.ttf")
matplotlib.rc('font', family="IPAGothic")

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

delta_t = []
sample_rate = []
interval = 0.001

#with open('/home/eguchi/ownCloud/Documents/raspberrypi/time_readadc_spidev',) as rf:
#    t = rf.readlines()
t = np.loadtxt('/home/eguchi/ownCloud/Documents/raspberrypi/time_vs_bit/spidev_output_interval_'+str(interval)+'.txt')
#with open('/home/eguchi/ownCloud/Documents/raspberrypi/time_vs_bit/spidev_output_interval_0.0005.txt', mode = 'w') as wf:
#    print("avg",statistics.mean(t),file=wf)
#    print("stdev",statistics.stdev(t),file=wf)
#    print("var",math.sqrt(numpy.var(t,ddof=1)),file=wf)

print(np.shape(t)[0])

for i in range(np.shape(t)[0]):
    delta_t.append(t[i][0]-interval*(i+1))
for i in range(np.shape(t)[0]):
    sample_rate.append(t[i][0]-t[i-1][0])

with open('/home/eguchi/ownCloud/Documents/raspberrypi/time_vs_bit/std_avg_spidev_output_interval_'+str(interval), mode = 'w') as wf:
    print("interval",'{:e}'.format(interval),file=wf)
    print("jitter_avg",statistics.mean(delta_t),file=wf)
    print("stdev_sample",statistics.stdev(delta_t),file=wf)
    print("stdev_unbiased",math.sqrt(np.var(delta_t,ddof=1)),file=wf)

fig, ax = plt.subplots(figsize = (9,6)) #アスペクト比 
ax.xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax.set_xlabel("サンプリング周期")
ax.ticklabel_format(  # 指数表記
    style="sci",
    scilimits=(0, 0),
    axis="x"
)
ax = plt.hist(
    delta_t,
    bins=200,
    range=(0,0.0002),
)


plt.savefig("test.png") 
#plt.hist(sample_rate)

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

interval = 0.0005
sample = 100000
wave = 'sq'
duration = 0.1
freq = 2500

zoom = 5
x = []
y = []



t = np.loadtxt('E:/owncloud/Documents/raspberrypi/adc_pwm/spidev_output_interval='+str(interval)+'s_duration='+str(duration)+'s_wave='+wave+'_freq='+str(freq)+'Hz')

for i in range(int(np.shape(t)[0]/zoom)):
    x.append(t[i][0])
    y.append(t[i][1])

fig, ax = plt.subplots(figsize = (9,6)) #アスペクト比
ax.xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax.set_xlabel("time (s)")
ax.set_ylabel("voltage (3.3/4096 v)")

ax.plot(x,y,linewidth = 0.5)
plt.savefig('E:/owncloud/Documents/raspberrypi/adc_pwm/wave_interval='+str(interval)+'s_duration='+str(duration)+'s_wave='+wave+'_freq='+str(freq)+'Hz.png')

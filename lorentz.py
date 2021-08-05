import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from seaborn.palettes import color_palette

sns.set(
    context='talk',  # スライドに合ったフォントサイズ・線幅
    style='ticks',  # 背景白，グリッドなし 軸目盛りあり
    palette='plasma',  # あらきお気に入りのカラースキーム
    font='cm',#'sans-serif',  # フォント指定
    font_scale=1,  # フォントスケール指定（これを変えるとcontextで決まるプリセットを更にいじれる）
    rc={'text.usetex': False}  # LaTeX書式を使えるように
)

transparency = 0.5


fig = plt.figure(figsize = (10.0,10.0))
ax = fig.add_subplot(111,projection='3d')


b = 8/3
r = 30
sigma = 10

dt = 0.01
nt = 10000

x = np.zeros(nt+1)
y = np.zeros(nt+1)
z = np.zeros(nt+1)

x[0] = 10
y[0] = 20
z[0] = -30

for n in range(nt):
    x[n+1] = x[n] + (-sigma*x[n]+sigma*y[n])*dt
    y[n+1] = y[n] + (-x[n]*z[n]+r*x[n]-y[n])*dt
    z[n+1] = z[n] + (x[n]*y[n]-b*z[n])*dt

ax.plot(
    x,y,z,
    color = 'black',
    linestyle = 'solid',
    linewidth = '1',
    marker = ' ',
    alpha = transparency
    )

ax.plot(
    x[0],y[0],z[0],
    color = 'white',
    marker = 'o',
    markeredgecolor = 'black',
    alpha = transparency
    )

#-----------------------------------------------------------------------
x = np.zeros(nt+1)
y = np.zeros(nt+1)
z = np.zeros(nt+1)
#-----------------------------------------------------------------------
x[0] = 30
y[0] = 20
z[0] = 10

for n in range(nt):
    x[n+1] = x[n] + (-sigma*x[n]+sigma*y[n])*dt
    y[n+1] = y[n] + (-x[n]*z[n]+r*x[n]-y[n])*dt
    z[n+1] = z[n] + (x[n]*y[n]-b*z[n])*dt

ax.plot(
    x,y,z,
    color = 'blue',
    linestyle = 'solid',
    linewidth = '1',
    marker = ' ',
    alpha = transparency
    )

ax.plot(
    x[0],y[0],z[0],
    color = 'white',
    marker = 'o',
    markeredgecolor = 'blue',
    alpha = transparency
    )

plt.show()
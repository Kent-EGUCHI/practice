import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from seaborn.palettes import color_palette

sns.set(
    context='talk',  # スライドに合ったフォントサイズ・線幅
    style='ticks',  # 背景白，グリッドなし 軸目盛りあり
    palette='plasma',  # あらきお気に入りのカラースキーム
    font='sans-serif',  # フォント指定
    font_scale=1,  # フォントスケール指定（これを変えるとcontextで決まるプリセットを更にいじれる）
    rc={'text.usetex': True}  # LaTeX書式を使えるように
)

transparency = 1.0
color = ['black','blue','blue']

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
z[0] = 100

for n in range(nt):
    x[n+1] = x[n] + (-sigma*x[n]+sigma*y[n])*dt
    y[n+1] = y[n] + (-x[n]*z[n]+r*x[n]-y[n])*dt
    z[n+1] = z[n] + (x[n]*y[n]-b*z[n])*dt

ax.plot(
    x,y,z,
    color = color[0],
    linestyle = 'solid',
    linewidth = '1',
    marker = ' ',
    alpha = transparency
    )

ax.plot(
    x[0],y[0],z[0],
    color = 'white',
    marker = 'o',
    markeredgecolor = color[0],
    alpha = transparency
    )
ax.text(x[0], y[0],z[0], r'$({x}, {y},{z})$'.format(x=x[0], y=y[0],z=z[0]))

ax.grid(False)
ax.set_xlabel(r"$X$")
ax.set_ylabel(r"$Y$")
ax.set_zlabel(r"$Z$")

#-----------------------------------------------------------------------
x2 = np.zeros(nt+1)
y2 = np.zeros(nt+1)
z2 = np.zeros(nt+1)
#-----------------------------------------------------------------------
x2[0] = -10
y2[0] = -20
z2[0] = -10

for n in range(nt):
    x2[n+1] = x2[n] + (-sigma*x2[n]+sigma*y2[n])*dt
    y2[n+1] = y2[n] + (-x2[n]*z2[n]+r*x2[n]-y2[n])*dt
    z2[n+1] = z2[n] + (x2[n]*y2[n]-b*z2[n])*dt

ax.plot(
    x2,y2,z2,
    color = color[1],
    linestyle = 'solid',
    linewidth = '1',
    marker = ' ',
    alpha = transparency
    )

ax.plot(
    x2[0],y2[0],z2[0],
    color = 'white',
    marker = 'o',
    markeredgecolor = color[1],
    alpha = transparency
    )
ax.text(x2[0], y2[0],z2[0], r'$({x}, {y},{z})$'.format(x=x2[0], y=y2[0],z=z2[0]))

plt.tight_layout()
plt.savefig('/mnt/j/onedrive_ou/OneDrive - Osaka University/Ⅰセメ/非線形力学特論/fig_lorentz.png')
plt.show()

fig = plt.figure(figsize = (10.0,10.0))
ax2 = fig.add_subplot(111)

r = np.zeros(nt+1)

tau = np.zeros(nt+1)

for n in range(nt+1):
    r[n] = np.sqrt((x[n]-x2[n])**2+(y[n]-y2[n])**2+(z[n]-z2[n])**2)
    tau[n] = n*dt

ax2.plot(
    tau,r,
    color = color[2],
    linestyle = 'solid',
    linewidth = '1',
    marker = '',
    alpha = transparency
    )

ax2.set_yscale('log')

#plt.show()
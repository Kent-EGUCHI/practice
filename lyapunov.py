import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from seaborn.palettes import color_palette

sns.set(
    context='talk',  # スライドに合ったフォントサイズ・線幅
    style='ticks',  # 背景白，グリッドなし 軸目盛りあり
    palette='plasma',  # あらきお気に入りのカラースキーム
    font='sans-serif',  # フォント指定
    font_scale=2,  # フォントスケール指定（これを変えるとcontextで決まるプリセットを更にいじれる）
    rc={'text.usetex': True}  # LaTeX書式を使えるように
)

transparency = 1.0
color = ['black','blue','blue']

fig = plt.figure(figsize = (10.0,8.0))
ax = fig.add_subplot(111)



b = 8/3
r = 30
sigma = 10

dt = 0.01
nt = 10000
dd = 0.00001

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

#-----------------------------------------------------------------------
x2 = np.zeros(nt+1)
y2 = np.zeros(nt+1)
z2 = np.zeros(nt+1)
#-----------------------------------------------------------------------
x2[0] = 10
y2[0] = 20+dd
z2[0] = 100

for n in range(nt):
    x2[n+1] = x2[n] + (-sigma*x2[n]+sigma*y2[n])*dt
    y2[n+1] = y2[n] + (-x2[n]*z2[n]+r*x2[n]-y2[n])*dt
    z2[n+1] = z2[n] + (x2[n]*y2[n]-b*z2[n])*dt


#-----------------------------------------------------------------------
x3 = np.zeros(nt+1)
y3 = np.zeros(nt+1)
z3 = np.zeros(nt+1)
#-----------------------------------------------------------------------
dx = x[1]-x[0]
dy = y[1]-y[0]
dz = z[1]-z[0]
dr = np.sqrt(dx**2+dy**2+dz**2)
dx = dx/dr
dy = dy/dr
dz = dz/dr


x3[0] = x[0] + dd*dx
y3[0] = y[0] + dd*dy
z3[0] = z[0] + dd*dz

x3[0] = x[0] + (-sigma*x2[0]+sigma*y2[0])*dt*dd
y3[0] = y[0] + (-x2[0]*z2[0]+r*x2[n]-y2[0])*dt*dd
z3[0] = z[0] + (x2[0]*y2[0]-b*z2[0])*dt*dd

for n in range(nt):
    x3[n+1] = x3[n] + (-sigma*x3[n]+sigma*y3[n])*dt
    y3[n+1] = y3[n] + (-x3[n]*z3[n]+r*x3[n]-y3[n])*dt
    z3[n+1] = z3[n] + (x3[n]*y3[n]-b*z3[n])*dt



r = np.zeros(nt+1)

tau = np.zeros(nt+1)

for n in range(nt+1):
    r[n] = np.sqrt((x[n]-x2[n])**2+(y[n]-y2[n])**2+(z[n]-z2[n])**2)
    tau[n] = n*dt

ax.plot(
    tau,r,
    color = color[0],
    linestyle = 'solid',
    linewidth = '1',
    marker = '',
    alpha = transparency
    )
ax.plot(
    tau[0],r[0],
    color = 'white',
    marker = 'o',
    markeredgecolor = 'blue',
    alpha = transparency
    )

for n in range(nt+1):
    r[n] = np.sqrt((x[n]-x3[n])**2+(y[n]-y3[n])**2+(z[n]-z3[n])**2)
    tau[n] = n*dt
    if(n==0):
        print(r[0])

print(x[0],y[0],z[0])
print(x[1],y[1],z[1])
print(x3[0],y3[0],z3[0])

ax.set_xlabel(r"$t$")
ax.set_ylabel(r"$\Delta(t)$")

# ax.plot(
#     tau,r,
#     color = color[1],
#     linestyle = 'solid',
#     linewidth = '1',
#     marker = '',
#     alpha = transparency
#     )

ax.set_yscale('log')

plt.tight_layout()
plt.savefig('/mnt/j/onedrive_ou/OneDrive - Osaka University/Ⅰセメ/非線形力学特論/fig_lyapunov.png')
plt.show()
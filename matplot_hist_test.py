import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg') # この行を追記

x = np.random.normal(50, 10, 1000)
plt.hist(x, bins=50)

plt.savefig("hoge.png") # この行を追記
import numpy as np
import matplotlib.pyplot as plt

x= np.arange(0,100)
y = x*2
z = x**2

# fig = plt.figure()
# ax1 = fig.add_axes([0,0,1,1])
# ax1.plot(x,z)
# ax1.plot(x,y)
# ax1.set(xlabel='xlabel',ylabel='ylabel',title='title')

# ax.set_title('Plot title')
# plt.show()

# ax2 = fig.add_axes([0.2,0.5,0.2,0.2])
# ax2.plot(x,y)
# ax2.set_xlim(20,100)
# ax1.set(xlabel='xlabel',ylabel='ylabel')
# plt.show()

fig ,ax = plt.subplots(nrows=1, ncols=2)
ax[0].plot(x,y,linewidth=2,linestyle="-.",label="x-y")
ax[1].plot(x,z,linewidth=2,linestyle="--",label="x-z",color="red")
plt.legend()
plt.tight_layout()
plt.show()
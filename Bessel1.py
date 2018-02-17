import numpy as np
import matplotlib.pyplot as plt
import scipy.special.cython_special

x=np.linspace(0.,20.,1000)
fig,ax=plt.subplots()
ax.plot(x,scipy.special.jn(0,x),color='black',label='0')
ax.plot(x,scipy.special.jn(1,x),color='yellow',label='1')
ax.plot(x,scipy.special.jn(2,x),color='green',label='2')
ax.plot(x,scipy.special.jn(3,x),color='red',label='3')
ax.plot(x,scipy.special.jn(4,x),color='blue',label='4')
ax.legend(loc='upper right')
plt.show()

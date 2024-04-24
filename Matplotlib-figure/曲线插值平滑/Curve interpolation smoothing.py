import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import make_interp_spline

Size = 30
x = np.arange(Size)
y = np.random.randint(1, Size, Size)

#平滑前
plt.plot(x, y,'r')
plt.show()

#平滑处理后
x_smooth = np.linspace(x.min(), x.max(), 500)  # np.linspace 等差数列,从x.min()到x.max()生成300个数，便于后续插值
y_smooth = make_interp_spline(x, y)(x_smooth)
plt.plot(x_smooth, y_smooth,'b')
plt.show()



'''
    The reference materials:
    https://blog.csdn.net/m0_51233386/article/details/129875772
'''
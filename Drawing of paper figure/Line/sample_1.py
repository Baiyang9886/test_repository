import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''
1. 保存文件 np.savetxt('src.csv', src, fmt='%f', delimiter='  ', newline='\n')
2. xls文件编码格式要求utf-8，Windows默认为gbk
'''


def plot_1(path_to_save, src, prediction, sampled_src):

    idx_scr = [i for i in range(len(src))]
    # index shift 1 for compare prediction and real of next day
    idx_pred = [i for i in range(1, len(prediction) + 1)]
    idx_sampled_src = [i for i in range(len(sampled_src))]

    plt.figure(figsize=(15, 6))
    # 参数设置参考文档：https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams
    plt.rcParams["font.size"] = 18
    # plt.rcParams['font.family'] = 'Times New Roman'

    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html?highlight=grid#matplotlib.pyplot.grid
    plt.grid(visible=True, which='major', linestyle='-')
    plt.grid(visible=True, which='minor', linestyle='--', alpha=0.5)
    plt.minorticks_on()

    # REMOVE DROPOUT FOR THIS PLOT TO APPEAR AS EXPECTED !!
    # DROPOUT INTERFERES WITH HOW THE SAMPLED SOURCES ARE PLOTTED
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html?highlight=plot#matplotlib.pyplot.plot
    plt.plot(idx_sampled_src, sampled_src, 'o-.', color='red', label='sampled source', linewidth=1, markersize=10)
    plt.plot(idx_scr, src, 'o-.', color='blue', label='input sequence', linewidth=1)
    plt.plot(idx_pred, prediction, 'o-.', color='limegreen', label='prediction sequence', linewidth=1)
    # o-  o--
    plt.title("Teaching Forcing from Sensor 32 Epoch 200")
    plt.xlabel("Time Elapsed")
    plt.ylabel("Humidity (%)")
    plt.legend()    # loc=1 upper right
    plt.savefig(path_to_save + f"/Epoch_200.png")
    plt.close()


if __name__ == "__main__":
    path_to_save = "output"
    # 读取文件中所有数据，注意CSV文件是
    data = pd.read_csv("res.csv")
    src, prediction, sampled_src = data.iloc[:, 0], data.iloc[1:, 1], data.iloc[:, 2]
    plot_1(path_to_save, src, prediction, sampled_src)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''
1. plot可接受的输入类型？Series、Array、List
2. 背景、线条、颜色、图例、字体
'''


def EMA(values, alpha=0.1):
    ema_values = [values[0]]
    for idx, item in enumerate(values[1:]):
        ema_values.append(alpha * item + (1 - alpha) * ema_values[idx])
    return ema_values


def plot_2(path_to_save):
    plt.rcParams.update({'font.size': 10})
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    with open("./train_loss.txt", 'r') as f:
        loss_list = [float(line) for line in f.readlines()]
    EMA_loss = EMA(loss_list)
    # plot color: 'b', 'g', 'r', "purple"
    l1, = plt.plot(range(len(loss_list[::10])), loss_list[::10], 'o', label="loss", markersize=5, c='green', linestyle='dashed')
    l2, = plt.plot(range(len(loss_list[::10])), EMA_loss[::10], 'o-', markersize=5, label="EMA loss", c='red')
    plt.xlabel("Epochs")
    plt.ylabel("Loss")
    #  setting legend
    from matplotlib.legend_handler import HandlerLine2D
    plt.legend(prop={'family': 'Times New Roman', 'size': 12},
               handlelength=3,
               handler_map={l1: HandlerLine2D(numpoints=2), l2: HandlerLine2D(numpoints=2)},
               handles=[l1, l2], labels=['loss-1', 'loss-2'], loc=1, frameon=False)
    plt.title("Training Loss of Transformer")
    plt.savefig(path_to_save + f"/training_loss_solve.png")
    plt.close()


if __name__ == "__main__":
    path_to_save = "output"
    plot_2(path_to_save)
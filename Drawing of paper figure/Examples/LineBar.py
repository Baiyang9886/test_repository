import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np

myfont7 = FontProperties(size=14)
myfont8 = FontProperties(size=12)

def draw_figure_7():
    fig, ax1 = plt.subplots(1, 1, figsize=(6, 4))
    PD_BERT = [0.296, 0.309, 0.316, 0.324, 0.328, 0.329, 0.332, 0.335, 0.337, 0.340]
    PTinyBERT = [0.277, 0.289, 0.301, 0.307, 0.317, 0.318, 0.324, 0.327, 0.332, 0.334]
    Unique = [539264, 957589, 1321446, 1660668, 1989253, 2312669, 2633543, 2953503, 3272902, 3592060]
    Unique_norm = [x / 1000000 for x in Unique]

    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    x_value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    x_label = ["0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1.0"]
    ax1.plot(x, PD_BERT, 'o-', label="PD-BERT")
    ax1.plot(x, PTinyBERT, '^-', label="STinyBERT+Pairwise")
    ax1.set_ylim(0.26, 0.36)
    ax1.set_xticks(x_value)
    ax1.set_xticklabels(x_label, fontproperties=myfont7)
    for label in ax1.get_xticklabels():
        label.set_fontproperties(myfont7)
    for label in ax1.get_yticklabels():
        label.set_fontproperties(myfont7)
    ax1.set_ylabel('MRR@10', fontproperties=myfont7)
    ax1.set_xlabel('Training Data Amount (Ratio)', fontproperties=myfont7)
    ax1.legend(prop=myfont8, loc="center", bbox_to_anchor=(0.5, 0.92), ncol=3)
    ax1.grid(alpha=0.3, linestyle='--')

    ax2 = ax1.twinx()
    ax2.bar(x, Unique_norm, width=0.6, edgecolor='w', hatch="//", color="forestgreen", alpha=.8)
    ax2.set_ylim(0, 5)
    for label in ax2.get_yticklabels():
        label.set_fontproperties(myfont7)
    ax2.set_ylabel("# Positive Samples (M)", fontproperties=myfont7)

    plt.tight_layout()
    plt.savefig("output/figure7.png")


draw_figure_7()
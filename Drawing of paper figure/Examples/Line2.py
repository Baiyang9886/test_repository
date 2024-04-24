import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np

myfont3 = FontProperties(fname='./LinLibertine_R.ttf', size=22)
myfont4 = FontProperties(fname='./LinLibertine_R.ttf', size=26)


def draw_figure_4():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    x = [0.2, 0.4, 0.6, 0.8, 1]
    map = [0.5458, 0.5469, 0.5468, 0.5496, 0.5500]
    ndcg3 = [0.5429, 0.5433, 0.5441, 0.5475, 0.5478]
    nocl_map = [0.5341, 0.5341, 0.5341, 0.5341, 0.5341]
    nocal_ndcg3 = [0.5296, 0.5296, 0.5296, 0.5296, 0.5296]
    x_value = [0.2, 0.4, 0.6, 0.8, 1.0]
    x_label = ["20%", "40%", "60%", "80%", "100%"]
    ax1.plot(x, map, 'o-', color='#1f77b4', label="CL-MAP")
    ax1.plot(x, ndcg3, '^-' ,color='#ff7f0e', label="CL-NDCG@3")
    ax1.plot(x, nocl_map, 'o--', color='#1f77b4', label="None-MAP")
    ax1.plot(x, nocal_ndcg3, '^--' ,color='#ff7f0e', label="None-NDCG@3")
    ax1.set_ylim(0.525, 0.551)
    ax1.set_xticks(x_value)
    ax1.set_xticklabels(x_label, fontproperties=myfont4)
    ax1.set_yticklabels(["0.525", "0.530", "0.535", "0.540", "0.545", "0.550"], fontproperties=myfont4)
    ax1.legend(prop=myfont3, loc="center right", bbox_to_anchor=(1.0, 0.55))
    ax1.set_xlabel("Data Amount", fontproperties=myfont4)
    ax1.grid(alpha=0.3, linestyle='--')

    map = [0.5462, 0.5472, 0.5481, 0.5500, 0.5497]
    ndcg3 = [0.5433, 0.5450, 0.5452, 0.5478, 0.5476]
    nocl_map = [0.5341, 0.5341, 0.5341, 0.5341, 0.5341]
    nocal_ndcg3 = [0.5296, 0.5296, 0.5296, 0.5296, 0.5296]

    x = [1, 2, 3, 4, 5]
    ax2.plot(x, map, 'o-', color='#1f77b4', label="CL-MAP")
    ax2.plot(x, ndcg3, '^-' ,color='#ff7f0e', label="CL-NDCG@3")
    ax2.plot(x, nocl_map, 'o--', color='#1f77b4', label="None-MAP")
    ax2.plot(x, nocal_ndcg3, '^--' ,color='#ff7f0e', label="None-NDCG@3")
    ax2.set_ylim(0.525, 0.551)
    ax2.set_xticks(x)
    ax2.set_xticklabels([1, 2, 3, 4, 5], fontproperties=myfont4)
    ax2.set_yticklabels(["0.525", "0.530", "0.535", "0.540", "0.545", "0.550"], fontproperties=myfont4)
    ax2.legend(prop=myfont3, loc="center right", bbox_to_anchor=(1.0, 0.55))
    ax2.set_xlabel("Training Epoch", fontproperties=myfont4)
    ax2.grid(alpha=0.3, linestyle='--')

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    x = [0.2, 0.4, 0.6, 0.8, 1]
    map = [0.5458, 0.5469, 0.5468, 0.5496, 0.5500]
    ndcg3 = [0.5429, 0.5433, 0.5441, 0.5475, 0.5478]
    nocl_map = [0.5341, 0.5341, 0.5341, 0.5341, 0.5341]
    nocal_ndcg3 = [0.5296, 0.5296, 0.5296, 0.5296, 0.5296]
    x_value = [0.2, 0.4, 0.6, 0.8, 1.0]
    x_label = ["20%", "40%", "60%", "80%", "100%"]
    ax1.plot(x, map, 'o-', color='#1f77b4', label="CL-MAP")
    ax1.plot(x, ndcg3, '^-', color='#ff7f0e', label="CL-NDCG@3")
    ax1.plot(x, nocl_map, 'o--', color='#1f77b4', label="None-MAP")
    ax1.plot(x, nocal_ndcg3, '^--', color='#ff7f0e', label="None-NDCG@3")
    ax1.set_ylim(0.525, 0.551)
    ax1.set_xticks(x_value)
    ax1.set_xticklabels(x_label, fontproperties=myfont4)
    ax1.set_yticklabels(["0.525", "0.530", "0.535", "0.540", "0.545", "0.550"], fontproperties=myfont4)
    ax1.legend(prop=myfont3, loc="center right", bbox_to_anchor=(1.0, 0.55))
    ax1.set_xlabel("Data Amount", fontproperties=myfont4)
    ax1.grid(alpha=0.3, linestyle='--')

    map = [0.5462, 0.5472, 0.5481, 0.5500, 0.5497]
    ndcg3 = [0.5433, 0.5450, 0.5452, 0.5478, 0.5476]
    nocl_map = [0.5341, 0.5341, 0.5341, 0.5341, 0.5341]
    nocal_ndcg3 = [0.5296, 0.5296, 0.5296, 0.5296, 0.5296]

    x = [1, 2, 3, 4, 5]
    ax2.plot(x, map, 'o-', color='#1f77b4', label="CL-MAP")
    ax2.plot(x, ndcg3, '^-', color='#ff7f0e', label="CL-NDCG@3")
    ax2.plot(x, nocl_map, 'o--', color='#1f77b4', label="None-MAP")
    ax2.plot(x, nocal_ndcg3, '^--', color='#ff7f0e', label="None-NDCG@3")
    ax2.set_ylim(0.525, 0.551)
    ax2.set_xticks(x)
    ax2.set_xticklabels([1, 2, 3, 4, 5], fontproperties=myfont4)
    ax2.set_yticklabels(["0.525", "0.530", "0.535", "0.540", "0.545", "0.550"], fontproperties=myfont4)
    ax2.legend(prop=myfont3, loc="center right", bbox_to_anchor=(1.0, 0.55))
    ax2.set_xlabel("Training Epoch", fontproperties=myfont4)
    ax2.grid(alpha=0.3, linestyle='--')


    plt.tight_layout()
    plt.savefig("output/figure4.png")
    plt.show()


draw_figure_4()
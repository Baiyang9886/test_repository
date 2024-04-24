import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np

myfont2 = FontProperties(fname='./TIMES.TTF', size=32)
myfont3 = FontProperties(fname='./TIMES.TTF', size=22)


def draw_figure_3():
    coca_map = [0.552700927070873, 0.543403267053195, 0.4876967263751009]
    duet_map = [0.4031463588267755, 0.39543176001219477, 0.384521141975356]
    cars_map = [0.4331293302456068, 0.4232857811441042, 0.3982938125484895]
    hba_map = [0.5315612397803664, 0.5264386514846908, 0.4780848161335488]

    coca_ndcg3 = [0.5502390266892377, 0.5390684662493154, 0.48418425092634415]
    duet_ndcg3 = [0.38460203985733127, 0.3762263757389652, 0.3671913235364889]
    cars_ndcg3 = [0.41548140827936514, 0.4038658384980803, 0.38140468885004214]
    hba_ndcg3 = [0.5277788066111762, 0.5212777296124101, 0.4729313905099101]

    x = np.arange(3)
    total_width, n = 0.8, 4  # 有多少个类型，只需更改n即可
    width = total_width / n
    x = x - (total_width - width) / 2
    label_list = ["Short", "Medium", "Long"]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
    hatch = [2 * '\\', 2 * '//', 2 * '.', 4 * '\\']
    ax1.bar(x, duet_map, width=width, label='Duet', hatch=hatch[0], edgecolor='w', color="#d62728")
    ax1.bar(x + width, cars_map, width=width, label='CARS', hatch=hatch[1], edgecolor='w', color="#1f77b4")
    ax1.bar(x + 2 * width, hba_map, width=width, label='HBA', hatch=hatch[2], edgecolor='w', color="#ff7f0e")
    ax1.bar(x + 3 * width, coca_map, width=width, label='COCA', hatch=hatch[3], edgecolor='w', color="#2ca02c")
    ax1.set_xticks([index + 1.5 * width for index in x])
    ax1.set_xticklabels(label_list, fontproperties=myfont2)
    # plt.yticks(y_label)
    label_format = '{:,.1f}'
    ax1.set_yticklabels(["0.30", "0.35", "0.40", "0.45", "0.50", "0.55", "0.60"], fontproperties=myfont2)
    ax1.set_ylim(0.3, 0.6)
    ax1.legend(prop=myfont3)
    ax1.set_ylabel("MAP", fontproperties=myfont2)

    ax2.bar(x, duet_ndcg3, width=width, label='Duet', hatch=hatch[0], edgecolor='w', color="#d62728")
    ax2.bar(x + width, cars_ndcg3, width=width, label='CARS', hatch=hatch[1], edgecolor='w', color="#1f77b4")
    ax2.bar(x + 2 * width, hba_ndcg3, width=width, label='HBA', hatch=hatch[2], edgecolor='w', color="#ff7f0e")
    ax2.bar(x + 3 * width, coca_ndcg3, width=width, label='COCA', hatch=hatch[3], edgecolor='w', color="#2ca02c")
    ax2.set_xticks([index + 1.5 * width for index in x])
    ax2.set_xticklabels(label_list, fontproperties=myfont2)
    ax2.set_yticklabels(["0.30", "0.35", "0.40", "0.45", "0.50", "0.55", "0.60"], fontproperties=myfont2)
    ax2.set_ylim(0.3, 0.6)
    ax2.legend(prop=myfont3)
    ax2.set_ylabel("NDCG@3", fontproperties=myfont2)

    plt.tight_layout()
    plt.savefig("output/figure3.png")
    plt.show()


draw_figure_3()
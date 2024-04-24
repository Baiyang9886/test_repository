import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np

myfont1 = FontProperties(fname="./TIMES.ttf", size=22)



def draw_figure_2():
    label_list = ['D1', 'D2', 'D3', 'D4', 'D5', 'D6']
    M1_P1 = [0.2091269841269841, 0.3030013247226363, 0.44205425061906556, 0.4910003050246953, 0.5527537277537277,
                    0.49428571428571433]
    M1_P2 = [0.22106392106392106, 0.3205253648901191, 0.46131253006253015, 0.510060828963268, 0.563666426166426,
                  0.5276190476190475]
    M2_P1 = [0.22857679107679105, 0.26725332954841174, 0.4182105445994338, 0.47823062213306106,
                   0.5194083694083694, 0.5461904761904762]
    M2_P2 = [0.23413234663234656, 0.2731276464883025, 0.43141846151105434, 0.4834700078602517, 0.5233766233766234,
                 0.5461904761904762]
    M3_P1 = [0.19460531960531957, 0.233750413975824, 0.3419656218267334, 0.4102632011168599, 0.48554593554593556,
                    0.5342857142857144]
    M3_P2 = [0.21825396825396817, 0.27174348875168575, 0.37706151016336237, 0.4297240699679726, 0.512000962000962,
                  0.5676190476190476]
    M4 = [0.09181141439205956, 0.3027295285359802, 0.40074441687344914, 0.15384615384615385,
                      0.04466501240694789, 0.00620347394540943]

    x = np.arange(6)

    total_width, n = 0.8, 7  # 有多少个类型，只需更改n即可
    width = total_width / n
    x = x - (total_width - width) / 2

    plt.figure(figsize=(16, 8))
    hatch = ['//',  '.', 2 * '//', 2 * '.', 4 * '//', 4 * '.', 2 * '\\']
    plt.bar(x, M1_P1, width=width, label='M1 + Part1', hatch=hatch[0], edgecolor='w')
    plt.bar(x + width, M1_P2, width=width, label='M1 + Part2', hatch=hatch[1], edgecolor='w')
    # plt.bar(x + 2 * width, num_list_3, width=width, label='CEOS', hatch=4*'\\', edgecolor='w')
    plt.bar(x + 2 * width, M2_P1, width=width, label='M2 + Part1', hatch=hatch[2], edgecolor='w')
    plt.bar(x + 3 * width, M2_P2, width=width, label='M2 + Part2', hatch=hatch[3], edgecolor='w')
    plt.bar(x + 4 * width, M3_P1, width=width, label='M3 + Part1', hatch=hatch[4], edgecolor='w')
    plt.bar(x + 5 * width, M3_P2, width=width, label='M3 + Part2', hatch=hatch[5], edgecolor='w')
    plt.bar(x + 6 * width, M4, width=width, label='M4', hatch=hatch[6], edgecolor='w')
    plt.xticks([index + 3 * width for index in x], label_list, fontproperties=myfont1)
    plt.yticks(fontproperties=myfont1)
    plt.legend(prop=myfont1)
    plt.tight_layout()
    plt.savefig("output/figure2.png")
    # plt.show()


draw_figure_2()
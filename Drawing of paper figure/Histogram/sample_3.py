import matplotlib.pyplot as plt

# Stacked bar chart

labels = ['G1', 'G2', 'G3', 'G4', 'G5']
P1_means = [20, 35, 30, 35, 27]
P2_means = [25, 32, 34, 20, 25]
P1_std = [2, 3, 4, 1, 2]
P2_std = [3, 5, 2, 3, 3]
width = 0.35       # the width of the bars: can also be len(x) sequence

fig, ax = plt.subplots()

ax.bar(labels, P1_means, width, yerr=P1_std, label='Part-1')
ax.bar(labels, P2_means, width, yerr=P2_std, bottom=P1_means,
       label='Part-2')

ax.set_ylabel('Scores')
ax.set_title('Scores by Model-1 and Model-2')
ax.legend()
plt.savefig(f"output/result_3.png")
# plt.show()
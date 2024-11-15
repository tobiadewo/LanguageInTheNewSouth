import os
import textgrid
from pprint import *

import matplotlib.pyplot as plt
import numpy as np

parents = {}
# parents = {"Both Parents from Georgia": ['1008', '1034', '1095', '2433', '3212', '5063', '5551', '8812'],
#            "One Parent from Georgia": ['5017', '5019', '5070', '5543', '8813'],
#            "Both Parents from America": ['1313', '3002', '4023', '5013', '5519', '5260', '6234', '9913'],
#            "Both Parents from the Caribbean": ['6978'],
#            "Both Parents from Africa": ['1708', '4341', '5033', '5036', '5066', '5099', '5111', '5538', '9012']}

# parents["Both Parents from Georgia"] = ['1008', '1095', '2433', '3212', '5063', '5551', '8812']
# parents["Both Parents from Africa"] = ['1708', '4341', '5033', '5036', '5066', '5099', '5111', '5538', '9012']

parents["Both Parents from Georgia"] = ['1034', '1095', '5017', '5019', '5070', '8813']
parents["Both Parents from Africa"] = ['4341', '5033', '5036', '5066', '5099', '9012']

grids = {k: {} for (k, v) in parents.items()}

for k in parents.keys():
    speakers = parents[k]
    for s in speakers:
        grid_path = "TextGrids/{}_Interview.TextGrid".format(s)
        if os.path.exists(grid_path):
            grid = textgrid.TextGrid.fromFile(grid_path)
            grids[k][s] = grid

word_counts = {k: {} for (k, v) in parents.items()}

for k in grids.keys():
    speakers = grids[k]
    for s in speakers:
        grid = grids[k][s][0]
        for i in range(len(grid)):
            if grid[i].mark:
                words = grid[i].mark.split()
                for word in words:
                    word = word.lower()
                    if word in word_counts[k].keys():
                        word_counts[k][word] += 1
                    else:
                        word_counts[k][word] = 1

for k in word_counts.keys():
    sorted_freq = dict(reversed(sorted(word_counts[k].items(), key = lambda item: item[1])))
    print(k)
    print(sorted_freq)
    print(len(list(sorted_freq.items())))
    print(sum(list(sorted_freq.values())))

    # x = np.array([k + " ({})".format(sorted_freq[k]) for k, v in sorted_freq.items()])
    # y = np.array(list(sorted_freq.values()))
    # # plt.show()
    #
    # fig, ax = plt.subplots()
    # # ax.pie(y, labels=x)
    # ax.pie(y)
    # plt.legend(labels=x, bbox_to_anchor=(1,1))
    # ax.set_title(k + " (Total words spoken: {})".format(sum(list(sorted_freq.values()))))
    # plt.show()

# pprint(len(grids['Both Parents from Africa']['4341'][0]))





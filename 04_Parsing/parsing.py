#!/usr/bin/python3

from io import open
from conllu import parse_incr
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

path = Path().absolute()

# plot stuff
labels = {0:'lat', 1:'spa', 2:'por',3:'fre',4:'ita', 5:'rom', 6:'cat', 7:'gal', 8:'hin', 9:'eng'}
x = []  # proportion of OV
y = []  # proportion of VO
plt.plot(x, y, 'ro')
plt.title('Relative word order of verb and object')
plt.xlim([0,1]) # Set the x and y axis ranges
plt.ylim([0,1])
plt.xlabel('OV') # Set the x and y axis labels
plt.ylabel('VO')

# computation stuff
def propDuples (filedir, xlist, ylist):

    data_file = path.joinpath(filedir).open("r", encoding="utf-8")

    sentences = list(parse_incr(data_file))

    total = 0
    numVO = 0
    numOV = 0

    column = []

    for i in sentences:
        for n in range(len(i)):
            column.append(i[n]['deprel'])
            if i[n]['deprel'] in {'obj','iobj'}:
                total += 1
                temp_id = int(i[n]['id'])
                temp_head = int(i[n]['head'])
                if temp_id > temp_head:
                    numOV += 1
                elif temp_id < temp_head:
                    numVO += 1

    propVO = round(numVO/total, 2)
    propOV = round(numOV/total, 2)

    res = list(zip(*np.unique(column, return_counts=True)))
    
    xlist.append(propOV)
    ylist.append(propVO)

    # print stuff
    print(res)
    print(sentences[0:4])
    print("Proportion Verb-Object: ", propVO)
    print("Proportion Object-Verb: ", propOV)

# directories and call the function
dir1 = 'UD_Latin-Perseus/la_perseus-ud-test.conllu'
dir2 = 'UD_Spanish-GSD/es_gsd-ud-test.conllu'
dir3 = 'UD_Portuguese-GSD/pt_gsd-ud-test.conllu'
dir4 = 'UD_French-GSD/fr_gsd-ud-test.conllu'
dir5 = 'UD_Italian-ISDT/it_isdt-ud-test.conllu'
dir6 = 'UD_Romanian-RRT/ro_rrt-ud-test.conllu'
dir7 = 'UD_Catalan-AnCora/ca_ancora-ud-test.conllu'
dir8 = 'UD_Galician-CTG/gl_ctg-ud-test.conllu'
dir9 = 'UD_Hindi-HDTB/hi_hdtb-ud-test.conllu'
dir10 = 'UD_English-EWT/en_ewt-ud-test.conllu'

directories = [dir1, dir2, dir3, dir4, dir5,
        dir6, dir7, dir8, dir9, dir10]

for lang in directories:
    propDuples (lang, x, y)

# create the plot
for i in labels:  # Add labels to each of the points
        plt.text(x[i]-0.03, y[i]-0.03, labels[i], fontsize=9)
        plt.savefig("parsing_romance.png")
        plt.show()

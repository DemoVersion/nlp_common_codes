import argparse
import random
import numpy as np
import matplotlib.pyplot as plt
import collections

# read from parameters
parser = argparse.ArgumentParser(description='Corpus Histogram Creator')
parser.add_argument('-input_file_path', action="store",required=True,help='Path of input file, The words in corpus should be tokenized and space seperated.')
results = parser.parse_args()
input_file_path=results.input_file_path

# create dictionary
count_dictionary = dict()
with open(input_file_path,"r") as f_in:
    line_id = 0
    for line in f_in:
        words = line.strip('\n').strip(' ').split(" ")
        line_o = ""
        for word in words:
            if word in count_dictionary:
                count_dictionary[word] +=1
            else:
                count_dictionary[word] =1
        line_id = line_id + 1
        if line_id % 10000 == 0 or line_id % 10000 == 1:
            print(line_id)
            print(line)
# create plot
fig=plt.figure()
data=np.array(list(count_dictionary.values()))
plt.hist(data, bins=np.logspace(np.log10(1),np.log10(10000), 50))
plt.gca().set_xscale("log")
plt.title(input_file_path)
plt.xlabel("Number of occurrences")
plt.ylabel("Number of words")
plt.show()
#fig.savefig(input_file_path+".png")
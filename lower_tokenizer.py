import argparse
import nltk

from nltk.stem.lancaster import LancasterStemmer

def line_by_line(file_input,file_output):
	line_id=0
	with open(file_input, "r") as f_in:
		with open(file_output,"w") as f_out:
			for line in f_in:
				lowers = line.lower()
				tokens = nltk.word_tokenize(lowers)
				line2=' '.join(tokens)
				f_out.write(line2+"\n")
				line_id = line_id+1
				if line_id%100000 == 0:
					print(line_id)
					print(line)
					print(line2)
#Parsing Parameters
parser = argparse.ArgumentParser(description='Lower Tokenizer')
parser.add_argument('-file_in_name', action="store",required=True,help='Path of input file.')
parser.add_argument('-file_out_name', action="store",required=True,help='Path of output file.')
results = parser.parse_args()
#Tokenization
file_in_name=results.file_in_name
file_out_name=results.file_out_name
line_by_line(file_in_name,file_out_name)
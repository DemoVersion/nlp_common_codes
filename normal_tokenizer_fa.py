from hazm import *
def line_by_line(file_input,file_output):
	line_id=0
	normalizer = Normalizer()
	with open(file_input, "r") as f_in:
		with open(file_output,"w") as f_out:
			for line in f_in:
				normalized = normalizer.normalize(line.lower())
				tokens = word_tokenize(normalized)
				line2=' '.join(tokens)
				line2=line2.replace('_',' ')
				f_out.write(line2+"\n")
				line_id = line_id + 1
				if line_id%10000 == 0:
					print(line_id)
					print(line)
					print(line2)
#Parsing Parameters
parser = argparse.ArgumentParser(description='Normalizer Tokenizer')
parser.add_argument('-file_in_name', action="store",required=True,help='Path of input file.')
parser.add_argument('-file_out_name', action="store",required=True,help='Path of output file.')
results = parser.parse_args()
#Tokenization
file_in_name=results.file_in_name
file_out_name=results.file_out_name
line_by_line(file_in_name,file_out_name)
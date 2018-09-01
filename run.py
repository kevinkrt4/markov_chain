#import sys
#print (sys.path)
from markov_python.cc_markov import MarkovChain

mc = MarkovChain()
mc.add_file('/home/krt4/CA/markov_chain/shakespeare.txt')
print(mc.generate_text())

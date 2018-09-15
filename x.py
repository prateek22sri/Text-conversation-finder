import os
from nltk.parse import stanford
os.environ['STANFORD_PARSER'] = '/Users/prateeksrivastava/stanford-corenlp/stanford-corenlp-3.8.0.jar'
os.environ['STANFORD_MODELS'] = '/Users/prateeksrivastava/stanford-corenlp/stanford-corenlp-3.8.0-models.jar'

parser = stanford.StanfordParser(model_path="/location/of/the/englishPCFG.ser.gz")
sentences = parser.raw_parse_sents(("Hello, My name is Melroy.", "What is your name?"))
print sentences

# GUI
for line in sentences:
    for sentence in line:
        sentence.draw()
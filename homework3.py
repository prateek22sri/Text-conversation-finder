from pycorenlp import StanfordCoreNLP

class wrapper:
    def __init__(self):
        self.nlp = None
        self.text = ""
        self.actionVerb = []
        self.sentenceList = []
        self.converstaion = tuple()
        self.converstaionDistribution = {self.converstaion: None}
        self.actionVerbReader('actionVerb.txt')
        self.sent = []

    def actionVerbReader(self, filename):
        with open(filename) as f:
            for words in f:
                self.actionVerb.append(words.lower().strip('\n'))

    def read(self, filename):
        with open('books/' + filename, 'r') as f:
            text = f.read()
        return text

    def parse(self, text):
        self.text = text
        self.nlp = StanfordCoreNLP('http://localhost:9000')

        output = self.nlp.annotate(
            text,
            properties={
                "outputFormat": "json",
                "annotators": "ssplit,dcoref",
                "ssplit.boundaryTokenRegex" : "[.]+"
            }
        )

        return output

    def findConversation(self, output):
        sets = set()
        senList = []
        print("Total Sentences = ",len(output['sentences']))
        for sentence in output['sentences']:
            for token in sentence['tokens']:
                if token['lemma'] in self.actionVerb:
                    sent = " ".join(wordsList['word'] for wordsList in sentence['tokens'])
                    senList.append(sent)
                    for wordlist in sentence['tokens']:
                        if wordlist['ner'] == 'PERSON':
                            sets.add(wordlist['word'])
        count = 0
        for i in senList:
            for names in sets:
                if names in i:
                    count+=1

        print("Dialog count in the text was ",count)

if __name__ == '__main__':
    w = wrapper()
    # filename = 'a_christmas_carol.txt'
    filename = 'chapter1.txt'
    # filename = 'alice_chapter1.txt'
    text = w.read(filename)
    output = w.parse(text)
    w.findConversation(output)

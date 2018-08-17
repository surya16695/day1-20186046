'''
    Document Distance - A detailed description is given in the PDF
'''

def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    dict1_temp = dict1.lower()
    dict2_temp = dict2.lower()

def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords
def make_dict(input)
	for word in input:
    	if word not in dict1:
    		dict1[word] = 1
    	else :
    		dict1[word] += 1
    return dict1
def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()
    input_1 = input1.lower()
    input_2 = input2.lower()
    #print(input1)
    #print(input2)
    dict1 = {}
    dict2 = {}
    input_1 = input_1.strip().replace('.', '').replace(',', '').replace('?', '').split()
    #print(input_1)
    input_2 = input_2.strip().replace('.', '').replace(',', '').replace('?', '').split()
    #print(input_2)
    dict1 = make_dict(input_1)
    print(dict1)
    dict2 = make_dict(input_2)
    print(dict2)
    print(similarity(input1, input2))

if __name__ == '__main__':
    main()

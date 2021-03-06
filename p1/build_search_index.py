'''
    Tiny Search Engine - Part 1 - Build a search index

    In this programming assingment you are given with some text documents as input.
    Complete the program below to build a search index. Don't worry, it is explained below.
    A search index is a python dictionary.
    The keys of this dictionary are words contained in ALL the input text documents.
    The values are a list of documents such that the key/word appears in each document atleast once.
    The document in the list is represented as a tuple.
    The tuple has 2 items. The first item is the document ID.
    Document ID is represented by the list index.
    For example: the document ID of the third document in the list is 2
    The second item of the tuple is the frequency of the word occuring in the document.

    Here is the sample format of the dictionary.
    {
        word1: [(doc_id, frequency),(doc_id, frequency),...],
        word2: [(doc_id, frequency),(doc_id, frequency),...],
        .
        .
    }
'''
import re
def make_dict(input):
    dict_1 = {}
    for i in range (len(input)):
        dict_1[i] = input[i]
    #print(dict_1)
    return dict_1


# helper function to load the stop words from a file
def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as f_stopwords:
        for line in f_stopwords:
            stopwords[line.strip()] = 0
    return stopwords


def word_list(dict_0):
    '''
        Change case to lower and split the words using a SPACE
        Clean up the text by remvoing all the non alphabet characters
        return a list of words
    '''
    for key in  dict_0:
        dict_0[key] = dict_0[key].lower()
        regex = re.compile('[^a-z ]')
        dict_0[key] = regex.sub('', dict_0[key])
        dict_0[key] = dict_0[key].split()
    #print(dict_0)
    return dict_0

def computing(dict):
    word_s = load_stopwords('stopwords.txt')
    #print(word_s)
    for key in dict:
        for word in dict[key]:
            if word in word_s:
                dict[key] = dict[key] - word_s.keys()

    return dict

def build_search_index(docs):
    '''
        Process the docs step by step as given below
    '''
    dic_5 = {}
    # initialize a search index (an empty dictionary)
    dic_2 = {}
    dic_3 = {}
    dic_4 = {}
    # iterate through all the docs
    dic_2 = make_dict(docs)
    dic_3 = word_list(dic_2)
    #print (dic_3)
    dic_4 = computing(dic_3)
    dic_5 = index(dic_4)
    #print(dic_4)
    return dic_5

def index(dic_4):
    index_1 = {}
    dict_temp = {}
    for i in dic_4.keys():
        dict_temp[i] = str(dic_4[i])
    print (dict_temp)
    coun_t = 1
    k = 0
    while i in dict_temp.keys():
        if values in dict_temp[key]:
            index_1[values] = (key, coun_t+1)
        i = i+1
    print (dict_temp)
    return index_1

    # keep track of doc_id which is the list index corresponding the document
    # hint: use enumerate to obtain the list index in the for loop

        # clean up doc and tokenize to words list

        # add or update the words of the doc to the search index


    # return search index


# helper function to print the search index
# use this to verify how the search index looks
def print_search_index(index):
    '''
        print the search index
    '''
    keys = sorted(index.keys())
    for key in keys:
        print(key, " - ", index[key])

# main function that loads the docs from files
def main():
    '''
        main function
    '''
    # empty document list

    documents = []
    # iterate for n times
    lines = int(input())
    # iterate through N times and add documents to the list
    for i in range(lines):
        documents.append(input())
        i += 1
    #print(documents)
 
    # call print to display the search index
    print_search_index(build_search_index(documents))

if __name__ == '__main__':
    main()

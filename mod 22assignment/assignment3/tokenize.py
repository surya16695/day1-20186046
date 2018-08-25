'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
def clean_string(string):
    """ cleaning of string"""
    input_string = string
    regex = re.compile("[^a-zA-Z0-9]")
    input_string = regex.sub('', input_string)
    return input_string

def tokenize(string):
    dic_t = {}
    count_1 = 0
    for i in range(len(string)):
        for word in string:
            if word  in dic_t:
                dic_t[word] += 1
            else:
                dic_t[word] = 1
    return dic_t
    
def main():
    n = int(input())
    l_1 = ""
    for i in range(n):
        l_1 += input()
        i = i+1
    # print(l_1)
    print(tokenize(l_1.split()))
if __name__ == '__main__':
    main()

'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string):
    dic_t = {}
    count_1 = 0
    for i in range(len(string)):
        for word in string:
            if word not in dic_t.keys():
                dic_t[word] = 1
            else:
                dic_t[word] += 1
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

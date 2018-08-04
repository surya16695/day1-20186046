'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
def main():
    '''
    Read string from the input, store it in variable str_input.
    '''
    str_input = input()
    s = ""
    for i in str_input:
    	if i in ('!', '@', '#', '$', '%', '^', '&', '*'):
    	    s = s+" "
    	else:
    	    s = s+i
    print(s)
if __name__ == "__main__":
    main()

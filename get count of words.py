# get count of words

def get_counts_words(string: str)-> int:

    counter = 1
    
    if (len(string) == 0):

        return 0


    for char in string:

        if char == ' ' or char == '\t' or char == '\n':

            counter+= 1

    return counter

def invoke_get_words_counts():

    input = 'hello word'

    count = get_counts_words(input)

    print(f'total count of words is {count}')

# invocation code

invoke_get_words_counts()
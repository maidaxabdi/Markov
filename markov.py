"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    # your code goes here
    overall_text = open(file_path).read()


    return overall_text


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    # your code goes here
    
    new_text = text_string.split() #splits all the blankspace so there is no \n
    for i in range(len(new_text) - 2):
        bi_tuple = (new_text[i], new_text[i+1])
        
        # chains[bi_tuple] = []
        if bi_tuple in chains.keys():
           chains[bi_tuple].append(new_text[i + 2])
        else:
            chains[bi_tuple] = [new_text[i + 2]]
      
        
    return chains


def make_text(chains):
    """Return text from chains."""

    word_picked = choice(chains.keys()) #tuple of two words
    words = list(word_picked) #makes a list of the tuples
    
    while True:
        new_word = choice(chains[word_picked])
        words.append(new_word)
        new_key = (word_picked[1], new_word)
        

    # your code goes here
    #for i in range(len(chains)):
    #    if chains[i] in chains.keys():
    #        words.append(chains[1])
        #words.append(chains[1][i])
        
        
    return ' '.join(words)
# make a new key for the second word out of the first key in our dictionary EX: ('Would', 'You') <- use You.
# whatever value for that key, pull a random word from the list that follows it.
# Using the new key, look up the new key in the dictionary and pull a new random word from the new list
# keep going until KeyError
# Remember that the last line of text from green-eggs.txt is "Sam I am?"


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# # Get a Markov chain
chains = make_chains(input_text)
# print(make_chains(input_text))

# # Produce random text
random_text = make_text(chains)
print(random_text)

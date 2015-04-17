import sys
import random

# maya_poem = open("maya-angelou.txt")
# maya_string = maya_poem.read(len(maya_poem))
# for word in maya_poem:
#     word = word.rstrip()
#     word = word.split(' ')
# print maya_poem

def make_chains(corpus):
    """Takes input text as string; returns dictionary of markov chains."""
    split_text = corpus.split()
    
    chain_dict = {}

    for i in range(len(split_text) - 2):
        key = (split_text[i], split_text[i + 1])
        value = split_text[i + 2]

        if key not in chain_dict:
            chain_dict[key] = [value]
        else:
            chain_dict[key].append(value) 

    # print chain_dict
    # print split_text

    return chain_dict


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""
    word_list = []

    # Step 1: Choose random key from chains
    current_key = random.choice(chains.keys())
    print current_key
    # Step 2: Put words of random key into a list
    # sub-Step 2: We should see a list that has two words
    # sub-sub-Step 2: Two words should be the word from tuple
    # Step 3: With two words in word list, use a while loop, 
            # probably key in dictionary. 
    # Step 4: While in while loop, choose a value for the key
    # while current_key in chains 
    # Step 5: Place value, append to word list
    # Step 6: Make a new key that will be the second word of the current key for our next value.
    # current_key = (current_key[1], value) 
    print word_list
    return "Here's some random text."


# # Change this to read input_text from a file, deciding which file should
# # be used by examining the `sys.argv` arguments (if neccessary, see the
# # Python docs for sys.argv)

print sys.argv[1]
# input_text = "Some text"
input_file = open(sys.argv[1])
# input_file = open('green-eggs.txt')
input_text = input_file.read()
#print input_text                                                                                                                    
# Get a Markov chain
chain_dict = make_chains(input_text)

# # Produce random text
random_text = make_text(chain_dict)

#print random_text

import sys
import random

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

    return chain_dict


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    # Step 1: Choose random key from chains
    current_key = random.choice(chains.keys())
    word_list = [current_key[0], current_key[1]]
    # Step 2: Put words of random key into a list
    # sub-Step 2: We should see a list that has two words
    # sub-sub-Step 2: Two words should be the word from tuple
    # Step 3: With two words in word list, use a while loop, 
            # probably key in dictionary.
    while current_key in chains:  
    # Step 4: While in while loop, choose a value for the key
        word = random.choice(chains[current_key])
    # while current_key in chains 
    # Step 5: Place value, append to word list
        word_list.append(word)
    # Step 6: Make a new key that will be the second word of the current key for our next value.
    # current_key = (current_key[1], value) 
        current_key = (current_key[1], word)

    return " ".join(word_list)

# # Change this to read input_text from a file, deciding which file should
# # be used by examining the `sys.argv` arguments (if neccessary, see the
# # Python docs for sys.argv)

# input_text = "Some text"
# input_file = open(sys.argv[1])
input_file = open('green-eggs.txt')
input_text = input_file.read() 

# Get a Markov chain
chains = make_chains(input_text)

# # Produce random text
random_text = make_text(chains)
print random_text




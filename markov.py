"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    the_stringified_file = open(file_path).read()
    return the_stringified_file


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
    # stringified_text = open_and_read_file("/Users/gedailey/src/markov-chains/green-eggs.txt")

    words = text_string.split()

    for index in range(len(words) - 2):
        # print(words[word], words[word + 1])
        key = (words[index], words[index + 1])
        if key not in chains:
            chains[key] = [words[index + 2]]
        else:
            chains[key].append(words[index + 2])

        # value = []

        # for key, value in chains.items():
        #     if key == (words[word], words[word + 1]):
        #         value.append(words[word +2])
        # else:
        #     chains[(words[word], words[word + 1])] = []


# If we assign the word at i+2 as the value to our key, we’ll overwrite
# the value every time we find another instance of that word pair in our text. So instead, let’s create a list as the value and append words into it.

# But when do you make an empty list and when do you append into it? Check
# to see if the key is in the dictionary already. If it’s not, make sure you initialize that list and put your word into it. If the key is already in the dictionary, append your word to the list that’s already there.

    return chains

print(make_chains(open_and_read_file("/Users/gedailey/src/markov-chains/gettysburg.txt")))

#output {(This, is): [a, helps, banana]}

def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)

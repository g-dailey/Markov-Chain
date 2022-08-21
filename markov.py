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

    words = text_string.split()

    for index in range(len(words) - 2):
        key = (words[index], words[index + 1])
        if key not in chains:
            chains[key] = [words[index + 2]]
        else:
            chains[key].append(words[index + 2])


    return chains


def make_text(chains):
    """Return text from chains."""


    chained_dictionary = make_chains(open_and_read_file("/Users/gedailey/src/markov-chains/green-eggs.txt"))


    words = []
    all_keys = []

    for key, value in chained_dictionary.items():
        all_keys.append(key)

    random_key = choice(all_keys)

    words.append(random_key)

    for key, value in chained_dictionary.items():
        if random_key == key:
            random_value = choice(value)
            words.append(random_value)


    additional_key = (words[0][1], words[1])

    for key, value in chained_dictionary.items():
        if key not in chained_dictionary:
                chained_dictionary[additional_key] = choice(value)
        else:
            pass

        print(f"{key[0]} {key[1]} {value[0]}")


    # print(chained_dictionary)

input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

# print(random_text)

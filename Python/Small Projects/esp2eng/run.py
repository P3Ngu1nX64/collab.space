import string
import json
from sys import argv, exit

prompt = "> "


class Language:
    def __init__(self, name):
        self.name = name
        self.abbrev = None


class Dictionary:

    def __init__(self, infile):
        self.infile = infile
        data = open(infile).read()
        self.dict = {}
        for i in json.loads(data):
            self.dict.update(i)

        self.length = len(self.dict)
        self.lang_in = None  # Requires class Language()
        self.lang_out = None  # Requires class Language()

    def append(self, dict_new):
        """Append a dictionary to self.dict"""
        self.dict.update(dict_new)
        self.length = len(self.dict)

    def append_UI(self):
        """Interactive appending to dictionary"""
        print("""UI Dictionary Appender
Type [!x] to exit
Type [!s] to save to file
Type [!d] to display changes
""")
        exit_script = False
        append_dic = {}
        while not exit_script:
            term_in = input("[{}]{}".format(self.lang_in.name, prompt))
            if term_in == "!x":
                exit_script = True
                break
            elif term_in == "!s":
                self.write()
                print("Dictionary saved to {}.".format(self.infile))
            elif term_in == "!d":
                print('-' * 10)
                n = 1
                for i in sorted(append_dic.keys()):
                    print(f"{n}: ESP=\"{i}\", ENG=\"{append_dic[i]}\"")
                    n += 1
                print('-' * 10)
            else:
                term_out = input("[{}]{}".format(self.lang_out.name, prompt))
                if term_out == "!x":
                    exit_script = True
                    break
                elif term_out == "!s" or term_out == "!d":
                    print("Error: Option not valid")
                else:
                    append_dic.update({term_in: term_out})
        self.dict.update(append_dic)

    def delete(self, entry):
        """deletes an entry"""
        term_out = self.dict.pop(entry)
        print("Removed: {}={}, {}={}".format(self.lang_in.abbrev, entry,
                                             self.lang_out.abbrev, term_out))

    def display(self):
        """displays the dictionary"""
        print('-' * 10)
        n = 1
        for i in sorted(self.dict.keys()):
            print("{}: {}=\"{}\", {}=\"{}\"".format(n, self.lang_in.abbrev, i,
                                                    self.lang_out.abbrev,
                                                    self.dict[i]))
            n += 1
        print('-' * 10)

    def read(self):
        """read the input_file again"""
        data = open(self.infile).read()
        self.dict = {}
        for i in json.loads(data):
            self.dict.update(i)
        print(f"File {self.infile} read.")
        self.length = len(self.dict)

    def write(self):
        """Write/Update to input file"""
        with open(self.infile, 'w') as outfile:
            outfile.write("[")
            json.dump(self.dict, outfile)
            outfile.write("]")
        print(f"File {self.infile} written.")


def transliterate(dictionary):  # ESP->ENGT Only
    """Takes in a dictionary for translation or transliteration"""
    sentence = input("Please enter (in {})\n[{}]{}".format(
               dictionary.lang_in.name, dictionary.lang_in.abbrev, prompt))
    if sentence == "!r":
        return True  # For Special Mode
    elif sentence == "!x":
        return 'quit'
    # Adds special characters to Spanish
    esp_punctuation = string.punctuation + "¡¿"
    # Makes a translation table for removing punctuations
    table = str.maketrans('', '', esp_punctuation)
    words = sentence.split(' ')
    new_words = []
    for i in words:
        # Uncapitalize and strip punctuations from "i"
        processed_i = i.casefold().translate(table)
        # Gets JSON dictionary translation of word (if available)
        # If not available, use original "i", and set a boolean to the value.
        in_dic = False
        if processed_i in dictionary.dict:
            in_dic = True
        new_word = dictionary.dict.get(processed_i, i)
        # Refers back to original "i" to determine whether to capitalize
        if i.istitle():
            new_word = new_word.capitalize()

        if in_dic:
            last_char = i[-1]  # Possible last character is Punctuation
            if last_char == ',':
                new_word += ','
            elif last_char == '.':
                new_word += '.'
            elif last_char == '!':
                new_word += '!'
            elif last_char == '?':
                new_word += '?'
            elif last_char == ';':
                new_word += ';'
            elif last_char == ':':
                new_word += ':'
        # No need for an Else clause
        # Adds to printed list.
        new_words.append(new_word)
    # Prints the concatenated list.
    print(' '.join(new_words))
    return False  # For special mode


# Set Up

spanish = Language('Spanish')
spanish.abbrev = 'ESP'
english = Language('English')
english.abbrev = 'ENG'

esp2eng = Dictionary('dict.json')
esp2eng.lang_in = spanish
esp2eng.lang_out = english


# Special Mode(s):

if len(argv) == 2 and (argv[1] == "-t" or argv[1] == "--transliterate"):
    exit_script = False
    print("Entering Transliteration Only Mode...\n")
    print("Type [!r] to return to main script")
    print("Type [!x] to exit script")
    while not exit_script:
        exit_script = transliterate(esp2eng)
        if exit_script == 'quit':  # While loop will not be able to see this.
            exit(0)


help_menu = """
Options:
[a] Add Words
[d] Delete a Word
[o] Check Entire Database
[w] Check a Specific Word
[u] Update Database from File
[t] Transliterate
[s] Save Changes
[h] Help Menu
[x] Exit
"""

stats_menu = f"""
Stats:
Language in = {esp2eng.lang_in.name}, Abbreviation = {esp2eng.lang_in.abbrev}
Language out = {esp2eng.lang_out.name}, Abbreviation = {esp2eng.lang_out.abbrev
}
Words = {esp2eng.length}"""


# Main Loop:

print(f"""\n{esp2eng.lang_in.name} to {esp2eng.lang_out.name} Transliterator
{stats_menu}
{help_menu}""")

exit_script = False

while not exit_script:
    command = input(prompt)
    if command.casefold() == 'a':
        esp2eng.append_UI()
    elif command.casefold() == 'd':
        entry = input("Which word to delete?\n{}".format(prompt))
        esp2eng.delete(entry)
    elif command.casefold() == 'o':
        print(stats_menu, end='\n\n')
        esp2eng.display()
    elif command.casefold() == 'w':
        index = input("Please Enter Search Entry:\n[{}]{}".format(
                      esp2eng.lang_in.abbrev, prompt))
        print('-' * 10)
        if index in esp2eng.dict:
            print("1: {}=\"{}\", {}=\"{}\"".format(esp2eng.lang_in.abbrev,
                                                   index,
                                                   esp2eng.lang_out.abbrev,
                                                   esp2eng.dict.get(index)))
        else:
            print("1: ENTRY DOES NOT EXIST.")
        print('-' * 10)
    elif command.casefold() == 'u':
        esp2eng.read()
    elif command.casefold() == 't':
        transliterate(esp2eng)
    elif command.casefold() == 's':
        esp2eng.write()
    elif command.casefold() == 'h':
        print(help_menu)
    elif command.casefold() == 'x':
        # Breaks the while loop at any time (command page) with "x"
        exit_script = True
    else:
        print("Invalid Option.")

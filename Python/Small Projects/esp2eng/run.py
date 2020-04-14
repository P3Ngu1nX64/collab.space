import json

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
        exit = False
        append_dic = {}
        while not exit:
            term_in = input("[{}]{}".format(self.lang_in.name, prompt))
            if term_in == "!x":
                exit = True
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
                    exit = True
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


def transliterate(dictionary):
    """Takes in a dictionary for translation or transliteration"""
    sentence = input("Please enter (in {})\n[{}]{}".format(
               dictionary.lang_in.name, dictionary.lang_in.abbrev, prompt))
    words = sentence.split(' ')
    new_words = []
    for i in words:
        new_words.append(dictionary.dict.get(i, i))

    print(' '.join(new_words))


spanish = Language('Spanish')
spanish.abbrev = 'ESP'
english = Language('English')
english.abbrev = 'ENG'

esp2eng = Dictionary('dict.json')
esp2eng.lang_in = spanish
esp2eng.lang_out = english

help_menu = """
Options:
[a] Add Words
[d] Delete a Word
[o] Check Database
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

print(f"""\n{esp2eng.lang_in.name} to {esp2eng.lang_out.name} Transliterator
{stats_menu}
{help_menu}""")

exit = False

while not exit:
    command = input(prompt)
    if command == 'a' or command == 'A':
        esp2eng.append_UI()
    elif command == 'd' or command == 'D':
        entry = input("Which word to delete?\n{}".format(prompt))
        esp2eng.delete(entry)
    elif command == 'o' or command == 'O':
        print(stats_menu, end='\n\n')
        esp2eng.display()
    elif command == 'u' or command == 'U':
        esp2eng.read()
    elif command == 't' or command == 'T':
        transliterate(esp2eng)
    elif command == 's' or command == 'S':
        esp2eng.write()
    elif command == 'h' or command == 'H':
        print(help_menu)
    elif command == 'x' or command == 'X':
        exit = True
    else:
        print("Invalid Option.")

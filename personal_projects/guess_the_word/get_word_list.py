import re

import json


def get_word_list():
    """
    Generate a list of all distinct words from the text.

    Using re module, the function will look for string of words that are 3 to
    8 characters long and distinct, and will be stored in a json file for future use cases.

    Returns
    -------
    None.

    """
    with open('the_time_machine.txt', 'r', encoding='UTF-8') as f:
        f_obj = f.read()
    pattern = re.compile(r"(\b[a-zA-Z][a-z]{3,15}\b)")
    matches = re.findall(pattern, f_obj)
    words = list(set(matches))
    with open("word_list.json", "w+", encoding="UTF-8") as f:
        json.dump(words, f)
    pass


def main():
    """
    Will call all the other functions of the module.

    Returns
    -------
    None.

    """
    get_word_list()


if __name__ == "__main__":
    main()

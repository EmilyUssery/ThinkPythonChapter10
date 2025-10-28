def words_d(file_path:str) -> dict:
    words = {}
    with open(file_path,'r') as fp:
        for line in fp:
            line = line.strip().lower()
            if len (line) >= 3:
                words[line] = True
            return words


def is_interlocking(word_in)-> bool:
    first = word_in[0::2]
    second = word_in[1::2]
    return word_dict.get(first,False) and word_dict.get(second, False)



print(is_interlocking('schooled', words_d('words.txt')))
def value_counts(string):
    counter = {}
    for letter in string:
        if letter not in counter:
            counter[letter] = 1
        else:
            counter[letter] += 1
    return counter

def value_counts_e(string):
    counter = {}
    for letter in string:
        counter[letter] = counter.get(letter, 0) + 1
    return counter

def has_duplicates(sequence):
    seen = set()
    for element in sequence:
        if element in seen:
            return True
        seen.add(element)
    return False

def finds_repeats(counter):
    repeats = []
    for letter, count in counter.items():
        if count > 1:
            repeats.append(letter)
        return []






print(value_counts("october"))
print(value_counts_e("october"))







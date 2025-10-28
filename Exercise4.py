from Exercise02 import value_counts_efficient

def finds_repeats(counter):
    repeats = []
    for letter, count in counter.items():
        if count > 1:
            repeats.append(letter)
    return repeats

print(finds_repeats(value_counts_efficient("halloween")))


from Exercise02 import value_counts_efficient
# {'b': 1, 'r' :2, 'o':2 , 'n': 1 , 't' : 1, 'o': 2 , 's': 2, 'a' : 1, 'u': 2,'r': 1,'u' : 2',s': 2}
# {'a': 3, 'p': 1, 'a':3, 't': 1, 'o': 1, 's': 2, 'a': 3, 'u':2, 'r': 1,'u': 2 ,'s': 2 }
# {'b' : 1, 'r': 3, 'o' : 3, 'n' 1, 't': 2, 'o': 3, 's': 4, 'a': 4, 'u': 4 'r': 2, 'u': 3, 's': 4, 'a': 4, 'p': 1, 'a': 4, 't': 2, 'o': 3, 's': 4, 'a': 4, 'u': 4, 'r': 3, 'u': 4, 's': 4}


def add_counter(d1:dict, d2:dict) -> dict:
    # copy first dict d1
    counter = dict(d1)
    # Loop over Second dict d2
    for k, v in d2.items():
        # if the key from d2 is in d1 add value
        if k in counter:
            counter [k] = v
            # else add ket and value to d1
        else:
            counter[k] = v
            # return your result
            return counter

if __name__ == '__main__':
    counter1 = value_counts_efficient('brontosaurus')
    counter2 = value_counts_efficient('apatosaurus')
    # {'b': 1, 'r' :2, 'o':2 , 'n': 1 , 't' : 1, 'o': 2 , 's': 2, 'a' : 1, 'u': 2,'r': 1,'u' : 2',s': 2}
    # {'a': 3, 'p': 1, 'a':3, 't': 1, 'o': 1, 's': 2, 'a': 3, 'u':2, 'r': 1,'u': 2 ,'s': 2 }
    print(counter1)
    print(counter2)
    print(add_counter(counter1, counter2))



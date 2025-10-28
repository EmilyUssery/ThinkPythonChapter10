def has_duplicates(sequence):
    seen = set()
    for element in sequence:
        if element in seen:
            return True
        seen.add(element)
    return False

print(has_duplicates("unpredictably"))
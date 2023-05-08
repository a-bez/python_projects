def serch_longest_string(list_of_strings):
    # step1
    list_of_string_length = [len(string) for string in list_of_strings]
    list_of_string_length = zip(list_of_strings, list_of_string_length)
    #step2
    max_length = max(list_of_string_length, key=lambda t: t[1])

    return max_length


print(serch_longest_string(['a bdfa dsfrgadfdrg5', 'bdfa', 'fsd', 'dsfrgadfdrg5', 'fdab', 'sefdpijc4 fdab']))
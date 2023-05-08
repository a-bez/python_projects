def serch_longest_string(list_of_strings):
    longest_string = None
    longest_string_length = 0

    for string in list_of_strings:
        if len(string) > longest_string_length:
            longest_string_length = len(string)
            longest_string = string

    return longest_string

print(serch_longest_string(['a', 'bdfa', 'fsd', 'dsfrgadfdrg5', 'fdab', 'sefdpijc4']))
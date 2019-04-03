def compare(str1, str2):
    to_string = lambda inp : str(inp) if type(inp) != str else inp

    if str1 == None or str2 == None:
        raise ValueError()

    str1=to_string(str1)
    str2=to_string(str2)
    
    for char1, char2 in zip(str1, str2):
        ascii1 = ord(char1)
        ascii2 = ord(char2)
        if ascii1 != ascii2:
            return 1 if ascii1 > ascii2 else -1

    return 0 if len(str1) == len(str2) else (1 if len(str1) > len(str2) else -1)

     
def quote_hell(x):
    """
    spaces reverse groups
    single quotes are literal quotes
    double quotes just group
    """
    i = 0

    def read_quote(quotechar=None):
        nonlocal i
        result = ''
        while i < len(x):
            letter = x[i]
            i += 1
            if letter == ' ' and quotechar != "'":
                result2 = read_quote(quotechar)
                return result2 + ' ' + result
            if letter == quotechar:
                return result
            if letter == '"' and quotechar is None:
                result += read_quote('"')
            elif letter == "'" and quotechar is None:
                result += read_quote("'")
            else:
                result += letter
        return result
    return read_quote()

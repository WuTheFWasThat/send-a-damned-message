def quote_hell(x):
    """spaces swap order, double quotes group, single quotes group and make spaces literal spaces"""
    i = 0

    def read_quote(quotechar=None):
        nonlocal i
        result = ''
        while i < len(x):
            letter = x[i]
            i += 1
            if letter == ' ' and quotechar != "'":
                result2 = read_quote(quotechar)
                # since we re-enter with same quotechar, we must exit if exited
                return result2 + ' ' + result
            elif letter == quotechar:
                return result
            elif letter == '"' and quotechar is None:
                result += read_quote('"')
                # result2 = read_quote('"')
                # result = result2 + result
            elif letter == "'" and quotechar is None:
                result += read_quote("'")
                # result2 = read_quote("'")
                # result = result2 + result
            else:
                result += letter
        return result
    return read_quote()

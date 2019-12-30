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
            l = x[i]
            i += 1
            if l == ' ' and quotechar is not "'":
                result2 = read_quote(quotechar)
                return result2 + ' ' + result
            if l == quotechar:
                return result
            if l == '"' and quotechar is None:
                result += read_quote('"')
            elif l == "'" and quotechar is None:
                result += read_quote("'")
            else:
                result += l
        return result
    return read_quote()


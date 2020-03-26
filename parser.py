keyword = ['if', 'then', 'else', 'begin', 'end']
symbol_table = []

def isSpecial(word):
    return (not((ord(word) > 64 and ord(word) < 91) or (ord(word) > 96 and ord(word) < 123) or (ord(word) > 47 and ord(word)< 58) or (ord(word)==46)))

def hasSpecial(word):
    return (True in (isSpecial(char) for char in word) )

def isValidInt(integer):
    try:
        return (isinstance(int(integer), int))
    except ValueError:
        return False 
    
def isReal(word):
    try:
       return (isinstance(float(word), float))
    except ValueError:
        return False

def addToList(word):
    for symbol in symbol_table:
        if (word['symbol'] == symbol[0]):
            symbol[2] += 1
            return 

    symbol_table.append([word['symbol'], word['token_class'], word['occurance']])

def printSymbolTable():
    print("Symbol table:")
    for symbol in symbol_table:
        if (len(symbol[1]) == 4):
            print ('\tsymbol:' + symbol[0]+ '\tcategory: ' + symbol[1] + "\t" + '\toccurance: '+ str(symbol[2]))
        else:
            print ('\tsymbol:' + symbol[0]+ '\tcategory: ' + symbol[1] + '\toccurance: '+ str(symbol[2]))

def parse(x):
    if (hasSpecial(x) and len(x)>1):
        token = ''
        spe_char = ''

        for i in range(len(x)):
            if (isSpecial(x[i])):
                spe_char += x[i]
                parse(spe_char)
                spe_char = ''
            else:
                token += x[i]
                if (i < len(x)-1):
                    if (isSpecial(x[i+1])):
                        parse(token)
                        token = ''
                else:
                    parse(token)
                    token = ''
    else:
        if (x in keyword):
            addToList({ 'symbol': x, 'token_class': 'keyword', 'occurance': 1})
        elif (hasSpecial(x)):
            addToList({ 'symbol': x, 'token_class': 'special', 'occurance': 1})
        elif (isValidInt(x)):
            addToList({ 'symbol': x, 'token_class': 'integer', 'occurance': 1})
        elif (isReal(x)):
            addToList({ 'symbol': x, 'token_class': 'real', 'occurance': 1})
        else:
            addToList({ 'symbol': x, 'token_class': 'identifier', 'occurance': 1})

#driver code
def main(code):
    for x in code.split(" "):
        parse(x)
    
    printSymbolTable()

code = 'if [ 123 cat ))) then begin if cat x 12+123 + end] cat [ 12.23, end'
main(code)

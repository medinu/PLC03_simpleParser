keyword = ['if', 'then', 'else', 'begin', 'end']

special = list('()[]+-=,;')
digit =list('0123456789')
character = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

symbol_table = []

def isKeyWord(word):
    for key in keyword:
        if (word == key):
            return True
    return False

def isSpecial(word):
    for key in special:
        if (word == key):
            return True
    return False

def hasSpecial(word):
    for char in word:
        if (char in special):
            return True
    return False

def isValidInt(integer):
    try:
        float(integer)
        return True
    except ValueError:
        return False

def isReal(word):
    index = 0
    count = 0
    for i in range(len(word)):
        if (word[i] == '.'):
            count +=1
            index = i

    pre = word[0:index]
    post = word[(index+1):len(word)]

    if (isValidInt(pre) and isValidInt(post) and count == 1):
        return True
    else:
        return False

def addToList(word):
    #if token exists in list flip exists to true
    exists = False
    for symbol in symbol_table:
        if (word['symbol'] == symbol[0]):
            exists = True
            break
    # if word is already in symbol table
    if (exists):
        symbol[2] += 1 
    else: 
        symbol_table.append([word['symbol'], word['token_class'], word['occurance']])

def parse(x):
    if (hasSpecial(x) and len(x)>1):
        token = ''
        spe_char = ''

        for i in range(len(x)):
            if (x[i] in special):
                spe_char += x[i]
                parse(spe_char)
                spe_char = ''
            else:
                token += x[i]
                if (i < len(x)-1):
                    if (x[i+1] in special):
                        parse(token)
                        token = ''

                elif (i+1 == len(x)):
                    parse(token)
                    token = ''
    else:
        if (isKeyWord(x)):
            keyWord = { 'symbol': x, 'token_class': 'keyword', 'occurance': 1}
            addToList(keyWord)
        elif (isSpecial(x)):
            keyWord = { 'symbol': x, 'token_class': 'special', 'occurance': 1}
            addToList(keyWord)
        elif (isValidInt(x)):
            if (isReal(x)):
                keyWord = { 'symbol': x, 'token_class': 'real', 'occurance': 1}
                addToList(keyWord)
            else: 
                keyWord = { 'symbol': x, 'token_class': 'integer', 'occurance': 1}
                addToList(keyWord)
        else:
            keyWord = { 'symbol': x, 'token_class': 'identifier', 'occurance': 1}
            addToList(keyWord)

def printSymbolTable():
    print("Symbol table:")
    for symbol in symbol_table:
        if (len(symbol[1]) == 4):
            print ('\tsymbol:' + symbol[0]+ '\tcategory: ' + symbol[1] + "\t" + '\toccurance: '+ str(symbol[2]))
        else:
            print ('\tsymbol:' + symbol[0]+ '\tcategory: ' + symbol[1] + '\toccurance: '+ str(symbol[2]))

#driver code
def main(code):
    lexeme = code.split(" ")

    for x in lexeme:
        parse(x)

    printSymbolTable()

code = 'if [ 123 cat ))) then begin if cat x 12+123 + end] cat [ 12.23, end'
main(code)
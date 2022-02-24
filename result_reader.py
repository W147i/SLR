# result_reader implements the reading of the result txt files

# returns the list of accepted documents
def ok():
    readfile = open("passed.txt", "r", encoding='utf-8')
    data = readfile.read()
    arrdata = data.split("\n")
    if '' in arrdata:
        arrdata.remove('')
    print("passed")
    print(arrdata)
    print(type(arrdata))
    readfile.close()
    return arrdata

# returns the list of declined documents
def no():
    readfile = open("unclear.txt", "r", encoding='utf-8')
    data = readfile.read()
    arrdata = data.split("\n")
    if '' in arrdata:
        arrdata.remove('')
    print("unclear")
    print(arrdata)
    print(type(arrdata))
    readfile.close()
    return arrdata

# returns the list of documents to be reviewed manually
def maybe():
    readfile = open("declined.txt", "r", encoding='utf-8')
    data = readfile.read()
    arrdata = data.split("\n")
    if '' in arrdata:
        arrdata.remove('')
    print("declined")
    print(arrdata)
    print(type(arrdata))
    readfile.close()
    return arrdata

# returns the list of documents with unsupported formats or languages
def uk():
    readfile = open("unsupported.txt", "r", encoding='utf-8')
    data = readfile.read()
    arrdata = data.split("\n")
    if '' in arrdata:
        arrdata.remove('')
    print("unsupported")
    print(arrdata)
    print(type(arrdata))
    readfile.close()
    return arrdata
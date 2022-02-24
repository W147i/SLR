# used to load and screen pdf files
# sorts in categories "accepted", "unclear", "declined", "unsupported"

import glob
import PyPDF2
import re

def screen():
    # search for pdf files in designated folder
    pdflist = glob.glob("pdf/*.pdf")
    print(pdflist)

    # for testing
    total = len(pdflist)
    current = 0

    # lists for end results
    passed = []
    unclear = []
    declined = []
    unsupported = []

    for item in pdflist:
        # for testing
        current += 1
        msg = str(current) + "/" + str(total)
        print(msg)
        print(item)

        # open current file, only first page selected
        pdfFileObj = open(item, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        pageObj = pdfReader.getPage(0)
        text=(pageObj.extractText())
        
        # language/format check
        words0=['the']
        word_exp0='|'.join(words0)
        found0 = re.findall(word_exp0,text,re.M)

        if len(found0) > 0:
            # search for separate term groups
            words1=['quantum computing','quantum computer','quantum computation', 'quantumcomputing', 'quantumcomputer', 'quantumcomputation', 'quantum algorithm', 'quantumalgorithm']
            words2=['differential equation', 'wave equation', 'poisson equation', 'differentialequation', 'waveequation', 'poissonequation']
            word_exp1='|'.join(words1)
            word_exp2='|'.join(words2)
            found1 = re.findall(word_exp1,text,re.M)
            found2 = re.findall(word_exp2,text,re.M)
            # print(found1)
            # print(found2)

            # evaluate by the results obtained
            if len(found1) > 0 :
                if len(found2) > 0:
                    passed.append(item)
                else:
                    unclear.append(item)
            else:
                if len(found2) > 0:
                    unclear.append(item)
                else:
                    declined.append(item)
            pdfFileObj.close()
        
        else:
            unsupported.append(item)

    # for testing
    print("")
    print("The following documents have passed")
    print(passed)
    print("The following documents are not classified yet")
    print(unclear)
    print("The following documents been declined")
    print(declined)
    print("The following documents have unsupported languages or formats")
    print(unsupported)

    # new temporary lists for second evaluation steps
    passed1 = []
    unclear1 = []
    declined1 = []

    # for testing
    total = len(unclear)
    current = 0

    for item in unclear:
        # for testing
        current += 1
        msg
        print(str(current) + "/" + str(total))
        print(item)

        # read current file
        pdfFileObj = open(item, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        pagecount = pdfReader.numPages

        found1 = []
        found2 = []

        for page in range(1,pagecount):
            # load file
            pageObj = pdfReader.getPage(page)
            text=(pageObj.extractText())

            # search for same term groups in whole dodument
            words1=['quantum computing','quantum computer','quantum computation', 'quantumcomputing', 'quantumcomputer', 'quantumcomputation', 'quantum algorithm', 'quantumalgorithm']
            words2=['differential equation', 'wave equation', 'poisson equation', 'differentialequation', 'waveequation', 'poissonequation']
            word_exp1='|'.join(words1)
            word_exp2='|'.join(words2)
            tmp1 = re.findall(word_exp1,text,re.M)
            tmp2 = re.findall(word_exp2,text,re.M)

            # evaluate by the results obtained
            for entry in tmp1:
                if entry not in found1:
                    found1.append(entry)
            for entry in tmp2:
                if entry not in found2:
                    found2.append(entry)

        # print("")
        # print("In the complete document " + item)
        # print(found1)
        # print(found2)

        # evaluate again with the new results
        if len(found1) > 0 :
            if len(found2) > 0:
                passed.append(item)
                passed1.append(item)
            else:
                unclear1.append(item)
        else:
            if len(found2) > 0:
                unclear1.append(item)
            else:
                declined.append(item)
                declined1.append(item)
        pdfFileObj.close()

    unclear = unclear1

    # for testing
    print("")
    print("The following documents have passed in second iteration")
    print(passed1)
    print("The following documents have to be classified manufally")
    print(unclear1)
    print("The following documents been declined in second iteration")
    print(declined1)

    # for testing
    print("")
    print("The total result of content checking is:")
    print("The following documents have passed")
    print(passed)
    print("The following documents have to be classified manufally")
    print(unclear)
    print("The following documents been declined")
    print(declined)
    print("The following documents have unsupported languages or formats")
    print(unsupported)

    # saves the results in designated files to be readable on their own
    statefile = open("passed.txt", "w", encoding='utf-8')
    for item in passed:
        statefile.write(item)
        statefile.write("\n")
    statefile.close()

    statefile = open("unclear.txt", "w", encoding='utf-8')
    for item in unclear:
        statefile.write(item)
        statefile.write("\n")
    statefile.close()

    statefile = open("declined.txt", "w", encoding='utf-8')
    for item in declined:
        statefile.write(item)
        statefile.write("\n")
    statefile.close()

    statefile = open("unsupported.txt", "w", encoding='utf-8')
    for item in unsupported:
        statefile.write(item)
        statefile.write("\n")
    statefile.close()

    # for testing
    readfile = open("passed.txt", "r", encoding='utf-8')
    data = readfile.read()
    arrdata = data.split("\n")
    if '' in arrdata:
        arrdata.remove('')
    print("passed")
    print(arrdata)
    print(type(arrdata))
    readfile.close()

    readfile = open("unclear.txt", "r", encoding='utf-8')
    data = readfile.read()
    arrdata = data.split("\n")
    if '' in arrdata:
        arrdata.remove('')
    print("unclear")
    print(arrdata)
    print(type(arrdata))
    readfile.close()

    readfile = open("declined.txt", "r", encoding='utf-8')
    data = readfile.read()
    arrdata = data.split("\n")
    if '' in arrdata:
        arrdata.remove('')
    print("declined")
    print(arrdata)
    print(type(arrdata))
    readfile.close()

    readfile = open("unsupported.txt", "r", encoding='utf-8')
    data = readfile.read()
    arrdata = data.split("\n")
    if '' in arrdata:
        arrdata.remove('')
    print("unsupported")
    print(arrdata)
    print(type(arrdata))
    readfile.close()
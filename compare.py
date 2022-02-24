# only used to compare the results of the tool with the results of my personal study
# no general use
# can be used to reproduce my results
import glob

readfile = open("myResults/passed.txt", "r", encoding='utf-8')
data = readfile.read()
arrdata = data.split("\n")
if '' in arrdata:
    arrdata.remove('')
# print("passed")
readfile.close()

#for item in arrdata:
#    print(item)

pdflist = glob.glob("myResults/*.pdf")

# for testing
total = len(pdflist)
current = 0

# lists for end results
same = 0
different = 0
print(same)

for item in pdflist:
    item1 = item.replace("myResults\\", "")

    # for testing
    current += 1
    msg = str(current) + "/" + str(total)
    # print(msg)

    tmp_item = "pdf\\" + item1
    #print(tmp_item)

    if tmp_item in arrdata:
        same += 1
        print(same)
        print(tmp_item)
    else:
        different += 1

print("For the accepted documents")
print("files corresponding: ")
print(str(same))
print("files different: ")
print(str(different))
print("")

readfile = open("myResults/unclear.txt", "r", encoding='utf-8')
data = readfile.read()
arrdata = data.split("\n")
if '' in arrdata:
    arrdata.remove('')
#print("passed")
readfile.close()

#for item in arrdata:
#    print(item)

same = 0
different = 0
print(same)

for item in pdflist:
    item1 = item.replace("myResults\\", "")

    # for testing
    current += 1
    msg = str(current) + "/" + str(total)
    # print(msg)

    tmp_item = "pdf\\" + item1
    #print(tmp_item)

    if tmp_item in arrdata:
        same += 1
        print(same)
        print(tmp_item)
    else:
        different += 1

print("For the documents to be reviewed")
print("files corresponding: ")
print(str(same))
print("files different: ")
print(str(different))
print("")

readfile = open("myResults/unsupported.txt", "r", encoding='utf-8')
data = readfile.read()
arrdata = data.split("\n")
if '' in arrdata:
    arrdata.remove('')
#print("passed")
readfile.close()

#for item in arrdata:
#    print(item)

same = 0
different = 0
print(same)

for item in pdflist:
    item1 = item.replace("myResults\\", "")

    # for testing
    current += 1
    msg = str(current) + "/" + str(total)
    #print(msg)

    tmp_item = "pdf\\" + item1
    #print(tmp_item)

    if tmp_item in arrdata:
        same += 1
        print(same)
        print(tmp_item)
    else:
        different += 1

print("For the unsupported documents")
print("files corresponding: ")
print(str(same))
print("files different: ")
print(str(different))
print("")

readfile = open("myResults/declined.txt", "r", encoding='utf-8')
data = readfile.read()
arrdata = data.split("\n")
if '' in arrdata:
    arrdata.remove('')
#print("passed")
readfile.close()

#for item in arrdata:
#    print(item)

same = 0
different = 0
print(same)

for item in pdflist:
    item1 = item.replace("myResults\\", "")

    # for testing
    current += 1
    msg = str(current) + "/" + str(total)
    #print(msg)

    tmp_item = "pdf\\" + item1
    #print(tmp_item)

    if tmp_item in arrdata:
        same += 1
        print(same)
        print(tmp_item)
    else:
        different += 1

print("For the declined documents")
print("files corresponding: ")
print(str(same))
print("files different: ")
print(str(different))
print("")
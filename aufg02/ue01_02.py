
# FUNCTIONS
def most30words(fileurl, stopwords):
    """returns the 30 most appearing words in a text from a given file url.
       Filtered out stopwords if param is set to True"""

    #get stopwords
    stoplist = []
    if stopwords:
        stopwords = open("stopwords.txt", 'r').read()
        stoplist = stopwords.split()

    #get text from file
    text = open(fileurl, 'r').read()

    #lowercase
    text = text.lower()

    # split string at spaces
    textlist = text.split()
    wordcount = len(textlist)
    #print(textlist)

    # count occurrences in dictionary
    textdict = {}
    for x in textlist:
        
        #ignore words that appear in stoplist
        if (x not in stoplist):
            if (textdict.get(x, -1)) > 0:
                textdict.update({x: (textdict.get(x)+1)})
            else:
                textdict.setdefault(x, 1)
            
    # create a sorted list from elements in dictionary
    result = sorted(textdict.items(), key=lambda x: x[1], reverse=True)
    #
    #print(result[:30])

    # add percantage to word list
    endlist = list()
    for word in result[:30]:
        temp = list(word)
        temp.append(temp[1]/wordcount)
        endlist.append(temp)

    return endlist



def countWords(fileurl):
    """returns the wordcount from a given file url"""
    
    text = open(fileurl, 'r').read()

    # split string at spaces
    textlist = text.split()
    return str(len(textlist))
    

def makeTable(url1, url2, stopwords):
    """Takes two file urls and creates a table,
       comparing the 30 most used words of the text files.
       stopwords is True/False, if stopwords should be considered"""
    list1 = most30words(url1, stopwords)
    list2 = most30words(url2, stopwords)

    print("Considered stopwords: " + str(stopwords))
    print("-------------------------------------------------------")
    print(url1 + "\t|| " + url2)
    print("Total words: " + countWords(url1) + "\t|| " + "Total words: " +countWords(url2))
    print("-------------------------------------------------------")
    print("Word\tAbs.\tPerc.\t||\tWord\tAbs.\tPerc.\t")
    print("-------------------------------------------------------")      

    i = 0
    while i<len(list1):
        print(list1[i][0]+"\t" + str(list1[i][1])+"\t" + str(round(list1[i][2], 5))+"\t||\t"
              + list2[i][0]+"\t" + str(list2[i][1])+"\t" + str(round(list2[i][2], 5)))
        
        i = i+1

    print("-------------------------------------------------------")



#--------------------------------------
#MAIN BODY

makeTable("frankenstein.txt", "samsa.txt", False)
print()
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
print()
makeTable("frankenstein.txt", "samsa.txt", True)




    





#Wait for user input to stop program
input("Press <ENTER> to continue")

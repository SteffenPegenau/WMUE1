
# FUNCTIONS
def charcounter(fileurl, charpairs):
    """returns the numbers of chars in a text from a given file url."""


    #get text from file, transform to lowercase
    text = open(fileurl, 'r').read().lower()

    # split string into list of chars
    charlist = list(text)
    charnumber = len(charlist)
    


    #count occurrences in dictionary
    #remember lastchar for finding charpairs
    lastchar = ""
    chardict = {}
    for char in charlist:
        
        #transform escape sequences
        if char == "\n":
            char = r"\n"

        if charpairs:
            #only pairs of chars shall be considered
            if lastchar == char:
                #a pair is found. Add to dictionary
                if (chardict.get(char+char, -1)) > 0:
                    chardict.update({char+char: (chardict.get(char+char)+1)})
                else:
                    chardict.setdefault(char+char, 1)
            #else:
                #no charpair. Do nothing and continue through list

            #update lastchar
            lastchar = char
                
                
        else:
            #pairs of chars shall not be considered
            if (chardict.get(char, -1)) > 0:
                chardict.update({char: (chardict.get(char)+1)})
            else:
                chardict.setdefault(char, 1)
            
    # create a sorted list from elements in dictionary
    result = sorted(chardict.items(), key=lambda x: x[1], reverse=True)
    #print("Listenlänge: " + str(len(result)))
    
    #print(result[:30])

    # add percantage to char list
    endlist = list()
    for char in result[:30]:
        temp = list(char)
        temp.append(temp[1]/charnumber)
        endlist.append(temp)

    return endlist



def countChars(fileurl):
    """returns the charcount from a given file url"""
    
    text = open(fileurl, 'r').read()

    # split string at spaces
    charlist = list(text)
    return str(len(charlist))
    

def makeTable(url1, url2, charpairs):
    """Takes two file urls and creates a table,
       comparing the 30 most used words of the text files.
       charpairs is True/False, if only charpairs should be considered"""
    list1 = charcounter(url1, charpairs)
    list2 = charcounter(url2, charpairs)

    print("Charpairs considered: " + str(charpairs))
    print("-------------------------------------------------------")
    print(url1 + "\t|| " + url2)
    print("Total chars: " + countChars(url1) + "\t|| " + "Total chars: " +countChars(url2))
    print("-------------------------------------------------------")
    print("Char\tAbs.\tPerc.\t||\tChar\tAbs.\tPerc.\t")
    print("-------------------------------------------------------")      

    i = 0
    while i<len(list1) and i<len(list2):
        print(list1[i][0]+"\t" + str(list1[i][1])+"\t" + str(round(list1[i][2], 5))+"\t||\t"
              + list2[i][0]+"\t" + str(list2[i][1])+"\t" + str(round(list2[i][2], 5)))
        
        i = i+1

    print("-------------------------------------------------------")



#--------------------------------------
#MAIN BODY

makeTable("samsa_german.txt", "samsa.txt", True)





    





#Wait for user input to stop program
input("Press <ENTER> to continue")

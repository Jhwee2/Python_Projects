class fileStrip:
    def readfile(self,filename):
        with open(filename,'r', encoding="utf8") as f:
            print(f.read())
    
    def removeSpecial(self,filename):
        removal = [".","?","!",",",";",":","-","[","]","{","}","'",'“','”','"',"(",")","’","*"]
        with open(filename,'r', encoding="utf8") as f:
            book = f.read().strip()
            rebuild = ""
            for char in book:
                if char in removal:
                    rebuild += ""
                else:
                    rebuild += char
            return rebuild

    def lowercaseBook(self,filename):
        with open(filename,'r', encoding="utf8") as f:
            print(f.read().lower())

    def totalWords(self,nonSpecialFile):
        splitBook = nonSpecialFile.splitlines()
        rebuild = ""
        for lines in splitBook:
            rebuild += lines.lower() + " "
        lst = rebuild.strip().split(" ")
        moddedFile = [string for string in lst if string != ""]
        return moddedFile

    def uniqueFreq(self,modifiedFile):
        dict = {}
        dict2 = {}
        lst = modifiedFile
        for item in lst:
            if item not in dict:
                dict[item] = 1
            elif item in dict:
                dict[item] += 1
        for key,value in dict.items():
            if value == 1:
                dict2[key] = value
        return dict2
    
    def uniqueCount(self,dict):
        print("Total # of unique words:", len(dict))
    
    def hundredFrequent(self,modifiedFile):
        lst = modifiedFile
        dict = {}
        for item in lst:
            if item not in dict:
                dict[item] = 1
            elif item in dict:
                dict[item] += 1      
        sorted_dict = {}
        sorted_keys = sorted(dict, key=dict.get,reverse=True)
        for w in sorted_keys:
            sorted_dict[w] = dict[w]
        print(sorted_dict)

    def uniqueHundredFrequent(self,modifiedFile):
        lst = modifiedFile
        dict = {}
        for item in lst:
            if item not in dict:
                dict[item] = 1
            elif item in dict:
                dict[item] += 1      
        sorted_dict = {}
        sorted_keys = sorted(dict, key=dict.get,reverse=True)
        removal = ["a", "an", "the", "in", "up", "on", "for", "by", "of", "under", "onto", "into", "and", "or", "if", "whether", "why", "what", "who", "whom", "where", "which"]
        for w in sorted_keys:
            if w not in removal:
                sorted_dict[w] = dict[w]
        print(sorted_dict)

X = fileStrip()
name = "C:/Users/Jared Hwee/VsCodeProjects/FileStrip/book.txt" #Change based on your file path
moddedFile = X.totalWords(X.removeSpecial(name))

#X.readfile(name) #2.1. Read the downloaded and updated txt file with no header information
#print(X.removeSpecial(name)) #2.2. Strip whitespace & punctuation from the words
#X.lowercaseBook(name) # 2.3. Convert all the words to lowercase 
#print("Total # of words:", len(moddedFile)) #2.4. Output the total number of words in the book (can include **repeat** words)
#print(X.uniqueFreq(moddedFile)) #2.5. Create a dictionary with all the **unique** words in the book, along with their frequencies (each word is a key, each frequency is a value)
X.uniqueCount((X.uniqueFreq(moddedFile))) #2.6. Output the number of **unique** words used in the book
#X.hundredFrequent(moddedFile) #2.7. Output the 100 most frequently used words in the book and their frequencies, with the frequencies sorted in descending order *(see Think Python textbook, 2nd edition, chapter 13, for reference on how to do 2.4 - 2.7)*
#X.uniqueHundredFrequent(moddedFile) #2.8. Output the 100 most frequently used words in the book and their frequencies, with the frequencies sorted in descending order, excluding the following words: 
                                     #a, an, the, in, up, on, for, by, of, under, onto, into, and, or, if, whether, why, what, who, whom, where, which

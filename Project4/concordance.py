from hash_quad import *
import string

class Concordance:

    def __init__(self):
        self.stop_table = HashTable(191)          # hash table for stop words
        self.concordance_table = HashTable(191)   # hash table for concordance

    def load_stop_table(self, filename):
        """ Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
        Starting size of hash table should be 191: self.stop_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        try:
            file=open(filename,'r')
        except:
            raise FileNotFoundError
        stop_words=file.readlines()
        for line_num in range(len(stop_words)):
            self.stop_table.insert(stop_words[line_num].strip(),0)
        file.close()


    def load_concordance_table(self, filename):
        """ Read words from input text file (filename) and insert them into the concordance hash table, 
        after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)
        Starting size of hash table should be 191: self.concordance_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        try:
            file=open(filename,'r')
        except:
            raise FileNotFoundError
        words_list=file.readlines()
        for line_num in range(len(words_list)):
            words_list[line_num]=words_list[line_num].strip()
            filtered_line=self.remove_punc(words_list[line_num])
            for just_word in filtered_line.split():
                if self.is_number(just_word):
                    continue
                else:
                    self.concordance_table.insert(just_word,line_num+1)
        for index in range(len(self.concordance_table.hash_table)):
            if self.concordance_table.hash_table[index]!=None:
                temp=set(self.concordance_table.hash_table[index][1])
                sort_temp=list(temp)
                sort_temp.sort()
                key=self.concordance_table.hash_table[index][0]
                self.concordance_table.hash_table[index]=(key,sort_temp)
        file.close()

    def remove_punc(self,sentence):
        new=sentence
        for char in sentence:
            if char== '-':
                new=new.replace(char,' ')
            if char in string.punctuation:
                new=new.replace(char,'')
        return new.lower()

    def is_number(self,num):
        try:
            float(num)
            return True
        except ValueError:
            return False



    def write_concordance(self, filename):
        """ Write the concordance entries to the output file(filename)
        See sample output files for format."""
        outfile=open(filename,'w')
        tuple_list=[]
        string=''
        for item in self.concordance_table.hash_table:
            if item !=None:
                #tuple_list.append((item[0].lower(),item[1]))
                temp = (item[0].lower(), [0])
                # if temp in self.stop_table.hash_table:
                #     tuple_list.remove(tuple_list[index])
                if temp in self.stop_table.hash_table:
                    # replaces the stop words with 0 in the list
                    item = 0
                tuple_list.append(item)

        tuple_list = list(filter(lambda a: a != 0, tuple_list))
        tuple_list.sort()
        #now it's only the words we want
        for pairs in tuple_list:
            temp=''
            for nums in pairs[1]:
                temp+=str(nums)+' '
            nums=temp.strip()
            string+= pairs[0].lower()+": "+nums+'\n'
        final=string.strip()
        outfile.write(final)
        outfile.close()


#con=Concordance()
# con.load_stop_table("stop_words.txt")
# print(con.stop_table)
#con.load_concordance_table("dupe.txt")
#print(con.concordance_table.get_all_keys())
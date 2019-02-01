class HashTable:

    def __init__(self, table_size=191):         # can add additional attributes
        self.table_size = table_size        # initial table size
        self.hash_table = [None]*table_size # hash table
        self.num_items = 0                  # empty hash table

    def insert(self, key, value):
        """ Inserts an entry into the hash table (using Horner hash function to determine index, 
        and quadratic probing to resolve collisions).
        The key is a string (a word) to be entered, and value is the line number that the word appears on. 
        If the key is not already in the table, then the key is inserted, and the value is used as the first 
        line number in the list of line numbers. If the key is in the table, then the value is appended to that 
        key’s list of line numbers. If value is not used for a particular hash table (e.g. the stop words hash table),
        can use the default of 0 for value and just call the insert function with the key.
        If load factor is greater than 0.5 after an insertion, hash table size should be increased (doubled + 1)."""


        i = 0
        hash_val = self.horner_hash(key)
        # quadratic probing
        while self.hash_table[hash_val + i ** 2] and self.hash_table[hash_val + i ** 2][0] != key:
            i += 1
            if hash_val + i ** 2 >= self.table_size:
                hash_val -= self.table_size

        if self.hash_table[hash_val+i**2]==None and type(value) is not list:
            self.hash_table[hash_val + i ** 2] = (key, [value])
            self.num_items+=1
        elif self.hash_table[hash_val+i**2]==None and type(value) is list:
            self.hash_table[hash_val + i ** 2] = (key, value)
            self.num_items+=1
        elif self.hash_table[hash_val + i ** 2][0] == key:
            self.hash_table[hash_val + i ** 2][1].append(value)
        if self.get_load_factor()>0.5:
            self.rehash()


    def quad_probe_i(self,key):
        i = 0
        hash_val = self.horner_hash(key)
        # quadratic probing
        while self.hash_table[hash_val + i ** 2] and self.hash_table[hash_val + i ** 2][0] != key:
            i += 1
            if hash_val + i ** 2 >= self.table_size:
                hash_val -= self.table_size
        return hash_val+i**2


    def rehash(self):
        oldtable=self.hash_table
        newtable_size=self.table_size*2+1
        self.hash_table=[None]*newtable_size
        self.table_size=newtable_size
        self.num_items=0
        for item in oldtable:
            if item==None:
                continue
            else:
                self.insert(item[0],item[1])


    def horner_hash(self, key):
        """ Compute and return an integer from 0 to the (size of the hash table) - 1
        Compute the hash value by using Horner’s rule, as described in project specification."""
        n=min(len(key),8)
        hash=0
        for i in range(n):
            hash+= ord(key[i])*31**(n-1-i)
        return hash%self.table_size

    def in_table(self, key):
        """ Returns True if key is in an entry of the hash table, False otherwise."""
        i=self.quad_probe_i(key)
        if self.hash_table[i]!=None:
            if self.hash_table[i][0]==key:
                return True
        return False

    def get_index(self, key):
        """ Returns the index of the hash table entry containing the provided key. 
        If there is not an entry with the provided key, returns None."""
        if not self.in_table(key):
            return None
        else:
            i = self.quad_probe_i(key)
            if self.hash_table[i] != None:
                if self.hash_table[i][0] == key:
                    return i


    def get_all_keys(self):
        """ Returns a Python list of all keys in the hash table."""
        keys=[]
        for item in self.hash_table:
            if item!=None:
                keys.append(item[0])
        return keys


    def get_value(self, key):
        """ Returns the value (list of line numbers) associated with the key. 
        If key is not in hash table, returns None."""
        if not self.in_table(key):
            return None
        i = self.quad_probe_i(key)
        if self.hash_table[i] != None:
            if self.hash_table[i][0] == key:
                return self.hash_table[i][1]

    def get_num_items(self):
        """ Returns the number of entries (words) in the table."""
        return self.num_items

    def get_table_size(self):
        """ Returns the size of the hash table."""
        return self.table_size

    def get_load_factor(self):
        """ Returns the load factor of the hash table (entries / table_size)."""
        return (self.num_items/self.table_size)

    #def __repr__(self):
        #return "Table: {}".format(self.hash_table)
#ht=HashTable(7)
#print(ht.horner_hash("cyy"))

# import time
# x=open("the.txt")
# test=HashTable()
# l=x.readlines()
# start=time.time()
# for line in range(len(l)):
#     test.insert(l[line],line)
# end=time.time()
# print(end-start)
# print(test.hash_table)
# x.close()

import sys
import csv
import array as arr
import math


"The operations for numbers in binary are explained in the README file."

class BitArray:
    def __init__(self, size):
        self.size = size
        self.array = 0

    def getitem(self, index):
        return (self.array & (1 << index)) != 0

    def setitem(self, index, value):
        if value:
            self.array |= (1 << index)
        else:
            self.array &= ~(1 << index)

    def size(self):
        return self.size

class BloomFilter(object):
    def __init__(self, elements, prob):
        #n is the number of elements in the DataBase
        self.n = elements
        #p is the probability that a false positive will occur
        self.p = prob
        #m is the size of the bit array
        self.m = int(math.ceil((self.n * math.log(self.p)) / math.log(1 / pow(2, math.log(2)))));
        #k is the number of hash functions
        self.k = int(round((self.m / self.n) * math.log(2)));
        #bitArray is an array with true and false values
        self.bitArray = BitArray(self.m)
        
        """   
        Since I couldn't use the mmh3 library and use its hash function with
        different seeds, I had to implement it in another way. I used the default
        hash function of python, for each element that is added an iterator
        variable is concatenated in each iteration of a for loop with a range
        of the number of hashes function calculated to calculate diferents hashes.
    
        element: weseGLCIEPTUusDlU@aol.com
        first hash: weseGLCIEPTUusDlU@aol.com0
        second hash: weseGLCIEPTUusDlU@aol.com1
        ....
        last hash: weseGLCIEPTUusDlU@aol.com(self.k-1)
        """
    
    
    
    def add(self, element):
        """Hashes the element k times and updates the
        computed index values of the bitArray to true.

        Parameters:
        element (string): is the element to add
    
        Returns:
    
       """
        for i in range(self.k):
            hash_ = hash(element+str(i)) % self.m
            self.bitArray.setitem(hash_, 1)
            
    def check(self, element):
        """Hashes the element k times and checks if
        the computed index values of bitArray are all true.

        Parameters:
        element (string): is the element to check
    
        Returns: Returns true if all the values of the
        calculated indices are true; otherwise, it returns false.
    
       """
        for i in range(self.k):
            hash_ = hash(element+str(i)) % self.m
            if self.bitArray.getitem(hash_) == 0:
                return False
        return True


def readCsv(path):
    """Reads the information from an excel file and returns it as a list.
    
        Parameters:
        path (string): is the path of the file to analyze
    
        Returns: returns a list in which each element is a row from the excel file.
    
    """
    rows = []
    with open(path, 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            if "@" in row[0]:
                rows.append(row[0])
    return rows
    

def main():
    if len(sys.argv):
        dataBase = readCsv(sys.argv[1])
        searches = readCsv(sys.argv[2])
        
        n = len(dataBase)
        p = 1 * 10 ** -7
        bf = BloomFilter(n,p)
        
        for e in dataBase:
            bf.add(e)
        for e in searches:
            if bf.check(e) and e in dataBase:
                print(e + "," + "Probably in the DB")
            elif not bf.check(e) and e not in dataBase:
                print(e + "," + "Not in the DB")
            elif bf.check(e) and e not in dataBase:
                print(e + "," + "False positive")
        
            
    

main()
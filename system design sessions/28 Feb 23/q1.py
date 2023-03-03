# Bloom filter


"""
HashFunction  
Filter   
DataStructure 


DB1 -> Gautham   -> HF(Gautham) = 10010 = 0000000000010010
DB2 -> Sahil     -> HF(Sahil)   = 11100 = 0000000000011100


"""




class HashFunction:
    def __init__(self):
        pass
    def getHash(self, data):
        pass

class BFDataStructure:
    def __init__(self):
        pass
    def addDataHash(self, hash)-> None:
        pass
    def searchHash(self, hash) -> bool:
        pass 

class Filter:
    def __init__(self, hashFunction, bfDataStructure):
        self.hf = hashFunction
        self.filter_data_structure = bfDataStructure
    
    def add(self, data):
        pass
    def search(self, data):
        pass

class HF5(HashFunction):
    def __init__(self):
        pass
    def getHash(self, data):
        pass

class BitWiseDataStr(BFDataStructure):
    def __init__(self):
        pass
    def addDataHash(self, hash) -> None:
        pass
    def searchHash(self, hash) -> bool:
        pass

class SingleBloomFilter(Filter):
    def add(self, data):
        hash = self.hf(data)
        # to trim to size 
        self.filter_data_structure(hash)
    def search(self, data):
        hash = self.hf(data)
        return self.filter_data_structure.search(hash)
   
class MultiBloomFilter(Filter):
    def __init__(self,hashFunctions, bfDataStructure):
        self.hf = hashFunctions
        self.filter_data_structure = bfDataStructure

    def add(self, data):
        hash = data
        
        for hash_function in self.hf:
            hash = hash_function.getHash(hash)
        # to trim to size 
        self.filter_data_structure(hash)
    def search(self, data):
        for hash_function in self.hf:
            hash = hash_function.getHash(hash)
        return self.filter_data_structure.search(hash)


if __name__ == "__main__":
    hf5_function = HF5()
    bf_bitwise_structure = BitWiseDataStr()
    Bloomfilter = SingleBloomFilter(hf5_function, bf_bitwise_structure)
    MlBloomfilter = MultiBloomFilter([hf5_function, hf5_function], bf_bitwise_structure)

    MlBloomfilter.add("Gautham")
    MlBloomfilter.add("Sahil")

    MlBloomfilter.search("Prompt")  # => False
    MlBloomfilter.search("Gautham") # => True

# Bloom filter
"""
I possibly say it's true if I have it 
but if I don't have it I'm sure I don't have it 

hash_function -> this return just number, 
    - less collision, within limits 
    - [0,10^9]
            - 100/64 -> x ,  , 10000000/64-> x 

search 1000/64-> x
        999/64-> x-1 -> 0 
    - [64]
        setting bit to 1 in  -> x 
"""

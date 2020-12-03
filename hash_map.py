# Course: CS261 - Data Structures
# Assignment: 5
# Student: Na Kim
# Description: This written program will implement a HashMap class through the following
# methods: put,get,remove,contains_key,clear,empty_buckets,resize_table,table_load,and
# get_keys.


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


def hash_function_1(key: str) -> int:
    """
    Sample Hash function #1 to be used with A5 HashMap implementation
    DO NOT CHANGE THIS FUNCTION IN ANY WAY
    """
    hash = 0
    for letter in key:
        hash += ord(letter)
    return hash


def hash_function_2(key: str) -> int:
    """
    Sample Hash function #2 to be used with A5 HashMap implementation
    DO NOT CHANGE THIS FUNCTION IN ANY WAY
    """
    hash, index = 0, 0
    index = 0
    for letter in key:
        hash += (index + 1) * ord(letter)
        index += 1
    return hash


class HashMap:
    def __init__(self, capacity: int, function) -> None:
        """
        Init new HashMap based on DA with SLL for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.buckets = DynamicArray()
        for _ in range(capacity):
            self.buckets.append(LinkedList())
        self.capacity = capacity
        self.hash_function = function
        self.size = 0

    def __str__(self) -> str:
        """
        Return content of hash map t in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = ''
        for i in range(self.buckets.length()):
            list = self.buckets.get_at_index(i)
            out += str(i) + ': ' + str(list) + '\n'
        return out

    def clear(self) -> None:
        """
        this function will clear the content of the hash map without changing the capacity
        """
        for i in range(self.capacity):
            self.buckets[i] = LinkedList()
        # update and set size to 0 to clear content of the hash map
        self.size = 0


    def get(self, key: str) -> object:
        """
        this function will return the value associated with the given key
        """
        hash = self.hash_function(key)
        hash_index = hash % self.capacity
        val = self.buckets.get_at_index(hash_index).contains(key)

        # if the key is not in the hashmap, return None
        if self.buckets.get_at_index(hash_index).length() == 0:
            return None
        if val:
            return val.value
        else:
            return None

    def put(self, key: str, value: object) -> None:
        """
        this function will update the key/value pair in the hash map
        """
        hash = self.hash_function(key)
        hash_index = hash % self.capacity

        # if given key already exists in hash map
        if self.buckets.get_at_index(hash_index).contains(key):
            # remove associated value
            self.buckets.get_at_index(hash_index).remove(key)
            # replace old value with new value
            self.buckets.get_at_index(hash_index).insert(key,value)

        # if given key is not in the hash map
        elif self.buckets.get_at_index(hash_index).contains(key) is None:
            # add new key/value
            self.buckets.get_at_index(hash_index).insert(key,value)
            # add new key to overall count/size
            self.size +=1


    def remove(self, key: str) -> None:
        """
        this function removes given key and its associated value from the hashmap
        """
        hash = self.hash_function(key)
        hash_index = hash % self.capacity
        val = self.buckets.get_at_index(hash_index)

        if val.remove(key):
            self.size -=1


    def contains_key(self, key: str) -> bool:
        """
        this function checks to see if given key is in the hash map
        """
        hash = self.hash_function(key)
        hash_index = hash % self.capacity

        # if the hash map is empty and does not contain any keys
        if self.buckets.length() == 0:
            return False
        # if the given key is not in the hash map, return False
        if self.buckets.get_at_index(hash_index).contains(key) is None:
            return False
        # if the given key is in the hash map, return True
        elif self.buckets.get_at_index(hash_index).contains(key):
            return True

    def empty_buckets(self) -> int:
        """
        this function will return the number of empty buckets in the hash table
        """
        count = 0
        for i in range(self.buckets.length()):
            if self.buckets.get_at_index(i).length() == 0:
                count +=1
        return count

    def table_load(self) -> float:
        """
        this function will return the current hash table load factor
        """
        # load factor of hash table is calculated by (total # of elements stored) / ( number of buckets)
        return self.size / self.capacity


    def resize_table(self, new_capacity: int) -> None:
        """
        this function will change the capacity of the internal hash table
        """
        # if the new_capacity is less than 1, return and method should not do anything
        if new_capacity < 1:
            return
        # initialize new dynamic array and linkedlist
        new_val = DynamicArray()
        for temp in range(new_capacity):
            new_val.append(LinkedList())
        # takes keys and inserts into linkedlist
        for i in range(0,self.capacity):
            for index in self.buckets.get_at_index(i):
                if index != None:
                    hash = self.hash_function(index.key)
                    hash_index = hash % new_capacity
                    new_val.get_at_index(hash_index).insert(index.key,index.value) # insert into new dynamic array

        # update capacity and buckets
        self.capacity = new_capacity
        self.buckets = new_val
        return


    def get_keys(self) -> DynamicArray:
        """
        this function will return a Dynamic Array that contains the keys stored in the hash map
        """
        # set up Dynamic Array
        return_val = DynamicArray()

        # iterates through loop and stores key values
        for i in range(self.capacity):
            val = self.buckets.get_at_index(i)
            for index in val: # append key to new dynamic array
                return_val.append(index.key)
        # returns values of keys
        return return_val


# BASIC TESTING
if __name__ == "__main__":

    print("\nPDF - empty_buckets example 1")
    print("-----------------------------")
    m = HashMap(100, hash_function_1)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key1', 10)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key2', 20)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key1', 30)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key4', 40)
    print(m.empty_buckets(), m.size, m.capacity)


    print("\nPDF - empty_buckets example 2")
    print("-----------------------------")
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('key' + str(i), i * 100)
        if i % 30 == 0:
            print(m.empty_buckets(), m.size, m.capacity)


    print("\nPDF - table_load example 1")
    print("--------------------------")
    m = HashMap(100, hash_function_1)
    print(m.table_load())
    m.put('key1', 10)
    print(m.table_load())
    m.put('key2', 20)
    print(m.table_load())
    m.put('key1', 30)
    print(m.table_load())


    print("\nPDF - table_load example 2")
    print("--------------------------")
    m = HashMap(50, hash_function_1)
    for i in range(50):
        m.put('key' + str(i), i * 100)
        if i % 10 == 0:
            print(m.table_load(), m.size, m.capacity)

    print("\nPDF - clear example 1")
    print("---------------------")
    m = HashMap(100, hash_function_1)
    print(m.size, m.capacity)
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key1', 30)
    print(m.size, m.capacity)
    m.clear()
    print(m.size, m.capacity)


    print("\nPDF - clear example 2")
    print("---------------------")
    m = HashMap(50, hash_function_1)
    print(m.size, m.capacity)
    m.put('key1', 10)
    print(m.size, m.capacity)
    m.put('key2', 20)
    print(m.size, m.capacity)
    m.resize_table(100)
    print(m.size, m.capacity)
    m.clear()
    print(m.size, m.capacity)


    print("\nPDF - put example 1")
    print("-------------------")
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('str' + str(i), i * 100)
        if i % 25 == 24:
            print(m.empty_buckets(), m.table_load(), m.size, m.capacity)


    print("\nPDF - put example 2")
    print("-------------------")
    m = HashMap(40, hash_function_2)
    for i in range(50):
        m.put('str' + str(i // 3), i * 100)
        if i % 10 == 9:
            print(m.empty_buckets(), m.table_load(), m.size, m.capacity)


    print("\nPDF - contains_key example 1")
    print("----------------------------")
    m = HashMap(10, hash_function_1)
    print(m.contains_key('key1'))
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key3', 30)
    print(m.contains_key('key1'))
    print(m.contains_key('key4'))
    print(m.contains_key('key2'))
    print(m.contains_key('key3'))
    m.remove('key3')
    print(m.contains_key('key3'))


    print("\nPDF - contains_key example 2")
    print("----------------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 20)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.size, m.capacity)
    result = True
    for key in keys:
        # all inserted keys must be present
        result &= m.contains_key(str(key))
        # NOT inserted keys must be absent
        result &= not m.contains_key(str(key + 1))
    print(result)


    print("\nPDF - get example 1")
    print("-------------------")
    m = HashMap(30, hash_function_1)
    print(m.get('key'))
    m.put('key1', 10)
    print(m.get('key1'))


    print("\nPDF - get example 2")
    print("-------------------")
    m = HashMap(150, hash_function_2)
    for i in range(200, 300, 7):
        m.put(str(i), i * 10)
    print(m.size, m.capacity)
    for i in range(200, 300, 21):
        print(i, m.get(str(i)), m.get(str(i)) == i * 10)
        print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)


    print("\nPDF - remove example 1")
    print("----------------------")
    m = HashMap(50, hash_function_1)
    print(m.get('key1'))
    m.put('key1', 10)
    print(m.get('key1'))
    m.remove('key1')
    print(m.get('key1'))
    m.remove('key4')


    print("\nPDF - resize example 1")
    print("----------------------")
    m = HashMap(20, hash_function_1)
    m.put('key1', 10)
    print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))
    m.resize_table(30)
    print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))


    print("\nPDF - resize example 2")
    print("----------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 13)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.size, m.capacity)

    for capacity in range(111, 1000, 117):
        m.resize_table(capacity)

        m.put('some key', 'some value')
        result = m.contains_key('some key')
        m.remove('some key')

        for key in keys:
            result &= m.contains_key(str(key))
            result &= not m.contains_key(str(key + 1))
        print(capacity, result, m.size, m.capacity, round(m.table_load(), 2))


    print("\nPDF - get_keys example 1")
    print("------------------------")
    m = HashMap(10, hash_function_2)
    for i in range(100, 200, 10):
        m.put(str(i), str(i * 10))
    print(m.get_keys())

    m.resize_table(1)
    print(m.get_keys())

    m.put('200', '2000')
    m.remove('100')
    m.resize_table(2)
    print(m.get_keys())

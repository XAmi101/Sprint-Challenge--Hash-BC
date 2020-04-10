#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """        
    #loop through and for every ticket 
        #inserts each ticket into the hash table based on key
    #loop through every item in hash table
        #set route equal to hash_table_retrieve
        #where the starting point is equal to the route[] 
       
    for t in tickets:
        hash_table_insert(hashtable, t.source, t.destination)

    starting_point = "NONE"
    for i in range(length):
        route[i] = hash_table_retrieve(hashtable, starting_point)
        starting_point = route[i]
    return route[:len(route)-1] 
    

###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    file_handle = open(filename, 'r')
    cow_list = file_handle.readlines()
    file_handle.close()
    cow_dict = {}
    cow_name = []
    for line in cow_list:
        cow_name = line.split(',')
        cow_dict[cow_name[0]] = int(cow_name[1])
    
    return cow_dict

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cow_sorted = {k: v for k, v in sorted(
            cows.items(), key=lambda item: item[1], reverse = True)}
    print(cow_sorted)
    net_weight = 0
    trips = []
    current_trip = []
    while len(cow_sorted) != 0:
        for cow in cow_sorted:
            if (net_weight + cow_sorted[cow]) <= limit:
                current_trip += [cow]
                net_weight += cow_sorted[cow]
            
        for cow in current_trip:
            del(cow_sorted[cow])
    
        net_weight = 0
               
        trips += [current_trip]
        current_trip = []
        
    return trips
    

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """        
    print(cows)
    trip_weight = 0
    f = 0
    
    for partition in get_partitions(cows): #generating permutations os cows
        for sub_trip in partition: # iterating over each sublist in the permutation
            for name in sub_trip:
                trip_weight += cows[name] # calculating the weight of a sublist
            if trip_weight > limit:
                f = 1
                trip_weight = 0
                break # if the weight is more than limit, entire permutation is useless
            
            trip_weight = 0
            
        if f == 0:  # if, in the entire permutation, no sublist is overweight, it is the answer
            print(partition)
            break
            
        f = 0
        
        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    filename = 'ps1_cow_data.txt'
    cows = load_cows(filename)
    start = time.time()
    greedy_cow_transport(cows)
    end = time.time()
    print(end - start)
    start = time.time()
    brute_force_cow_transport(cows)
    end = time.time()
    print(end - start)

###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions

# ================================
# Part A: Transporting Space Cows
# ================================
import operator
import time
import itertools


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

    cow_dict = dict()

    f = open(filename, 'r')

    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows, limit=10):
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
    sorted_d = sorted(cows.items(), key=operator.itemgetter(1))
    ships = []
    while sorted_d:
        ship = []
        ship_limit = limit
        for k in reversed(sorted_d):
            if k[1] <= ship_limit:
                ship_limit -= k[1]
                ship.append(k)
                sorted_d.remove(k)
        ships.append(ship)
    return ships


# Problem 2
def brute_force_cow_transport(cows, limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
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
    comb = itertools.permutations(cows.items(), len(cows.items()))
    result = []
    for a in comb:
        ships = []
        used = []
        while len(used) != len(a):
            ship = []
            ship_limit = limit
            for k in reversed(a):
                if k[1] <= ship_limit and k not in used:
                    ship_limit -= k[1]
                    ship.append(k)
                    used.append(k)
            ships.append(ship)
        if not result or len(ships) < len(result):
            result = ships
    return result


# Problem 3
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
    cows = load_cows("ps1_cow_data.txt")
    limit = 10
    start_time_1 = time.time()
    print("Running greedy algorithm:...")
    greedy_res = len(greedy_cow_transport(cows, limit))
    end_1 = time.time() - start_time_1
    print("time taken-{}, ships a"
          "mount-{}".format(end_1, greedy_res))
    start_time_2 = time.time()
    print("Running brute force algorithm:...")
    brute_res = len(brute_force_cow_transport(cows, limit))
    end_2 = time.time() - start_time_2
    print("time taken-{}, ships amount-{}".format(end_2, brute_res))
    pass


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""


def main():
    print(brute_force_cow_transport({'MooMoo': 50, 'Boo': 20, 'Horns': 25, 'Lotus': 40, 'Milkshake': 40, 'Miss Bella': 25},
                              100))
    compare_cow_transport_algorithms()


if __name__ == '__main__':
    main()

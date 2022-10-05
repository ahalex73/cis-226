# Alexander Holmes
# 9/22/2022
# CRN:10235
# CIS 226: Advanced Python Programming
# Total time estimate: 3 hours

# This program demonstrates to the end user the practical applications of searching and sorting algorithms
# What is covered:
# Linked Lists and linearly searching through them
# Selection sort to sort through arrays
# Linearly searching through arrays
# Using binary search to search through arrays
# Each search and sort implementations have their respective Big O notation in
# Their given block comments.

# How to use:
# Either run with the command 'python search_and_sort.py' or run with anything that
# can run python files.

# You can also use the 'pytest' command to test that the selection sort is 
# sorting the given array correctly.


search_value = 8                                    # The search value you wish to look for
unsorted_array = [1, 7, 4, 2, 9, 8, 10, -4, 0, 3]   # Example array for searching and sorting through

class node:
    def __init__(self, data=None):
        ''' Initializes Node'''
        self.data = data
        self.next = None
        
class myLinkedList:
    def __init__(self):
        ''' Initializes Linked List'''
        self.head = node()

    def insert(self, data):
        ''' Appends a new node to the tail of our Linked list'''
        new_node = node(data)
        current = self.head
        while current.next !=None:
            current = current.next
        current.next = new_node

    def display(self):
        ''' Displays elements inside created linked list'''
        elements = []
        current = self.head
        while current.next != None:
            current = current.next
            elements.append(current.data)
        print(elements)

    def linear_search(self, search_value):
        ''' Linear search through linked list O(n)'''
        current = self.head     # Starts at the head of the linked list
        current_index = 0       # Keeps track of the current index in the linked list
        steps = 0               # Keeps track of the steps it took to search
        found = False

        if current is None:
            print("Linked List has no values")
            return

        while current is not None:
            if current.data == search_value:
                print("The value: {} is at index {}, found in {} steps\n".format(search_value, current_index, steps))
                found = True

            current_index += 1
            steps += 1
            current = current.next
        
        if found == False:
            print("The value: {} was not able to be found in the given Linked List.\n".format(search_value))


def swap(array, idx1, idx2):
    ''' Swaps the values at given indexes in a given array'''
    temp = array[idx1]  # temporary location to store index # 1 
                        #(dupliates the value into a seperate storage location)

    array[idx1] = array[idx2]   # changes first index given to second index given

    array[idx2] = temp          # changes second index to the temporary index value (where index 1 initially was)

def my_selection_sort(array):
    ''' Sorts given array in ascending order O(n^2)'''
    num_swaps = 0   # init number of swaps we used to sort array
    comparisons = 0 # init number of comparisons we computed from sorting

    for mark_a in range(len(array) - 1): # iterate fully through array
        min = mark_a                     # set a placeholder

        for current_idx in range(mark_a, len(array)):   # iterate through everything not 
                                                        #including what we already have searched through
            if array[current_idx] < array[min]:
                comparisons += 1
                min = current_idx

        # swap marker a's index with the minimum if they do not already equal
        if mark_a != min:
            num_swaps += 1
            swap(array, mark_a, min)

    print(array, "Number of swaps:{}. Number of comparisons:{}.\n".format(num_swaps, comparisons))
    return array
    

def linear_search(search_value, array):
    ''' Linearly searching for element in array O(n)'''
    step = 0
    for num in array:
        step += 1
        if num == search_value:
            print("The value {} is at index {}, found in {} steps\n".format(search_value, num, step))



def binary_search(search_value, array):
    ''' Search through array with binary sort O(log n)'''
    start = 0
    end = len(array)-1
    found = False
    step = 0
    comparisons = 0

    while found != True and start <= end:   
        # while we havent found search value and we havent crossed start and end markers
        # Calculate midway between start and end marker
        middle = int((start + end) / 2)

        if array[middle] == search_value:
            # Then we found the value
            comparisons += 1
            found = True
        
        elif array[middle] < search_value:
            # Value is to the right of our search
            start = middle + 1
            step += 1
            comparisons += 1
        else:
            # Value is to the left of our search
            end = middle - 1
            step += 1
            comparisons += 1
        
    print("The value {} is at index {}, found in {} steps\n".format(search_value, array[middle], step))

if __name__ == '__main__':
    print("The unsorted array:"+ str(unsorted_array))

    print("Sorting through unsorted list with selection sort.")
    sorted_array = my_selection_sort(unsorted_array)

    # 1, 7, 4, 2, 9, 8, 10, -4, 0, 3
    my_list = myLinkedList()

    print("Creating Linked List...")

    my_list.insert(1)
    my_list.insert(7)
    my_list.insert(4)
    my_list.insert(2)
    my_list.insert(9)
    my_list.insert(8)
    my_list.insert(-10)
    my_list.insert(-4)
    my_list.insert(0)
    my_list.insert(3)

    print("Linked list:")
    my_list.display()
    print("Linearly seaching for value {} in linked list.".format(search_value))
    my_list.linear_search(search_value) # linearly search for 8 in this case

    print("Linearly searching through unsorted array.")
    linear_search(search_value, unsorted_array)

    print("Binary Search through sorted array")
    binary_search(search_value, sorted_array)

# Alexander Holmes
# 9/22/2022
# CRN:10235
# CIS 226: Advanced Python Programming
# Total time estimate: 3 hours

from search_and_sort import my_selection_sort

def test_selection_sort():
    ''' Tests selection sort by comparing the 
        sorted array it gives us with what we expect'''
        
    sorted_array = [-4, 0, 1, 2, 3, 4, 7, 8, 9, 10]
    unsorted_array = [1, 7, 4, 2, 9, 8, 10, -4, 0, 3]

    assert my_selection_sort(unsorted_array) == sorted_array


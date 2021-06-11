#Author: Ashley Johnson
#Date: 4/16/2021
#Description: Program counts the number of comparisons and exchanges made while sorting a list and
# returns a tuple of the two values [comparisons, exchanges]. Programs uses bubble_count function to
#sort list using bubble sort and returns a tuple of comparisons and exchanges. Program uses insertion_sort
# function to sort list using insertion sort and returns a tuple of comparisons and exchanges.
def bubble_count(bubble_list):
    """function sorts a list using bubble sort and returns a tuple of the number of comparisons and exchanges
    made"""
    exchanges = 0
    comparisons = 0
    for pass_num in range(len(bubble_list)):
        for index in range(len(bubble_list) - 1 - pass_num):
            comparisons += 1
            if bubble_list[index] > bubble_list[index + 1]:
                temp = bubble_list[index]
                bubble_list[index] = bubble_list[index + 1]
                bubble_list[index + 1] = temp
                exchanges += 1
    return comparisons, exchanges

def insertion_count(insertion_list):
    """function sorts a list using insertion sort and returns a tuple of the number of comparisons and
    exchanges made"""
    exchanges = 0
    comparisons = 0
    for index in range(1, len(insertion_list)):
        value = insertion_list[index]
        pos = index - 1
        while pos >= 0:
            comparisons += 1
            if insertion_list[pos] > value:
                exchanges += 1
                insertion_list[pos + 1] = insertion_list[pos]
                pos -= 1
            else:
                break
        insertion_list[pos + 1] = value
    return comparisons, exchanges



def symmetric_difference_sets(set1, set2):

    return set1.symmetric_difference(set2)

# Example usage:
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

result = symmetric_difference_sets(set_a, set_b)
print(result)  


result_operator = set_a ^ set_b
print(result_operator) 

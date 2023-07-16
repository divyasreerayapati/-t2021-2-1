""" Problem-4:  Get the total count of number listed in the dictionary which is multiple of [1,2,3,4,5,6,7,8,9]
 (examples)
 input: [1,2,8,9,12,46,76,82,15,20,30]
 Output: {1: 11, 2: 8, 3: 4, 4: 4, 5: 3, 6: 2, 7: 0, 8: 1, 9: 1}"""

input_array = list(map(int, input().split(",")))

multi_dict = {}

for multiple in input_array:
    for value in range(1, 10):
        if multiple % value == 0:
            if value in multi_dict:
                multi_dict[value] += 1
            else:
                multi_dict[value] = 1
                
print(multi_dict)

"""Example Usage : 
    3,8,9,43,65,78,23,12
{1: 8, 3: 4, 2: 3, 4: 2, 8: 1, 9: 1, 5: 1, 6: 2}  """
        


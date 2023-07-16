"""Problem-2:  With a single integer as the input, generate the following until a = x [series of numbers as shown in below examples]

    Output: (examples)
        1) input a = 1, then output : 1
        2) input a = 2, then output : 1, 3
        3) input a = 3, then output : 1, 3, 5
        4) input a = 4, then output : 1, 3, 5, 7
        .
        .
        5) input a = x, then output : 1, 3, 5, 7, ......."""
        
def generateNumbers(a):
    output = []
    for i in range(1, a*2, 2):
        output.append(i)
    return output
            

a = int(input())
output = generateNumbers(a)
print(*output, sep=", ")


"""Example Usage
    9
    1, 3, 5, 7, 9, 11, 13, 15, 17 """
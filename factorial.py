###
#
#
##find factorail of given no
input_data = int(input("Enter no for factorial "))
result = 1
while input_data > 0 :
    result = result*input_data
    input_data = input_data-1
print(f'Result is % : ',result ) 

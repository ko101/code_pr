input_list = [23,32,12,435,6,7,443,34]
for i in range(len(input_list)):
    for j in range(i+1,len(input_list)):
        if input_list[i]>input_list[j]:
            input_list[i], input_list[j] = input_list[j],input_list[i]
            print(input_list)
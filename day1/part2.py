calibration_vls = []

file = open('test_lett.txt','r')
file_obj = file.readlines()
for line in file_obj:
  calibration_vls.append(line.strip())

# if the first 5 characters contains (one, two, three, four, five, six, seven, eight or nine) append to list, else append isdigit
# if the last 5 characters contains (one, two, three, four, five, six, seven, eight or nine) append to list, else append isdigit
lett_list=["one","two","three","four","five","six","seven","eight","nine"]
num_list=[]
for item in calibration_vls:
    for lett in lett_list:
        item.find(lett)

# last_list=[]
# for item in num_list:
#     var = item[0] + item[-1]
#     var = int(var)
#     last_list.append(var)

# total = sum(last_list)

# print(total)
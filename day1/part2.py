calibration_vls = []

file = open('test_lett.txt','r')
file_obj = file.readlines()
for line in file_obj:
  calibration_vls.append(line.strip())

last_list=[]

for item in calibration_vls:
    num_str=""
    if item[0].isdigit():
        num_str += str(item[0])
    if item[-1].isdigit():
        num_str += str(item[-1])

    if item[:3] == "one":
        num_str += "1"
    if item[-3:] == "one":
        num_str += "1"

    if item[:3] == "two":
        num_str += "2"
    if item[-3:] == "two":
        num_str += "2"

    if item[:5] == "three":
        num_str += "3"
    if item[-5:] == "three":
        num_str += "3"

    if item[:4] == "four":
        num_str += "4"
    if item[-4:] == "four":
        num_str += "4"

    if item[:4] == "five":
        num_str += "5"
    if item[-4:] == "five":
        num_str += "5"

    if item[:3] == "six":
        num_str += "6"
    if item[-3:] == "six":
        num_str += "6"

    if item[:5] == "seven":
        num_str += "7"
    if item[-5:] == "seven":
        num_str += "7"

    if item[:5] == "eight":
        num_str += "8"
    if item[-5:] == "eight":
        num_str += "8"

    if item[:4] == "nine":
        num_str += "9"
    if item[-4:] == "nine":
        num_str += "9"

    # num_str = int(num_str)
    last_list.append(num_str)

print(num_str)
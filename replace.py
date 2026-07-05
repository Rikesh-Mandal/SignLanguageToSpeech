f = open("D:/FYP/numberImageRecognition/Lib/train/C_data/C_test_data.txt", 'a')
fr =  open("D:/FYP/numberImageRecognition/Lib/train/C_data/C_test_data.txt", 'r')


output = fr.readlines()
new_file = open("D:/FYP/numberImageRecognition/Lib/train/C_data/C_test_newdata.txt", 'w')
for data in output:
    #print(data)
    result = data.replace("[","")
    result = result.replace("]","")
    result = result.replace(",","")
    new_file.write(result)
    #print(result)
# for each in fr:
#
#     f.write(each.split("[",""))
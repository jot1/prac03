__author__ = 'jc437345'

temp_file = open("temp.txt","w")
print("firstline", file=temp_file)
print("second line", file=temp_file)
print("third line", file=temp_file)
print("fourth line", file=temp_file)
temp_file.close()
print('===')
temp_file = open("temp.txt","r")
for line in temp_file:
    line = line.strip()
    print(line)
temp_file.close()
print('===')
temp_file = open("temp.txt","r")
my_str = temp_file.read()
print(my_str)
temp_file.close()
print('===')
temp_file = open("temp.txt", "r")
lines = temp_file.readlines()
print(lines)
#for line in lines:
 #   line = line.strip()
  #  print(line)
temp_file.close()
print('===')
my_list = ['firstline\n', 'second line\n', 'third line\n', 'fourth line\n']
out_file = open("out.txt", "w")
out_file.writelines(my_list)
out_file.close()


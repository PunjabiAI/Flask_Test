

file_data=open('file4.txt',encoding="utf-8", errors='ignore').read()
file_data = file_data.encode()
file_data = file_data.decode()
print(file_data)

# with open('file2.txt', 'r',encoding='utf-8') as fn:
#
#    lines = fn.readlines()
#    print(lines)



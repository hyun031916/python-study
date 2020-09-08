#p234
'''

file = open('파일이름', '옵션')
file.close()
'''

# file = open('file.txt', 'w')           #write
#
# file.write('hello')
# file.write('\n')
# file.write('world')
#
# file.close()

try:
    file = open('file.txt', 'w', encoding="utf8")  #r, w, rb, wb, a, r+, w+
    file.write('김미림, 010-2222-3333\n')
    file.write('이미림, 010-4444-5555\n')
finally:
    file.close()

# with open('file.txt', 'w', encoding='utf') as file:
#     file.write('hello')
#     file.write('월드')
#245
import array
with open('data.bin', 'rb') as file:
    data = array.array("B")
    data.fromfile(file, 3)

print(data)
for item in data:
    print(item)
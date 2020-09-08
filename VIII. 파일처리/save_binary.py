#p238
byte_list = bytes([255, 0, 127])    #[FF, 00, 7F]=>[11111111, 00000000, 01111111]
with open('data.bin', 'wb') as file:
    file.write(byte_list)
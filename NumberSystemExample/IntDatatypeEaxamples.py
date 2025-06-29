#int Datatype examples :
#Questions 1 to 7 . Level-1
#1 - Convert decimal 25 to  binary,octal,and hexadecimal.
  #Decimal to binary
a=25
bv=bin(a)
print(bv,type(bv))

  #Decimal to octal
b=25
ov=oct(b)
print(ov,type(ov))#type of tell the data type

  #Decimal to hexadecimal
c=25
hv=hex(c)
print(hv,type(hv))

#2-Convert decimal 64 to binary,octal,and hexadecimal.

  #Decimal to binary
a=64
bv=bin(a)
print(bv,type(bv))

  #Decimal to octal
b=64
ov=oct(b)
print(ov,type(ov))

  #Decimal to hexadecimal
c=64
hv=hex(c)
print(hv,type(hv))


#3-Convert binary 0b1010 to decimal.
a=0b1010
decimal_number=int(a)
print(decimal_number,type(decimal_number))

#4-Convert octal 0o45 to decimal.
a=0o45
decimal_number=int(a)
print(decimal_number,type(decimal_number))

#5-Convert hexadecimal 0x2F to decimal.
a=0x2F
decimal_number=int(a)
print(decimal_number)

#6-Convert decimal 100 to binary.
a=100
bv=bin(a)
print(bv)

#7-Convert binary 0b111111111 to octal and hexa decimal.
a=0b11111111
ov=oct(a)
print(ov)

a=0b11111111
hv=hex(a)
print(hv)

#8-Convert hexadecimal 0xA5 to binary and decimal.
a=0xA5
bv=bin(a)
print(bv)

decimal_number=int(a)
print(a)

#9-convert octal 0b777 to binary and decimal.
a=0o777
bv=bin(a)
print(bv)

decimal_number=int(a)
print(decimal_number)

#10-convert binary ob1100100 to decimal and hexadecimal.
a=0b1100100
decimal_nummber=int(a)
print(decimal_number)

hv=hex(a)
print(hv)

#11-Convert decimal 256 to all three: binary,octal,and hexa.
a=256
bv=bin(a)
ov=oct(a)
hv=hex(a)
print(bv,ov,hv)

#12-convvert decimal 500 to binary.
decimal_number=500
bv=bin(decimal_number)
print(bv)

#13-convert binary string "11001101" to decimal using int() in python.
binary_string="11001101"
decimal_nummber=int(binary_string,2)
print(decimal_number)

#14-convert hex string"1F4"to binary using python.
hex_string="1F4"
bv=(hex_string,16)
print(bv)

#15-convert decimal 4096 to binary,octal,and hexa.
decimal_number=4096
bv=bin(decimal_number)
ov=oct(decimal_number)
hv=hex(decimal_number)
print(bv,ov,hv)

#16-convert hexadecimal 0x1FA3 to binary and decimal.
hex_decimal=0x1FA3
bv=bin(hex_decimal)
decimal_number=int(hex_decimal)
print(bv,decimal_number)

#17-convert binary 0b100000000000 to octal and hexadecimal.
a=0b100000000000
ov=oct(a)
print(ov)
hv=hex(a)
print(hv)

#18-write a python function that accepts a decimal number and returns all three formats(binary,octal,hex).
def convert_number_formates(decimal_nummbers):
 bv=bin(decimal_number)
 ov=oct(decimal_number)
 hv=hex(decimal_number)
 return binary,octal,hexa
#Example usage :
decimal_nummber=256
#binary,octal,hexa=convert_nummber_formats(decimal)
print(decimal_number)
print(bv)
print(ov)
print(hv)

#19-write a python function that takes a binary string and returns decimal and hexa values.
def binary_to_decimal_and_hex(binary_str):
    decimal_value=int(binary_str,2)
    hex_value=hex(decimal_value)[2:].upper()
    return decimal_value,hex_value
#Example usage :
binary_input="1101101"
decimal,hexa=binary_to_decimal_and_hex(binary_input)
print(f"binary:{binary_input}")
print(f"decimal:{decimal}")
print(f"hexasdecimal:{hex}")

#20-converts this octal number 0o177777 to binary and hexadecimal.
a=0o177777
bv=bin(a)
print(bv)

hv=hex(a)
print(hv)




# Check if string is a valid number

# Given a  string, write a method that returns true if the string is a valid number or false otherwise. Only integers and decimals should be considered as valid. In other words, only characters allowed are digits, "-" and ".". The string can be very long (think millions of characters) and no built-in function/class can handle it without overflowing or losing precision.

# "13"    ---> true
# "3.0"   ---> true
# ".01"
# "-7.4"  ---> true
# "-00013.5" ---> true
# "abc"   ---> false
# "123a"  ---> false
# "-."    ---> false
# "-..--" ---> false
# "1.0.0.1" -> false
# "1."

def valid_number(word)->bool:
    count_decimal=False
    digit_counter = 0
    # valid_char = {'0','1','2','3','4','5','6',''}
    if word[0]=='.':
        count_decimal=True
    if not(word[0]=='-' or word[0].isdigit() or count_decimal):
        return False
    if word[0].isdigit():
        digit_counter+=1
    
    for c in word[1:]: 
        if c == ".":
            if count_decimal:
                return False
            else:
                count_decimal=True
                continue

        if not c.isdigit():
            return False
        else:
            digit_counter=1
    if digit_counter==0:
        return False
    return True

inp_list=["13",#    ---> true
"3.0",#   ---> true
".01",#
"-7.4",#  ---> true
"-00013.5",# ---> true
"abc",#   ---> false
"123a",#  ---> false
"-.",#    ---> false
"-..--",# ---> false
"1.0.0.1",# -> false
"1."] #]
for i in inp_list:
    print(valid_number(i))
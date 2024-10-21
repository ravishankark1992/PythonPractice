ones={
            0: "Zero",
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine"
        }
tens = {
    10: "Ten",
    11: "Eleven",
    12: "Twelve",
    13: "Thirteen",
    14: "Fourteen",
    15: "Fifteen",
    16: "Sixteen",
    17: "Seventeen",
    18: "Eighteen",
    19: "Nineteen",
    20: "Twenty",
    30: "Thirty",
    40: "Forty",
    50: "Fifty",
    60: "Sixty",
    70: "Seventy",
    80: "Eighty",
    90: "Ninety"
}


def numberToWords(i):
    if i<10:
        return ones[i]
    elif i<20:
        return tens[i]
    elif i<100:
        return tens[i//10*10] + " " + ones[i%10]
    else:
        return ones[i//100] + " Hundred " + tens[(i%100)//10*10] + " " + ones[i%10]
        
    return

print(numberToWords(123))
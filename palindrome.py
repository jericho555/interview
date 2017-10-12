def palindrome(number):
    if isPalindrome(number): #checking for palindrome on number
        print number, " is a palindrome"
    else:
        num = int(number) + int(number[::-1]) # reverse and add original number
        print num," not palindrome"
        if num > 1000000: # if doesnt converge
            print "Number > a million \nExiting"
            return False
        else:
            print "next ==>"
            return palindrome(str(num)) # return palindrome


def isPalindrome(number):
    #  check if palindrome and return true
    if number == number[::-1]:
        return True




if __name__== "__main__":

    while True:
        number = raw_input("PLease Enter NUMBER\n")

        if number.isdigit():# check whether string has numbers only

            palindrome(number)

        else:
            continue


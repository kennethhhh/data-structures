def bears(n):
    if n==42:
        return (True)
    elif n<42:
        return (False)
    else:
        if n%2==0:
            #if True, return True, if not, keep running
            if bears(n//2):
                return (True)
        if (n%3==0 or n%4==0):
            #operation to multiply last 2 digits
            string_of_num=str(n)
            integer=int(string_of_num[len(string_of_num)-1])*int(string_of_num[len(string_of_num)-2])
            #if True, return True, if not, keep running
            if integer!=0:
                if bears(n-integer):
                    return (True)
        #This is the last case so if not True, it returns False
        if n%5==0:
            return bears(n-42)
        #returns False if not True
        return (False)


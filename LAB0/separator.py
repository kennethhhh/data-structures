import sys

def  main():
    int_counter=0
    float_counter=0
    integers=""
    floats=""

    while int_counter-1 < int(sys.argv[1]) and float_counter-1 < int(sys.argv[1]):
        number=input()
        list_of_num=number.split()
        for num in list_of_num:
            if num.isdigit():
                int_counter += 1
                if int_counter > int(sys.argv[1]):
                    break
                integers+=(num)
                integers+=" "


            try:
                if num.isdigit()!=True and float(num):
                    float_counter += 1
                    if float_counter > int(sys.argv[1]):
                        break
                    floats+=(num)
                    floats+=" "

            except:
                int_counter+=int(sys.argv[1])+1
                break

        if number=="":
            break



    print("Integers:",integers)
    print("Floats:",floats)



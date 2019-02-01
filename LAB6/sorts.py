import random
import time

def selection_sort(list):
    comps=0
    for index in range(len(list)):
        positionofmin=index
        for j in range(index+1,len(list)):
            if list[j]<list[positionofmin]:
                positionofmin=j
            comps+=1
        list[index],list[positionofmin]=list[positionofmin],list[index]
    return comps


def insertion_sort(list):
    comps=0
    for index in range(1,len(list)):
        index_of_sorted=index-1
        comparing_number = list[index]
        if comparing_number>list[index_of_sorted]:
            comps+=1
        while comparing_number<list[index_of_sorted] and (index_of_sorted>=0):
            list[index_of_sorted+1]=list[index_of_sorted]
            index_of_sorted-=1
            comps+=1
        list[index_of_sorted+1]=comparing_number
    return comps

   

# def main():
#     # Give the random number generator a seed, so the same sequence of
#     # random numbers is generated at each run
#     random.seed(1234)
#
#     # Generate 5000 random numbers from 0 to 999,999
#     randoms = random.sample(range(1000000), 1000)
#     start_time = time.time()
#     comps = insertion_sort(randoms)
#     stop_time = time.time()
#     print(comps, stop_time - start_time)
#
# if __name__ == '__main__':
#     main()

#print(insertion_sort([4,51,2,541,2,1,4,5]))
#print(insertion_sort([10,9,8,7,6,5,4,3,2,1]))
#main()

def max_list_iter(int_list):  # must use iteration not recursion
    """finds the max of a list of numbers and returns the value (not the index)
    If int_list is empty, returns None. If list is None, raises ValueError"""
    if int_list==None:
        raise(ValueError)
    if len(int_list)==0:
        return (None)
    else:
        init_max = int_list[0]
        for indx in range(0,len(int_list)):
            if int_list[indx]>init_max:
                init_max=int_list[indx]
        return (init_max)


def reverse_rec(int_list):   # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
    If list is None, raises ValueError"""
    if int_list==None:
        raise(ValueError)
    if len(int_list)==0:
        return (int_list)
    if len(int_list)==1:
        return (int_list)
    else:
        return ([int_list[len(int_list)-1]]+reverse_rec(int_list[0:(len(int_list)-1)]))



def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
    If target is not found returns None. If list is None, raises ValueError """
    #Returns None if list is None or no items in list
    if int_list==None:
        raise(ValueError)
    if len(int_list) == 0:
        return (None)
    if high <= low and int_list[high] != target:
        return (None)
    middle = (low + high) // 2
    #If the target of the search is in the list, the function returns its index.
    if int_list[middle] == target:
        return (middle)
    #Assuming that the int_list is in order from least to greatest, searches higher or lower
    elif target > int_list[middle]:
        return (bin_search(target, middle + 1, high, int_list))
    elif target < int_list[middle]:
        return (bin_search(target, low, middle - 1, int_list))

#print(max_list_iter([10]))
#print(reverse_rec([]))
#print(bin_search(3,2,5,[3,3,2,4,6,3,8,9]))

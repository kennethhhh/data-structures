def perm_gen_lex(a):
    #base cases
    if len(a)==0:
        return([])
    if len(a)==1:
        return ([a])
    new_L=[]
    for idx in range(len(a)):
        #separating into simpler permutation
        perms= perm_gen_lex(a[:idx]+a[idx+1:])
        for letters in perms:
            #adding back letter that was subtracted from above
            new_L.append(a[idx]+letters)
    return (new_L)

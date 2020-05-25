#PF-Tryout

def guess_number(number_in_mind):
    import random
    i=random.randrange(1,11)
    print(i)
    if i<number_in_mind:
        print ('Number is low')
    elif i>number_in_mind:
        print ('Number is high')
    else:
        print ('You have got it right!!!')

guess_number(4)

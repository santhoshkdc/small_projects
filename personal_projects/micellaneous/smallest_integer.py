def closest_to_zero(A):
    a = 0
    array = A.split(' ')
    array = list(int(x) for x in array)
    length = len(array)
    if length > 100:
        print("size of the array is greater than 100.")
    elif length < 1:
        print("Size of the array is 0.")
    else:
        print(f"Size of the array is {length} \n")
        if a in array:
            print(a)
        else:
            neg = []
            pos = []
            for i in array:
                if abs(i)!=i:
                    neg.append(i)
                elif abs(i)==i:
                    pos.append(i)
            closest_neg = max(neg)
            closest_pos = min(pos)
            if abs(closest_neg) > closest_pos:
                print(closest_pos)
            elif closest_pos> abs(closest_neg):
                print(closest_neg)
            elif abs(closest_neg) == closest_pos:
                print(closest_pos)
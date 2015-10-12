def distance_from_zero (n):
    if isinstance(n,int) or  isinstance(n,float):
        return abs(n)
    else:
        return "This isn't an integer or a float!"

distance_from_zero (10)

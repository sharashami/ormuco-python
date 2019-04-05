import sys

if len(sys.argv) != 5:
    print('You should give me 4 numbers (x1,x2,x3,x4) as command line arguments which comprehend the two lines (x1,x2) and (x3,x4) on the x-axis. Then, I will check whether they overlap.')
else:

    _, x1, x2, x3, x4 = sys.argv

    try:
        float(x1)
        float(x2)
        float(x3)
        float(x4)
    except ValueError:
        raise ValueError('ValueError. You should give me 4 numbers (x1,x2,x3,x4) as input that means the two lines (x1,x2) and (x3,x4) on the x-axis. Then, I will check whether they overlap.')

    if x1 == x2 or x3 == x4:
        raise ValueError('A line cannot have the same start and end value.')
    
    line1 = [x1 , x2]
    line1.sort()
    line2 = [x3 , x4]
    line2.sort()
    overlap =  ( line1[0] >= line2[0] and line1[0] <= line2[1] ) or ( line1[1] >= line2[0] and line1[1] <= line2[1] )
        
    print(f'({x1},{x2}) and ({x3},{x4}) overlap.') if overlap else print(f'({x1},{x2}) and ({x3},{x4}) do not overlap.')
    
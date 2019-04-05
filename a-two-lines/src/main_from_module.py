import sys
import lines

if len(sys.argv) != 5:
    print('You should give me 4 numbers (x1,x2,x3,x4) as command line arguments which comprehends the two lines (x1,x2) and (x3,x4) on the x-axis. Then, I will check whether they overlap.')
else:

    _, x1, x2, x3, x4 = sys.argv


    print(f'({x1},{x2}) and ({x3},{x4}) overlap.') if lines.overlap(x1,x2,x3,x4) else print(f'({x1},{x2}) and ({x3},{x4}) do not overlap.')
    
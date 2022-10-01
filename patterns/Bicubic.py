import pandas as pd
import math
Bicubic_parameter_set=[]
def Bicubic_check_conflict(n, b,d1):
    i=3
    j=3
    index_a1=(d1 * (i-1) + j - 1 )
    index_a2=(d1 * (i-1) + j + 1 )
    index_a3=(d1 * (i+1) + j - 1 )
    index_a4=(d1 * (i+1) + j + 1 )
    a1 = math.floor(index_a1 / b) % n
    a2 = math.floor(index_a2 / b) % n
    a3 = math.floor(index_a3 / b) % n
    a4 = math.floor(index_a4 / b) % n
    A = [a1 ,a2 ,a3 ,a4 ]
    conflict_set = []
    for x in A :
        if(x in conflict_set) :
            # print("Bicubic conflict {0}".format(A))
            return
        else:
            conflict_set.append(x)
    print("Bicubic suceess ,"+"n=%d"%n+" b=%d"%b)
    valid_solution={'bank_number':n,'block_size':b}
    Bicubic_parameter_set.append(valid_solution)
    return

from datetime import datetime 
def get_Bicubic(bmax,nmax,Bicubic_width):
    start_t=datetime.now()
    b = 1
    while b <= bmax:
        n = 1
        while n <= nmax:
            Bicubic_check_conflict(n, b, Bicubic_width)
            n = n * 2
        b = b * 2
    end_t=datetime.now()
    print("Bicubic execute time = %d" %(end_t.microsecond-start_t.microsecond))
    
    Bicubic_df = pd.DataFrame(Bicubic_parameter_set, columns=['bank_number', 'block_size'], dtype=int)
    Bicubic_df.to_csv('./result/Bicubic.csv')

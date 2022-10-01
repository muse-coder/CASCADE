import pandas as pd
import math
Denoise_parameter_set=[]
def Denoise_check_conflict(n, b,d1):
    i=3#任意设的  无影响
    j=3#任意设的  无影响
    index_a1=(d1 * (i-1) + j  )
    index_a2=(d1 * (i+1) + j  )
    index_a3=(d1 * i + j - 1 )
    index_a4=(d1 * i + j + 1 )
    a1 = math.floor(index_a1 / b) % n
    a2 = math.floor(index_a2 / b) % n
    a3 = math.floor(index_a3 / b) % n
    a4 = math.floor(index_a4 / b) % n
    A = [a1 ,a2 ,a3 ,a4 ]
    conflict_set = []
    for x in A :
        if(x in conflict_set) :
            # print("Denoise conflict {0}".format(A))
            return
        else:
            conflict_set.append(x)

    print("Denoise suceess ,"+"n=%d"%n+" b=%d"%b)
    valid_solution={'bank_number':n,'block_size':b}
    Denoise_parameter_set.append(valid_solution)
    return

from datetime import datetime 

def get_Denoise(bmax,nmax,Denoise_width):
    start_t=datetime.now()
    b = 1
    while b <= bmax:
        n = 1
        while n <= nmax:
            Denoise_check_conflict(n, b, Denoise_width )
            n = n * 2
        b = b * 2
    end_t=datetime.now()
    print("Denoise execute time = %d" %(end_t.microsecond-start_t.microsecond))
    
    Denoise_df= pd.DataFrame(Denoise_parameter_set, columns=['bank_number', 'block_size'], dtype=int)
    Denoise_df.to_csv('./result/Denoise.csv')

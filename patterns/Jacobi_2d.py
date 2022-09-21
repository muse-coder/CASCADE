import pandas as pd
import math
Jacobi_2d_parameter_set=[]

def Jacobi_2d_check_conflict(n, b,d1):
    i=3#任意设的  无影响
    j=3#任意设的  无影响    
    index_a1=(d1 * (i-1) + j  )
    index_a2=(d1 * (i+1) + j  )
    index_a3=(d1 * i + j      )
    index_a4=(d1 * i + j - 1  )
    index_a5=(d1 * i + j + 1  )
    a1 = math.floor(index_a1 / b) % n
    a2 = math.floor(index_a2 / b) % n
    a3 = math.floor(index_a3 / b) % n
    a4 = math.floor(index_a4 / b) % n
    a5 = math.floor(index_a5 / b) % n
    A = [a1 ,a2 ,a3 ,a4 ,a5]
    conflict_set = []
    for x in A :
        if(x in conflict_set) :
            # print("Jacobi_2d conflict {0} ".format(A))
            return
        else:
            conflict_set.append(x)

    print("Jacobi_2d suceess ,"+"n=%d"%n+" b=%d"%b)
    valid_solution={'bank_number':n,'block_size':b}
    Jacobi_2d_parameter_set.append(valid_solution)
    return


def get_Jacobi_2d(bmax,nmax,Jacobi_2d_width):
    b = 1
    while b <= bmax:
        n = 1
        while n <= nmax:
            Jacobi_2d_check_conflict(n, b, Jacobi_2d_width )
            n = n * 2
        b = b * 2
    Jacobi_2d_df= pd.DataFrame(Jacobi_2d_parameter_set, columns=['bank_number', 'block_size'], dtype=int)
    Jacobi_2d_df.to_csv('./result/Jacobi_2d.csv')

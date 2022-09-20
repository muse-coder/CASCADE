import pandas as pd
import math
Log_parameter_set=[]

def Log_check_conflict(n, b,d1,N):
    for i in range(2, N-1):
        for j in range(2, N-1):
            index_a1 = (d1 * (i-2) + j   )
            index_a2 = (d1 * (i-1) + j   )
            index_a3 = (d1 * (i)   + j   )
            index_a4 = (d1 * (i+1) + j   )
            index_a5 = (d1 * (i+2) + j   )

            index_a6 =(d1 * (i)   + j - 2  )
            index_a7 =(d1 * (i)   + j + 2  )

            index_a8 =(d1 * (i)   + j - 1  )
            index_a9 =(d1 * (i-1) + j - 1  )
            index_a10=(d1 * (i+1) + j - 1  )

            index_a11 =(d1 * (i)   + j + 1  )
            index_a12 =(d1 * (i-1) + j + 1  )
            index_a13 =(d1 * (i+1) + j + 1  )

            a1 = math.floor(index_a1 / b) % n
            a2 = math.floor(index_a2 / b) % n
            a3 = math.floor(index_a3 / b) % n
            a4 = math.floor(index_a4 / b) % n
            a5 = math.floor(index_a5 / b) % n
            a6 = math.floor(index_a6 / b) % n
            a7 = math.floor(index_a7 / b) % n
            a8 = math.floor(index_a8 / b) % n
            a9 = math.floor(index_a9 / b) % n
            a10 = math.floor(index_a10 / b) % n
            a11 = math.floor(index_a11 / b) % n
            a12 = math.floor(index_a12 / b) % n
            a13 = math.floor(index_a13 / b) % n

            A = [a1 ,a2 ,a3 ,a4 ,a5 ,a6 ,a7 ,a8 ,a9 ,a10 ,a11 ,a12 ,a13]
            conflict_set = []
            for x in A :
                if(x in conflict_set) :
                    # print("Log conflict {0}".format(A))
                    return
                else:
                    conflict_set.append(x)

    print("Log suceess ,"+"n=%d"%n+" b=%d"%b)
    valid_solution={'bank_number':n,'block_size':b}
    Log_parameter_set.append(valid_solution)
    return


def get_Log(bmax,nmax,Log_width):
    b = 1
    while b < bmax:

        n = 1
        while n < nmax:
            Log_check_conflict(n, b, Log_width , Log_width - 1)
            n = n * 2
        b = b * 2
    Log_df= pd.DataFrame(Log_parameter_set, columns=['bank_number', 'block_size'], dtype=int)
    Log_df.to_csv('./result/Log.csv')

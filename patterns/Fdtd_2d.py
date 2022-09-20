import pandas as pd
import math
Fdtd_2d_parameter_set=[]
def Fdtd_2d_check_conflict(n, b,d1,N):
    for i in range(1, N):
        for j in range(1, N):
            index_x1=(d1 * (i) + j  )
            index_x2=(d1 * (i) + j + 1 )
            
            index_y1=(d1 * (i-1) + j)
            index_y2=(d1 * (i)   + j)
            
            index_z1=(d1 * (i-1) + j)
            index_z2=(d1 * (i)   + j)
            index_z3=(d1 * (i+1) + j)
            index_z4=(d1 * (i)   + j - 1 )
            index_z5=(d1 * (i)   + j + 1 )
            
            x1 = math.floor(index_x1 / b) % n
            x2 = math.floor(index_x2 / b) % n
            X_array = [x1 ,x2 ]
            X_conflict_set = []
            
            y1 = math.floor(index_y1 / b) % n
            y2 = math.floor(index_y2 / b) % n
            Y_array = [y1 ,y2 ]
            Y_conflict_set = []
            
            z1 = math.floor(index_z1 / b) % n
            z2 = math.floor(index_z2 / b) % n
            z3 = math.floor(index_z3 / b) % n
            z4 = math.floor(index_z4 / b) % n
            z5 = math.floor(index_z5 / b) % n
            Z_array = [z1 ,z2 ,z3 ,z4 ,z5 ]
            Z_conflict_set = []

            for x in X_array :
                if(x in X_conflict_set) :
                    # print("Bicubic conflict {0}".format(A))
                    return
                else:
                    X_conflict_set.append(x)
    
            for y in Y_array :
                if(y in Y_conflict_set) :
                    # print("Bicubic conflict {0}".format(A))
                    return
                else:
                    Y_conflict_set.append(y)
    
            for z in Z_array :
                if(z in Z_conflict_set) :
                    # print("Bicubic conflict {0}".format(A))
                    return
                else:
                    Z_conflict_set.append(z)

    print("Fdtd_2d suceess ,"+"n=%d"%n+" b=%d"%b)
    valid_solution={'bank_number':n,'block_size':b}
    Fdtd_2d_parameter_set.append(valid_solution)
    return


def get_Fdtd_2d (bmax,nmax,Fdtd_2d_width):
    b = 1
    while b < bmax:
        n = 1
        while n < nmax:
            Fdtd_2d_check_conflict(n, b, Fdtd_2d_width, Fdtd_2d_width - 1)
            n = n * 2
        b = b * 2
    Fdtd_2d_df = pd.DataFrame(Fdtd_2d_parameter_set, columns=['bank_number', 'block_size'], dtype=int)
    Fdtd_2d_df.to_csv('./result/Fdtd_2d.csv')
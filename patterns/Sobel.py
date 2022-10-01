import pandas as pd
import math
Sobel_parameter_set=[]
def Sobel_check_conflict(n, b,d1):
    i=3#任意设的  无影响
    j=3#任意设的  无影响
    index_x1=(d1 * (i - 1) + j - 1 )
    index_x2=(d1 * (i - 1) + j + 1 )
    index_x3=(d1 * (i - 1) + j     )
    
    index_x4=(d1 * (i) + j - 1)
    index_x5=(d1 * (i) + j + 1)
            
    index_x6=(d1 * (i + 1) + j - 1)
    index_x7=(d1 * (i + 1) + j + 1)
    index_x8=(d1 * (i + 1) + j    )
            
            
    x1 = math.floor(index_x1 / b) % n
    x2 = math.floor(index_x2 / b) % n
    x3 = math.floor(index_x3 / b) % n
    x4 = math.floor(index_x4 / b) % n
    x5 = math.floor(index_x5 / b) % n
    x6 = math.floor(index_x6 / b) % n
    x7 = math.floor(index_x7 / b) % n
    x8 = math.floor(index_x8 / b) % n
    X_array = [x1 ,x2 ,x3 ,x4 ,x5 ,x6 ,x7 ,x8 ]
    conflict_set = []

    for x in X_array :
        if(x in conflict_set) :
            # print("Bicubic conflict {0}".format(A))
            return
        else:
            conflict_set.append(x)
    
    print("Sobel suceess ,"+"n=%d"%n+" b=%d"%b)
    valid_solution={'bank_number':n,'block_size':b}
    Sobel_parameter_set.append(valid_solution)
    return


from datetime import datetime 
def get_Sobel (bmax,nmax,Sobel_width):
    start_t=datetime.now()
    b = 1
    while b <= bmax:
        n = 1
        while n <= nmax:
            Sobel_check_conflict(n, b, Sobel_width)
            n = n * 2
        b = b * 2
    end_t=datetime.now()
    print("Sobel execute time = %d" %(end_t.microsecond-start_t.microsecond))

    Sobel_df = pd.DataFrame(Sobel_parameter_set, columns=['bank_number', 'block_size'], dtype=int)
    Sobel_df.to_csv('./result/Sobel.csv')
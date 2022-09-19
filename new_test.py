import pandas as pd
import math
Bicubic_parameter_set=[]
Denoise_parameter_set=[]
jacobi_2d_parameter_set=[]
seidel_2d_parameter_set=[]
log_parameter_set=[]
def Bicubic_check_conflict(n, b,d1,N):
    for i in range(1, N):
        for j in range(1, N):
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
                    print("Bicubic conflict {0}".format(A))
                    return
                else:
                    conflict_set.append(x)
    print("Bicubic suceess ,"+"n=%d"%n+" b=%d"%b)
    valid_solution={'bank_number':n,'block_size':b}
    Bicubic_parameter_set.append(valid_solution)
    return

# a[i-1][j] a[i+1][j]
# a[i][j-1] a[i][j+1]
def Denoise_check_conflict(n, b,d1,N):
    for i in range(1, N):
        for j in range(1, N):
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
                    print("Denoise conflict {0}".format(A))
                    return
                else:
                    conflict_set.append(x)

    print("Denoise suceess ,"+"n=%d"%n+" b=%d"%b)
    valid_solution={'bank_number':n,'block_size':b}
    Denoise_parameter_set.append(valid_solution)
    return

# a[i-1][j]     a[i][j]    a[i+1][j]
# a[i][j-1]     a[i][j+1]

def jacobi_2d_check_conflict(n, b,d1,N):
    for i in range(1, N):
        for j in range(1, N):
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
                    print("jacobi_2d conflict {0} ".format(A))

                    return
                else:
                    conflict_set.append(x)

    print("jacobi_2d suceess ,"+"n=%d"%n+" b=%d"%b)
    valid_solution={'bank_number':n,'block_size':b}
    jacobi_2d_parameter_set.append(valid_solution)
    return


# a[i-1][j-1]  a[i-1][j]  a[i-1][j+1]
# a[i][j-1]    a[i][j]    a[i][j+1]
# a[i+1][j-1]  a[i+1][j]  a[i+1][j+1]
def seidel_2d_check_conflict(n, b,d1,N):
    for i in range(1, N):
        for j in range(1, N):
            index_a1=(d1 * (i-1) + j - 1  )
            index_a2=(d1 * (i-1) + j      )
            index_a3=(d1 * (i-1) + j + 1  )

            index_a4=(d1 * (i)   + j - 1  )
            index_a5=(d1 * (i)   + j      )
            index_a6=(d1 * (i)   + j + 1  )

            index_a7=(d1 * (i+1) + j - 1  )
            index_a8=(d1 * (i+1) + j      )
            index_a9=(d1 * (i+1) + j + 1  )

            a1 = math.floor(index_a1 / b) % n
            a2 = math.floor(index_a2 / b) % n
            a3 = math.floor(index_a3 / b) % n
            a4 = math.floor(index_a4 / b) % n
            a5 = math.floor(index_a5 / b) % n
            a6 = math.floor(index_a6 / b) % n
            a7 = math.floor(index_a7 / b) % n
            a8 = math.floor(index_a8 / b) % n
            a9 = math.floor(index_a9 / b) % n

            A = [a1 ,a2 ,a3 ,a4 ,a5 ,a6 ,a7 ,a8 ,a9]
            conflict_set = []
            for x in A :
                if(x in conflict_set) :
                    print("seidel_2d conflict {0}".format(A))
                    return
                else:
                    conflict_set.append(x)

    print("seidel_2d suceess ,"+"n=%d"%n+" b=%d"%b)
    valid_solution={'bank_number':n,'block_size':b}
    seidel_2d_parameter_set.append(valid_solution)
    return

def log_check_conflict(n, b,d1,N):
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
                    print("log conflict {0}".format(A))
                    return
                else:
                    conflict_set.append(x)

    print("log suceess ,"+"n=%d"%n+" b=%d"%b)
    valid_solution={'bank_number':n,'block_size':b}
    seidel_2d_parameter_set.append(valid_solution)
    return

def get_Bicubic(bmax,nmax,Bicubic_width):
    b = 1
    while b < bmax:
        n = 1
        while n < nmax:
            Bicubic_check_conflict(n, b, Bicubic_width, Bicubic_width - 1)
            n = n * 2
        b = b * 2
    Bicubic_df = pd.DataFrame(Bicubic_parameter_set, columns=['bank_number', 'block_size'], dtype=int)
    Bicubic_df.to_csv('./Bicubic.csv')

def get_Denoise(bmax,nmax,Denoise_width):
    b = 1
    while b < bmax:
        n = 1
        while n < nmax:
            Denoise_check_conflict(n, b, Denoise_width , Denoise_width - 1)
            n = n + 1
        b = b + 1
    Denoise_df= pd.DataFrame(Denoise_parameter_set, columns=['bank_number', 'block_size'], dtype=int)
    Denoise_df.to_csv('./Denoise.csv')

def get_jacobi_2d(bmax,nmax,jacobi_2d_width):
    b = 1
    while b < bmax:
        n = 1
        while n < nmax:
            jacobi_2d_check_conflict(n, b, jacobi_2d_width , jacobi_2d_width - 1)
            n = n * 2
        b = b * 2
    jacobi_2d_df= pd.DataFrame(jacobi_2d_parameter_set, columns=['bank_number', 'block_size'], dtype=int)
    jacobi_2d_df.to_csv('./jacobi_2d.csv')

def get_seidel_2d(bmax,nmax,seidel_2d_width):
    b = 1
    while b < bmax:
        n = 1
        while n < nmax:
            seidel_2d_check_conflict(n, b, seidel_2d_width , seidel_2d_width - 1)
            n = n * 2
        b = b * 2
    seidel_2d_df= pd.DataFrame(seidel_2d_parameter_set, columns=['bank_number', 'block_size'], dtype=int)
    seidel_2d_df.to_csv('./seidel_2d.csv')

def get_log(bmax,nmax,log_width):
    b = 1
    while b < bmax:

        n = 1
        while n < nmax:
            log_check_conflict(n, b, log_width , log_width - 1)
            n = n * 2
        b = b * 2
    log_df= pd.DataFrame(log_parameter_set, columns=['bank_number', 'block_size'], dtype=int)
    log_df.to_csv('./log.csv')

if __name__ == "__main__":
    # block的最大值
    bmax = 32
    # bank的最大值
    nmax = 32

    Bicubic_parameter_set = []
    Denoise_parameter_set = []
    jacobi_2d_parameter_set = []
    seidel_2d_parameter_set = []

    Bicubic_width = 512
    Denoise_width = 512
    jacobi_2d_width  = 250
    seidel_2d_width  = 512
    log_width     = 512

    get_Denoise(bmax=Denoise_width, nmax=nmax, Denoise_width=Denoise_width)
    get_Bicubic(bmax=Bicubic_width, nmax=nmax, Bicubic_width=Bicubic_width)
    get_jacobi_2d(bmax=jacobi_2d_width, nmax=nmax, jacobi_2d_width=jacobi_2d_width)
    get_seidel_2d(bmax=seidel_2d_width, nmax=nmax, seidel_2d_width=seidel_2d_width)
    get_log(bmax=log_width, nmax=nmax , log_width=log_width)

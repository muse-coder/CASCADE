import pandas as pd
import os
from patterns.Fdtd_2d   import *    
from patterns.Sobel     import *
from patterns.Bicubic   import *   
from patterns.Denoise   import *
from patterns.Jacobi_2d import *   
from patterns.Log       import *   
from patterns.Seidel_2d import *   

if __name__ == "__main__":
    # block的最大值
    bmax = 32
    # bank的最大值
    nmax = 32
    if not os.path.exists('./result'):
        os.mkdir('./result')

    Bicubic_width = 300
    Denoise_width = 300
    Jacobi_2d_width  = 250
    Seidel_2d_width  = 310
    Log_width     = 310
    Fdtd_2d_width = 310
    Sobel_width   = 310

    get_Denoise(bmax=Denoise_width, nmax=nmax, Denoise_width=Denoise_width)
    get_Bicubic(bmax=Bicubic_width, nmax=nmax, Bicubic_width=Bicubic_width)
    get_Jacobi_2d(bmax=Jacobi_2d_width, nmax=nmax, Jacobi_2d_width=Jacobi_2d_width)
    get_Seidel_2d(bmax=Seidel_2d_width, nmax=nmax, Seidel_2d_width=Seidel_2d_width)
    get_Log(bmax=Log_width, nmax=nmax , Log_width=Log_width)
    get_Fdtd_2d(bmax=Fdtd_2d_width, nmax=nmax , Fdtd_2d_width=Fdtd_2d_width)
    get_Sobel(bmax=Sobel_width, nmax=nmax , Sobel_width=Sobel_width)
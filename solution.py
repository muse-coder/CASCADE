import pandas as pd
import os
from  patterns import Fdtd_2d       
from  patterns import Sobel     
from  patterns import Bicubic      
from  patterns import Denoise   
from  patterns import Jacobi_2d    
from  patterns import Log          
from  patterns import Seidel_2d    
from  patterns import Split     
if __name__ == "__main__":
    # block的最大值
    bmax = 2
    # bank的最大值
    nmax = 32
    if not os.path.exists('./result'):
        os.mkdir('./result')

    Bicubic_width    = 256 + 2
    Denoise_width    = 256 + 3
    Jacobi_2d_width  = 256 + 2
    Fdtd_2d_width    = 256 + 2
    
    Sobel_width      = 256 + 3
    Seidel_2d_width  = 256 + 2
    Log_width        = 256 + 2
    iteration_domain = 255
    Split_width      = 256
    Denoise.get_Denoise     (bmax=bmax, nmax=nmax, Denoise_width=Denoise_width )
    Bicubic.get_Bicubic     (bmax=bmax, nmax=nmax, Bicubic_width=Bicubic_width )
    Jacobi_2d.get_Jacobi_2d (bmax=bmax, nmax=nmax, Jacobi_2d_width=Jacobi_2d_width )
    Seidel_2d.get_Seidel_2d (bmax=bmax, nmax=nmax, Seidel_2d_width=Seidel_2d_width )
    Log.get_Log             (bmax=bmax, nmax=nmax , Log_width=Log_width )
    Fdtd_2d.get_Fdtd_2d     (bmax=bmax, nmax=nmax , Fdtd_2d_width=Fdtd_2d_width )
    Sobel.get_Sobel         (bmax=bmax, nmax=nmax , Sobel_width=Sobel_width )
    # Split.get_Split         (bmax=bmax, nmax=nmax , Split_width=Split_width )
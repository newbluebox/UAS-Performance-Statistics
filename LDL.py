import numpy as np

data = [ [ 580.9837229013194, -62.20890898342024, -89.05144434071254, -290.4918614506597, 31.104454491710122, 44.52572217035626 ],
[-62.20890898342025, 7.087676016182128, 15.766843361585662, 31.104454491710122, -3.5438380080910643, -7.88342168079283 ],
[-89.05144434071252, 15.76684336158566, 25566.97148930695, 44.52572217035628, -7.883421680792831, -12783.485744653475 ],
[-290.49186145065966, 31.104454491710122, 44.525722170356275, 290.49186145065977, -31.104454491710136, -44.525722170356275 ],
[31.104454491710122, -3.543838008091064, -7.883421680792832, -31.104454491710133, 3.543838008091065, 7.883421680792832 ],
[44.52572217035626, -7.88342168079283, -12783.485744653475, -44.52572217035628, 7.883421680792831, 12783.485744653475 ] ]

A = np.array( data )
L = np.zeros_like( A )
D = np.zeros_like( A )

dim = 6

for j in range( dim ) :
    if j == 0 :
        D[ 0, 0 ] = A[ 0, 0 ]
#plot mandelbrot, choose zoom point and width
import matplotlib.pyplot as plt
import numpy as np

def scales (A:np.array, center:float = [0,0], width:float = 4):
    realmin = center[0]-width/2
    realmax = center[0]+width/2
    imgmin = center[1]-width/2
    imgmax = center[1]+width/2
    realpos = np.arange(realmin,realmax,(realmax-realmin)/len(A))
    imgpos = np.arange(imgmin,imgmax,(imgmax-imgmin)/len(A))
    Aindex = np.array(range(len(A)))
    for i in Aindex:
        for j in Aindex:
            A[i,j] = complex(realpos[i],imgpos[j])
    return A

def mandel (z, c = 0):
    z = z**2 + c
    return z

def get_iter(c:complex, thresh:int =4, max_steps:int =30) -> int:
    z=c
    i=1
    while i<max_steps and (z*z.conjugate()).real<thresh:
        z = mandel(z, c)
        i+=1
    return i

def parker (A):
    n = len(A)
    S = np.zeros((n,n))
    Aindex = np.array(range(len(A)))
    for i in Aindex:
        for j in Aindex:
            S[i,j] = get_iter(A[i,j])
    return S

n = 100
A = np.zeros((n,n),dtype=np.complex_)
A = scales(A, [0,0], 4)
S = parker(A)

plt.imshow(S, cmap="magma")
#plt.axis("off")
plt.savefig('zoom.png')
plt.show()

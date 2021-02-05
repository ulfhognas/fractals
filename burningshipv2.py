import matplotlib.pyplot as plt
import numpy as np

n =  1000
A = np.zeros((n,n),dtype=np.complex_)

def scales (A, min = -2.5, max = 2.5):
    pos = np.arange(min,max,(max-min)/len(A))
    Aindex = np.array(range(len(A)))
    for i in Aindex:
        for j in Aindex:
            A[i,j] = complex(pos[i],pos[j])
    return A

A = scales(A)

def mandel (z, c = 0):
    z = (abs(z.real)+abs(z.imag)*1j)**2 + c
    return z

def get_iter(c:complex, thresh:int =4, max_steps:int =64) -> int:
    z=c
    i=1
    while i<max_steps and (z*z.conjugate()).real<thresh:
        z= mandel(z, c)
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

print(type(parker(A)))

# print(parker(A)[60,60])
#
# print(get_iter(complex(0.4,0.4)))
#
# print(A[60,60])

S = parker(A)

plt.imshow(S, cmap="hot")
plt.savefig('burningship.png', dpi = 300)
plt.axis("off")
plt.show()

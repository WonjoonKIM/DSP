import numpy as np
import matplotlib.pyplot as plt
from  matplotlib import patches, rcParams

def convolve_m(x,nx,h,nh): # n, h는 샘플 시퀀스 nx,nh는 순서 시퀀스
    nyb=min(nx)+min(nh)
    nye=max(nx)+max(nh)
    ny=np.arange(nyb,nye+1)
    y=np.convolve(x,h)
    return y,ny

def impseq(n0,n1,n2):
    N=n2-n1+1 # N의 범위
    x=np.zeros(N)
    n=np.arange(N)
    for i in range(N):
        if i==n0: x[i]=1
    return x,n

def stepseq(n0,n1,n2):
    N=n2-n1+1 # N의 범위
    x=np.zeros(N)
    n=np.arange(N)
    for i in range(N):
        if i-n0>=0: x[i]=1
    return x,n


def zplane(b,a):    
    ax = plt.subplot(111)     #그림창을 만들고 단위원을 그린다.
    uc = patches.Circle((0,0), radius=1, fill=False,
                        color='black', ls='dashed')
    ax.add_patch(uc)
    if np.max(b) > 1:     #계수값 정규화
        kn = np.max(b)
        b = b/float(kn)
    else:
        kn = 1
    if np.max(a) > 1:
        kd = np.max(a)
        a = a/float(kd)
    else:
        kd = 1
        
    p = np.roots(a)     #극점, 영점 결정
    z = np.roots(b)
    k = kn/float(kd)
    
    t1 = plt.plot(z.real, z.imag, 'go', ms=10)     #영점 그리고 표시하기
    plt.setp( t1, markersize=10.0, markeredgewidth=1.0,
              markeredgecolor='k', markerfacecolor='g')

    t2 = plt.plot(p.real, p.imag, 'rx', ms=10)     #극점 그리고 표시하기
    plt.setp( t2, markersize=12.0, markeredgewidth=3.0,
              markeredgecolor='r', markerfacecolor='r')
    plt.title("Pole-Zero Diagram"); plt.grid()

    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    r = 1.5; plt.axis('scaled'); plt.axis([-r, r, -r, r])   #눈금 값 쓰기
    ticks = [-1, -.5, .5, 1]; plt.xticks(ticks); plt.yticks(ticks)












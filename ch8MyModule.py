import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from scipy.signal import chirp
from matplotlib import patches, rcParams


def zplane(b, a):
    ax = plt.subplot(111)  # 그림창을 만들고 단위원을 그린다.
    uc = patches.Circle((0, 0), radius=1, fill=False,
                        color='black', ls='dashed')
    ax.add_patch(uc)
    if np.max(b) > 1:  # 계수값 정규화
        kn = np.max(b)
        b = b / float(kn)
    else:
        kn = 1
    if np.max(a) > 1:
        kd = np.max(a)
        a = a / float(kd)
    else:
        kd = 1

    p = np.roots(a)  # 극점, 영점 결정
    z = np.roots(b)
    k = kn / float(kd)

    t1 = plt.plot(z.real, z.imag, 'go', ms=10)  # 영점 그리고 표시하기
    plt.setp(t1, markersize=10.0, markeredgewidth=1.0,
             markeredgecolor='k', markerfacecolor='g')

    t2 = plt.plot(p.real, p.imag, 'rx', ms=10)  # 극점 그리고 표시하기
    plt.setp(t2, markersize=12.0, markeredgewidth=3.0,
             markeredgecolor='r', markerfacecolor='r')
    plt.title("Pole-Zero Diagram");
    plt.grid()

    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    r = 1.5;
    plt.axis('scaled');
    plt.axis([-r, r, -r, r])  # 눈금 값 쓰기
    ticks = [-1, -.5, .5, 1];
    plt.xticks(ticks);
    plt.yticks(ticks)


def zmapping(bZ, aZ, Nz, Dz):
    bNzord = (len(bZ) - 1) * (len(Nz) - 1)
    aDzord = (len(aZ) - 1) * (len(Dz) - 1)
    bzord = len(bZ) - 1;
    azord = len(aZ) - 1
    bhp = np.zeros(bNzord + 1)
    for k in range(bzord + 1):
        pln = [1]
        for l in range(k):
            pln = np.convolve(pln, Nz)
        pld = [1]
        for l in range(bzord - k):
            pld = np.convolve(pld, Dz)
        bhp = bhp + bZ[k] * np.convolve(pln, pld)
    ahp = np.zeros(aDzord + 1)
    for k in range(azord + 1):
        pln = [1]
        for l in range(k):
            pln = np.convolve(pln, Nz)
        pld = [1]
        for l in range(azord - k):
            pld = np.convolve(pld, Dz)
        ahp = ahp + aZ[k] * np.convolve(pln, pld)
    return bhp, ahp


def Frequency_response_Signal_filtering(b, a):
    system = [b, a, 1]
    n, hn = signal.dimpulse(system)
    hh = hn[0];
    M = len(hh)
    hn = np.zeros(M)
    for i in range(M):
        pp = hh[i]
        hn[i] = pp[0]
    t = np.linspace(0, 1, 5000)
    xn = chirp(t, f0=10, t1=0.2, f1=500, method="linear")
    yn = np.convolve(hn, xn)
    plt.plot(yn, "b");
    plt.xlim(0, 5000)
    plt.title("Frequency Filtering Result")
    plt.xlabel("Samples(Frequency(0~500[Hz]))");
    plt.grid()
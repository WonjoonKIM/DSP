def IIR_direct_1(x):     #제1 직접형 IIR 필터
    y=[0]*tn
    v=[0]*tn
    for n in range(4, len(x)):
        v[n]=1/16*x[n]-3/16*x[n-1]+11/16*x[n-2]-27/16*x[n-3]+18/16*x[n-4]
        y[n]=v[n]-12/16*y[n-1]-2/16*y[n-2]+4/16*y[n-3]+1/16*y[n-4]
    return y
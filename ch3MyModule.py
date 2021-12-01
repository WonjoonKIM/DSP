import numpy as np

def impseq(n0,n1,n2): #단위샘플시퀀스
    N=n2-n1+1 #데이터수
    n=np.arange(N) #순서시퀀스
    xn=np.zeros(N) #데이터어레이 설정
    
    for i in range(N): #단위 샘플 시퀀스 생성"
        if(i+n1)==n0:
            xn[i]=1
    return xn 

def stepseq(n0,n1,n2): #단위계단시퀀스
    N=n2-n1+1 
    n=np.arange(N)
    xn=np.zeros(N)
    
    for i in range(N): #단위 계단 시퀀스 설정
        if(i+n1)>=n0:
            xn[i]=1
    
    return xn

def sigadd(n1,x1,n2,x2): #신호 덧셈
    nk=np.arange(min(min(n1),min(n2)),max(max(n1),max(n2))+1) #전체 시퀀스 축, 좌항부터 우항까지의 배열을 저장
    N=len(nk) #전체 시퀀스 길이
    y1=np.zeros(N) #x1을 위한 영점자리 맞춤(순서시퀀스)
    y2=np.zeros(N) #x2을 위한 영점자리 맞춤
    aa=abs(min(min(n1), min(n2))) # 자리맞춤이동폭

    n1=n1+aa #자리이동
    n2=n2+aa #자리이동

    y1[int(min(n1)):int(max(n1)+1)] = x1 #샘플저장
    y2[int(min(n2)):int(max(n2) + 1)] = x2  # 샘플저장
    y=y1+y2

    return nk,y,y1,

def sigmult(n1,x1,n2,x2): #신호곱셈
    n=np.arange(min(min(n1),min(n2)), max(max(n1),max(n2))+1) #전체 시퀀스 축
    N=len(n)
    y1=np.zeros(N) # x1 영점 자리맞춤
    y2=np.zeros(N) # x2 영점 자리맞춤
    aa=abs(min(min(n1),max(n1), min(n2), max(n2)))

    y1[min(n1)+aa:max(n1)+aa+1]=x1
    y2[min(n2) + aa:max(n2) + aa + 1] = x2
    y=y1.T*y2 #샘플대샘플 곱샘

    return n,y,y1,y2

def sigshift(m, x, k): #신호이동
    n=m+k
    y=x #신호복사

    return n,y

def sigfold(n1,x1): #신호반전
    N=len(n1)
    y=np.zeros(N)
    n=np.zeros(N)
    for i in range(N):
        y[i]=x1[N-1-i] #샘플교환
        n[i]=1*n1[N-1-i]

    return n,y
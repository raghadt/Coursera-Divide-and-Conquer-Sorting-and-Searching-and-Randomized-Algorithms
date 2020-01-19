
n=5678
m=1234



def karatsuba(n,m):
    
    a_len = int(len(str(n))/2)
    b_len = int(len(str(n)))
    

    a = int(str(n)[:a_len])
    b = int(str(n)[a_len:b_len])
    
    
    c_len = int(len(str(m))/2)
    d_len = int(len(str(m)))

    c = int(str(m)[:c_len])
    d = int(str(m)[c_len:d_len])
    
    s_1 = a*c
    s_2 = b*d
    s_3 = (a+b)*(c+d)
    s_4 = s_3 - s_1 - s_2

    s_5 = ( 10**b_len * s_1) + (10**a_len * s_4) + s_2
    print(s_5)


    karatsuba(n,m)
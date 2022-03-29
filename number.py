"""
数論に関係する関数などを定義。
"""


def fast_exp(x,n):
    # x**nを計算。
    s = "{:b}".format(n)
    y = x
    for i in range(1,len(s)):
        y = y**2
        if(s[i] == "1"):
            y = y*x            
    return y

def fast_exp_mod(x,n,p):
    # x**n (mod p) を計算。
    s = "{:b}".format(n)
    y = x
    for i in range(1,len(s)):
        y = y**2 % p
        if(s[i] == "1"):
            y = y*x % p            
    return y

def test_fast_exp_mod():
    print(fast_exp_mod(2,1001,7))
    
def main():
    test_fast_exp_mod()

if __name__ == '__main__':
    main()

"""
 ECはElliptic Curve(楕円曲線)の頭字語
"""

from number import *

class Integer2D:
    # 整数格子上の点を表すクラス。
    # x,yは共に整数である。
    # (x,y) == (None,None)の場合に無限点を表す。
    def __init__(self,x=0,y=0):
        # 整数或いは無限点であるか否かチェック
        assert(isinstance(x,int) or x == None)
        assert(isinstance(y,int) or y == None)
        
        self.x = x
        self.y = y        
    def __str__(self):
        if(self.x == None and self.y == None):
            return "(inf)"
        else:
            return "(%d,%d)"%(self.x,self.y)
        
    def is_infinity(self):
        return (self.x == None and self.y == None)
    
    @staticmethod
    def infinity():
        return Integer2D(None,None)
    
class EC:
    # 楕円曲線:y^2 = x^3 + a*x + b* mod (p)を表すクラス。
    def __init__(self,a,b,p):
       self.a = a
       self.b = b
       self.p = p
       
       assert(self.p > 3)
       # assert(self.p is a prime)       
       assert(self.is_in_Zp(self.a))
       assert(self.is_in_Zp(self.b))
       assert(self.ec_condition(self.a,self.b))

    def double_and_add(self,P,n):
        # 点Pと整数nが与えられたとき、n*Pを計算してその値を返す。
        assert(isinstance(P,Integer2D))
        assert(self.is_valid_point(P))
        assert(isinstance(n,int))

        d = "{:b}".format(n)
        T = P

        for i in range(1,len(d)):
            T = self.doubling(T)
            if(d[i] == "1"):
                T = self.addition(T,P)
                
        return T
    
    def addition(self,P1,P2):
        assert(isinstance(P1,Integer2D))
        assert(isinstance(P2,Integer2D))
        assert(self.is_valid_point(P1))
        assert(self.is_valid_point(P2))
        
        if(P1.x == P2.x):
            return Integer2D.infinity()

        delta_x = (P2.x - P1.x) % self.p
        s = ((P2.y - P1.y)*self.inverse(delta_x)) % self.p
        x3 = (s**2 - P1.x - P2.x) % self.p
        y3 = (s*(P1.x - x3) - P1.y) % self.p

        return Integer2D(x3,y3)

    def doubling(self,P):
        assert(isinstance(P,Integer2D))
        assert(self.is_valid_point(P))

        y_2 = P.y*2 % self.p
        s = ((3*P.x**2 + self.a)*self.inverse(y_2)) % self.p
        x3 = (s**2 - 2*P.x) % self.p
        y3 = (s*(P.x - x3) - P.y) % self.p

        return Integer2D(x3,y3)

    def negation(self,P):
        return Integer2D(P.x,self.p - P.y)
    
    def inverse(self,x):
        # y*x = 1 (mod P)を満たすようなyを返す。
        assert(0 <= x and x < self.p)
        # TODO: 最適化
        #return (x**(self.p-2)) % self.p # Fermat's little Theoremを使用。
        # Fermat's little Theoremを使用。
        return fast_exp_mod(x,self.p-2,self.p)
    
    def is_in_Zp(self,x):
        # xが{0,1,...,p-1}に含まれるか否かチェック
        return (0 <= x and x < self.p)

    def is_valid_point(self,P):
        # 点Pが楕円曲線上にあるか否かをチェック。
        test = (P.x**3 + self.a*P.x + self.b - P.y**2) % self.p
        return (test == 0)
    
    def ec_condition(self,a,b):
        # a,bは楕円曲線の条件である(4*(a**3) + 27*(b**2) != 0 (mod P))
        # を満たすか否かをチェック。
        # 満たす場合にTrue、そうでない場合にFalseを返す。
        val = 4*a**3 + 27*b**2
        return (val % self.p != 0)

def test1():
    ec = EC(2,2,17)
    P = Integer2D(5,1)
    Q = ec.doubling(P)
    print(P) # (5,1)
    print(Q) # (6,3)
    print(ec.is_valid_point(Q))

def test2():
    ec = EC(2,2,17)
    P = Integer2D(5,1)
    Q = ec.doubling(P)
    print(P)
    print(Q)    
    while(not Q.is_infinity()):
        Q = ec.addition(Q,P)
        print(Q)

def test3():
    ec = EC(2,2,17)
    P = Integer2D(5,1)
    Q= ec.double_and_add(P,13)
    print(Q)
    
def main():
    #test1()
    test2()
    test3()
    
if __name__ == '__main__':
    main()

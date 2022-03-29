from ec import *

class NISTP224(EC):
    # [注意] 安全ではない!!
    # http://safecurves.cr.yp.to/
    def __init__(self):
        p = 2^224 - 2^96 + 1
        b = 18958286285566608000408668544493926415504680968679321075787234672564
        a = -3

        # Zpに含まれるように調整。
        a %= p 
        b %= p
        
        super().__init__(a,b,p)
        
def main():
    ecc = NISTP224()
    
if __name__ == '__main__':
    main()

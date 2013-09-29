from math import sqrt
def detect_triangle(a,b,c):
    delta = 0.05
    # check type of input
    
    
    if ( ( not type(a) is float ) and ( not type(a) is int ) ) or ( ( not type(b) is float ) and ( not type(b) is int ) ) or ( ( not type(c) is float ) and ( not type(c) is int ) ) :  
        check = False
        return "Sai kieu"
    else : 
        a = float (a)
        b = float (b)
        c = float (c)
        check = True
        
        
        
    # check range of input
    if check :
        max = float( 2**32)
        if  not (a < max and b<max and c<max and a >0 and b>0 and c>0) :
            check = False
            return "Sai mien gia tri"
            
                
    if check :
    # kiem tra co phai la tam giac hay khong 
        if not ( a < b+c and b < a+c and c< a+b ) : 
            check = False
            return "Khong phai tam giac"
            
            
            
    #     Xac dinh la tam giac gi        
    if check :
        #    TH1 : Tam giac deu
        if ( a==b and b==c and c==a ) :
            return "Tam giac deu"
            
            
            # co 2 canh bang nhau
        elif ( a==b or b==c or c==a ) :    
            # TH2 : Tam giac vuong can
            #if  abs( a - sqrt(b**2+c**2))<=delta or abs( b - sqrt(a**2+c**2))<=delta or abs( c - sqrt(b**2+a**2) )<=delta  :
            if  ( b==c and abs( a - sqrt(2*b**2))<=delta) or ( a==c and abs( b - sqrt(2*a**2))<=delta ) or ( a==b and  abs( c - sqrt(2*b**2) )<=delta )  :
                return "Tam giac vuong can"
            
                
            # TH3 : Tam giac can    
            else :
               
                return "Tam giac can"
                # TH4 : Tam giac vuong        
        elif abs( a - sqrt(b**2+c**2))<=delta or abs( b - sqrt(a**2+c**2))<=delta or abs( c - sqrt(b**2+a**2) )<=delta  :
                    return "Tam giac vuong"
               
                    
            #TH5 : Tam giac thuong        
        else :
                return "Tam giac thuong"
               
                











            
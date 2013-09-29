'''
Created on Sep 24, 2013

@author: Toan
'''
import math,unittest
from triangle import detect_triangle

class Test(unittest.TestCase):
    # Kiem thu kieu gia tri
        def testSaiKieu1(self):
            self.assertMultiLineEqual(detect_triangle( "asdasd"    ,3.0        ,5.0), 'Sai kieu','Sai truong hop kieu' )  
        def testSaiKieu2(self):       
            self.assertMultiLineEqual(detect_triangle(    3.0 ,"1"       ,5.0), 'Sai kieu','Sai truong hop kieu' ) 
        def testSaiKieu3(self):       
            self.assertMultiLineEqual(detect_triangle(    3.0 ,4       ,'2323'), 'Sai kieu','Sai truong hop kieu' )      
    # Kiem thu Mien gia tri
        def testSaiMienGiaTri1(self):
            self.assertMultiLineEqual(detect_triangle( 2.0**32    ,3.0        ,5.0), 'Sai mien gia tri', 'Sai truong hop mien gia tri')  
        def testSaiMienGiaTri2(self):    
            self.assertMultiLineEqual(detect_triangle( -3.0        ,3.0        ,5.0), 'Sai mien gia tri', 'Sai truong hop mien gia tri')
        def testSaiMienGiaTri3(self):    
            self.assertMultiLineEqual(detect_triangle( 0        ,3.0        ,5.0), 'Sai mien gia tri', 'Sai truong hop mien gia tri')    
        def testSaiMienGiaTri4(self):
            self.assertMultiLineEqual(detect_triangle( 2.0**32    ,2.0**32 + 5        ,5.0), 'Sai mien gia tri', 'Sai truong hop mien gia tri')    
        def testSaiMienGiaTri5(self):
            self.assertMultiLineEqual(detect_triangle( 2.0**32    ,2.0**32 + 5        ,2.0**32 + 10), 'Sai mien gia tri', 'Sai truong hop mien gia tri')    
        def testSaiMienGiaTri6(self):    
            self.assertMultiLineEqual(detect_triangle( 0        ,0        ,0), 'Sai mien gia tri', 'Sai truong hop mien gia tri')    
    # Kiem thu tam giac giac vuong can    
        def testVuongCan1(self): 
            self.assertMultiLineEqual(detect_triangle( 3.0         ,3.0        ,math.sqrt(18)),  'Tam giac vuong can',   'Sai truong hop tam giac vuong can')
        def testVuongCan2(self):     
            self.assertMultiLineEqual(detect_triangle( 4.2426406*2**16         ,3.0*2**16        ,3.0*2**16),  'Tam giac vuong can',   'Sai truong hop tam giac vuong can')
        def testVuongCan3(self):     
            self.assertMultiLineEqual(detect_triangle(3.0*2**29 , math.sqrt(18)*2**29       ,3.0*2**29),  'Tam giac vuong can',   'Sai truong hop tam giac vuong can')
    # Kiem thu tam giac vuong        
        def testVuong1(self):
            self.assertMultiLineEqual(detect_triangle( 3.0         ,4.0        ,5.0),  'Tam giac vuong',       'Sai truong hop tam giac vuong')
        def testVuong2(self):    
            self.assertMultiLineEqual(detect_triangle( 4.0         ,5.0        ,3.0),  'Tam giac vuong',       'Sai truong hop tam giac vuong')
        def testVuong3(self):    
            self.assertMultiLineEqual(detect_triangle( 5.0         ,3.0        ,4.0),  'Tam giac vuong',       'Sai truong hop tam giac vuong')
        def testVuong4(self):    
            self.assertMultiLineEqual(detect_triangle( 5.0*2**29         ,3.0*2**29        ,4.0*2**29),  'Tam giac vuong',       'Sai truong hop tam giac vuong')    
    # Kiem thu tam giac deu    
        def testDeu(self):
            self.assertMultiLineEqual(detect_triangle( 3.0         ,3.0        ,3.0),  'Tam giac deu',         'Sai truong hop tam giac deu')
            
    # Kiem thu tam giac can    
        def testCan1(self):
            self.assertMultiLineEqual(detect_triangle( 3.0         ,3.0        ,5.0),  'Tam giac can',         'Sai truong hop tam giac can')
        def testCan2(self):    
            self.assertMultiLineEqual(detect_triangle( 2.0**31     ,2.0**31    ,6),    'Tam giac can',         'Sai truong hop tam giac can')
        def testCan3(self):    
            self.assertMultiLineEqual(detect_triangle( 2.0**31     ,1 , 2.0**31    ),    'Tam giac can',         'Sai truong hop tam giac can')    
        def testCan4(self):    
            self.assertMultiLineEqual(detect_triangle(      1,2.0**31 , 2.0**31    ),    'Tam giac can',         'Sai truong hop tam giac can')    
    # Kiem thu Khong phai tam giac          
        def testKhongPhaiTamGiac1(self):
            self.assertMultiLineEqual(detect_triangle( 1.0        ,2.0        ,5.0), 'Khong phai tam giac', 'Sai truong hop khong phai tam giac')
        def testKhongPhaiTamGiac2(self):    
            self.assertMultiLineEqual(detect_triangle( 20.0        ,3.0        ,1.0), 'Khong phai tam giac', 'Sai truong hop khong phai tam giac')
    # Kiem thu tam giac thuong    
        def testTamGiacThuong(self): 
            self.assertMultiLineEqual(detect_triangle( 6        ,4        ,5.0), 'Tam giac thuong', 'Sai truong hop Tam giac thuong')
                
if __name__ == "__main__":
    unittest.main()
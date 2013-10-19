'''
Created on Oct 1, 2013

@author: Toan
'''
import unittest
import inspect
import itertools
from input import main
# Kiem tra cac day co trung nhau hay khong
def checkTwoArray(arr_min,arr_max):
    for i in xrange(0, len(arr_min)-1) :
        if arr_min[i] > arr_max[i] or arr_max[i] > arr_min[i+1] :
            return False
    if arr_min[len(arr_min)-1] > arr_max[len(arr_min)-1] :
        return False
    return True   
# Sap xep lai day           
def sortTwoArray(arr1, arr2):
    for i in xrange(0, len(arr1) -1 ):
        for j in xrange( i, len(arr1) ):
            if arr1[i] > arr1[j] :
                # swap in arr1
                temp = arr1[j]
                arr1[j] = arr1[i]
                arr1[i] = temp
                # swap in arr2
                temp = arr2[j]
                arr2[j] = arr2[i]
                arr2[i] = temp

class tempVar(object):
    range = 0
    array_min = []
    array_max = []   
    def __init__(self,range):
        self.range = range
    def add_min(self,min):
        self.array_min.append(min)
    def add_max(self,max):
        self.array_max.append(max)

# Get doc in main
def MainRange():
    a = inspect.getdoc(main)
    a = inspect.cleandoc(a)
    b= a.splitlines()
    line1 = b[0]
    z = inspect.getargspec(main)
    param_number =  z[0].__len__()
    #print line1
    count_i = 0
    
    RangeVariable = []
     
    
    
    while count_i < param_number :
        line1 = b[count_i]
        range = line1.split(':')[1]
        range = inspect.cleandoc(range)
    
        range1 = range.split(']')
        i = 0
        ## Xac dinh cac khoang cua day
        array_min = []
        array_max = []
        ## Tao bien luu cac khoang 
        temp_var = tempVar(len(range1)-1)
        ## Nap cac gia tri vao
        while i < len(range1)-1 :
            temp_range = range1[i]
            temp_min = temp_range[ temp_range.find('[')+1 : temp_range.find(';')      ]
            temp_min = float(temp_min)
            array_min.append( temp_min )
            
            temp_max = temp_range[ temp_range.find(';')+1 : temp_range.__len__()      ]
            temp_max = float(temp_max)
            array_max.append( temp_max )
            i+=1
        i = 0
        while i < len(array_min) :
            i+=1
        temp_var.array_min = array_min
        temp_var.array_max = array_max
        RangeVariable.append(temp_var)    
        count_i+=1  
    i = 0
    
    while i< len(RangeVariable):
        temp = RangeVariable[i]
        sortTwoArray(temp.array_max, temp.array_min)
        i+=1
         
    return RangeVariable
class TestSequense(unittest.TestCase):
    pass
def test_generator(*args):
    def test(self):
        self.assertEqual(input.main(*args),-1)
    return test
if __name__ == "__main__":
    temp  = MainRange()
    check = True
    list = []
    # Check input
    for i in xrange( 0, len(temp)):
        temp1 = temp[i]
        temp_list = []
        array_max = temp1.array_max
        array_min = temp1.array_min
        for j in xrange( 0,  len (array_min)):
            temp_list.append(array_min[j])
        if not checkTwoArray(array_min, array_max) : 
            check = False
            break
        list.append(temp_list)
    if not check :
        raise Exception('Wrong input')
    else:
        print 'Right input'
    for list_item in itertools.product(*list) :       
        test_name   = 'test_'+str(list_item)
        test = test_generator(*list_item)
        setattr(TestSequense,test_name,test) 
    unittest.main()    

    

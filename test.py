from main import sort

def test_sort():
    print(sort(100, 100, 100, 10))  
    print(sort(10, 10, 10, 25))      
    print(sort(160, 50, 50, 5))       
    print(sort(200, 200, 200, 30))    
    print(sort(50, 50, 50, 10))        
    print(sort(100, 100, 100, 20))     
    print(sort(150, 10, 10, 19.9))     
    print(sort(10, 10, 10, 19.99))     
    print(sort(10, 10, 10, 20))        
    print(sort(150, 150, 150, 20))     

    try:
        print(sort(-10, 10, 10, 5))  
    except ValueError as e:
        print("Error:", e)

    try:
        print(sort("a", 10, 10, 5))   
    except ValueError as e:
        print("Error:", e)

test_sort()


def square_numbers(n):    
    for i in range(n):    
        yield i**2    
        
generator = square_numbers(5)    
      
for num in generator:    
    print(num)  

from math import *
def calculate_area(geom_type_str, p):
    	
    if geom_type_str == "circle" or  geom_type_str == "square":
        if geom_type_str == "circle":
            a = pi * p ** 2
        elif geom_type_str == "square":
            a = p ** 2
            
        if a < 100 and a >=10:
            return a
        elif a >100:
            print("Too big")
        elif a<10:    
            print("Too small")
    else:
        print("Unsopported geometry type "+ geom_type_str)
	

print()

# import the class CLcomputer
from aufgabeBanu import computer

# define objects, give them the reference 
config1 = computer(1, 950, 100, "T500", "Intel® Core™ i9" , True)
config2 = computer(2, 850, 75, "T300", "Intel® Core™ i7", True)
config3 = computer(3, 750, 50, "T200", "Intel® Core™ i5", False)

# P1 (same PAIR = same RESULT but shorter) 
# print the show_info method for the 3 objects      
for i in range(1,4):
    config=eval(f'config{i}')
    config.show_info()
    
# P2
# print the show_total_price method for the 3 objects
for i in range(1,4):
    config=eval(f"config{i}")
    config.show_total_price()   
    
    # P1
    # config=globals()[f'config{i}']
    # config.show_info()
    
# P1             
# config1.show_info()
# config2.show_info()
# config3.show_info()

# P2
# config1.show_total_price()
# config2.show_total_price()
# config3.show_total_price()
print()
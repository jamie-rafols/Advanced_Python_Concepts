def sum(*args):
    sum = 0
    for item in args:
        sum += item
    return sum
    
print(sum(5,6,7))


def vpair(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} {value}")
        
vpair(name="JJ",age=25,city="manila")
        
        

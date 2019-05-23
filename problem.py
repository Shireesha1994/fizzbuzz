def fin(num=101):
    for i in range(num):
        if(i % 3 == 0):
         	    print("Fizz")
	else:
		    print(i)
	if(i % 5 == 0):
                    print("Buzz")
	else:
	            print("Fin")
	if(i%3==0)and(i%5==0):
		    print("FizzBuzz")
	else:
		    print(i)

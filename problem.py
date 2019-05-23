#creating Funtion for printing 100 numbers
def fin(num=101):
#checking condition for divisible by 3
    for i in range(num):
        if(i % 3 == 0):
         	    print("Fizz")
	else:
		    print(i)
#checking condition for divisible by 5
	if(i % 5 == 0):
                    print("Buzz")
	else:
	            print(i)
#checking condition for divisible by 3 and 5
	if(i%3==0)and(i%5==0):
		    print("FizzBuzz")
	else:
		    print(i)

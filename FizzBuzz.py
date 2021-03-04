def FizzBuzz(*args):
    i = 1
    arr = []
    while i <= 100:
        if(i%3 == 0 and i%5==0):
            arr.append("FizzBuzz")
        elif(i%3 == 0):
            arr.append("Fizz")
        elif(i%5 == 0):
            arr.append("Buzz")
        else:
            arr.append(i)
        i+=1
    print(arr) #last step is to just print all the numbers
    if(type(args[0]) == int):
        return arr[args[0]-1]



FizzBuzz(15)   
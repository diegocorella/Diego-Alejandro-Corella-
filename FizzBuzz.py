for i in range (1,51):
    #si i es multipo de 3 y de 5 --"fizzbuzz"
    #si i es multiplo de 3 y de 5 --"fizz"
    #si i es multiplo de 5--"buzz"
    #si no--imprime i
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)
        print("Fin del programa")
        

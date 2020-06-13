######################calculater########################
while print:
    print("pluse  =  plus")
    print("mainas  =  minas")
    print("maltipal  =  malti")
    print("divide  =  divide")
    print("power  =  power")
    print("simple intrest  =  sint")
    print("to find averge of some number  =    ave")
    a=str(input("inter opretion name    :"))
    
    if a=="plus":
        f1=float(input("inter first number    :  "))
        f2=float(input("inter second number    :  "))
        print(f1+f2)    

    elif a=="minas":
        f1=float(input("inter first number    :  "))
        f2=float(input("inter second number    :  "))
        print(f1-f2)
    elif a=="malti":
        f1=float(input("inter first number    :  "))
        f2=float(input("inter second number    :  "))
        print(f1*f2)   
    elif a=="divide":
        f1=float(input("inter first number    :  "))
        f2=float(input("inter second number    :  "))
        print(f1/f2)     
    elif a=="power":
        f1=float(input("inter first number    :  "))
        f2=float(input("inter second number    :  "))
        print(f1**f2)   
    elif a=="ave":
        sum = 0
        n = int(input("enter no. of elem  "))
        for b in range( 0,n):
   
             b = float(input("enter number   "))
             sum = sum + b
        print(sum/n)     
    elif a=="sint":
        print("simple intest = simint")
        print("if you want find principal amount = pint")
        print("if you want find time             =  tint")
        print("if you want find rate of intrest = rint")
        b=str(input("inter wahat you want to find   "))
        if b=="simint":
             p=float(input("inter principal amount   :  "))
             r=float(input("inter rate of intrest    :  "))
             t=float(input("inter time of            :  "))
             print((p*r*t)/100)
        elif b=="pint":
            r=float(input("inter rate of interst   :"))  
            t=float(input("inter time of           :"))
            i=float(input("inter total interst     :"))   
            print((i*100)/(r*t))
        elif b=="rint":
            p=float(input("interprincipal amount   :"))  
            t=float(input("inter time of           :"))
            i=float(input("inter total interst     :"))   
            print((i*100)/(p*t))    
        elif b=="tint":
            p=float(input("interprincipal amount      :"))  
            r=float(input("inter rate of intrest      :"))
            i=float(input("inter total interst        :"))   
            print((i*100)/(p*r)) 

    else:
        print("ERROR")
        
        
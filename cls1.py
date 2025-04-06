# a=0
# for i in range(3):
#         print(i)
# while 1:
#     a=int(input("Enter any num: "))
#     if a<0:
#         print("Less so ",0)
#     elif a==0:
#         print("Zero")
#     else:
#         print("Positive")
# pass    

# a=0
# status=0
while 1:
        
        status=input("""Enter operation you want to perform: 
                     1.Add(+)
                     2.Subtract(-)
                     3.Multiply(*)
                     4.Division(/
                     5.Modulous(%)
""")
        match status:
            case '3'|'*':
                a=int(input("Enter the any number"))   
                # for a in range(7):
                b=int(input("Enter the any number"))  
               # for a in range(7):
                #for i in range(1):
                print(a,"*",b,a*b)
                for i in range(10):
                    print(a,"*",i,a*i)
            case 2|'-':
                a=int(input("Enter the any number"))  
                b=int(input("Enter the any number"))  
               # for a in range(7):
                #for i in range(1):
                print(a,"-",b,a-b)
            case 1|'+':
                a=int(input("Enter the any number"))  
                b=int(input("Enter the any number"))  
               # for a in range(7):
                #for i in range(1):
                print(a,"+",b,a+b)
            case 4|'/':
                a=int(input("Enter the any number"))  
                b=int(input("Enter the any number"))  
               # for a in range(7):
                #for i in range(1):
                print(a,"/",b,a/b)
            case 5|'%':
                a=int(input("Enter the any number"))  
                b=int(input("Enter the any number"))  
               # for a in range(7):
                #for i in range(1):
                print(a,"%",b,a%b)
            
            

    
    
   
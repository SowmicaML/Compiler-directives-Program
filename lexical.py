""" This is a program to perform lexical analysis for a c program in python

C program to be stored in a file InputProg.c """

#include <stdio.h> 
 #int main()
#{
#    int a , b , c;
#    b= 5 ;
#    c= 6 ;
#    a=b+c;
#    printf("%d",a);
#    return 0;
#}


#opening file
f = open('InputProg.c','r')
#defining the tokens

operator = ['=','+','-','/','*','++','--']
optname=['Assignment Operator','Additon Operator','Substraction Operator','Division Operator','Multiplication Operator','increment Operator', 'Decrement Operator']

header = {'.h': 'header file'}
header_keys = header.keys()

headerfile = {'<stdio.h>':'Standard Input Output Header','<string.h>':'String Manipulation Library'}

macros = {r'#\w+' : 'macro'}
macros_keys = macros.keys()

datatype = ['int','float','double','char','long','short']

size=['2 or 4',4,8,1,8,2]

keyword=['return','for','while','do','if','else','elseif','switch','case','break','continue']

builtin_functions = {'printf':'output operation'}


operators = ['_','`','~','!','@','#','$','%','^','&','*','(',')','|',':',';','{','}','[',']','?',',']

# Flag
dataFlag = False

#function to determine built in functions
def builtinfunc(t):
    for fun in builtin_functions:
        if fun in token:
            print(fun,":Built in function-",builtin_functions[fun])

#function to determine special operators
def spclop(t):
    for el in operators:
        if el in token:
            print(el,"special operator")
#assignment operators
def op(t):
    for asi in operator:
        if asi in token:
            print(asi,optname[operator.index(asi)])
            
i = f.read()#reading from the file
count = 0
program =  i.split('\n')

for line in program:
    count = count+1
    print( "Line #",count,"\n",line,"\n")
    
     
    tokens = line.split(' ')
    tokens=[el for el in tokens if el!='']
    print ("Tokens are",tokens)
    print("\n")
    for token in tokens:
        if token in macros_keys:
            print( "Macro is: ", macros[token])
        if '.h' in token:
            print( "Header File is: ",token, headerfile[token])
        if '()' in token:
            print ("Function named", token)
        if dataFlag == True and ('()' not in token) and (token not in operator) and (token not in operators) and (token not in builtin_functions ) :
            print( token," :Identifier")   
        if token in datatype:
            print (token," :Data Type","  Size=:" ,size[datatype.index(token)],"bytes")
            dataFlag = True
        
        
        builtinfunc(token)
        spclop(token)
        op(token)
        
        if token in keyword:
            print(token,":keyword")
    
        if token.isnumeric():
            print (token,":constant")
            
    dataFlag = False   
    print ("________________________")
    
f.close()

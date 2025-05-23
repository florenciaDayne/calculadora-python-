#Crea una Calculadora

num1= float(input("numero 1: "))
num2= float(input("numero 2: "))
operacion= input("introduce una operacion (+ - * /): ")

match operacion:
    case "+":
        res= num1+num2
    case "-":
        res= num1-num2
    case "*":
        res= num1*num2
    case "/":
        res= num1/num2

print(f"El resultado de {num1} {operacion} {num2} = {res}")
hola
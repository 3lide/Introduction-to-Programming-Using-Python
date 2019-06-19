subtotal, gratuityRate = eval(input("Enter the subtotal and a gratuity rate: "))

gratuity = subtotal * gratuityRate * 0.01
total = subtotal + gratuity

print("The gratuity is {:.2f} and the total is {:.2f}".format(gratuity, total))
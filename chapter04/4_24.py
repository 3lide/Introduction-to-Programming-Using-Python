import random

def getValue(number):
    if number == 0:
        value = 'Ace'
    elif number == 1:
        value = '1'
    elif number == 2:
        value = '2'
    elif number == 3:
        value = '3'
    elif number == 4:
        value = '4'
    elif number == 5:
        value = '5'
    elif number == 6:
        value = '6'
    elif number == 7:
        value = '7'
    elif number == 8:
        value = '8'
    elif number == 9:
        value = '9'
    elif number == 10:
        value = 'Jack'
    elif number == 11:
        value = 'Queen'
    elif number == 12:
        value = 'King'
    return value

def getPainting(number):
    if number == 0:
        painting = 'Spade'
    elif number == 1:
        painting = 'Heart'
    elif number == 2:
        painting = 'Club'
    else:
        painting = 'Diamond'
    return painting

def main():
    guessNumber = random.randint(0, 51)
    valueNumber = guessNumber // 4
    paintingNumber = guessNumber % 4
    value = getValue(valueNumber)
    painting = getPainting(paintingNumber)

    print("The card you picked is the {} of {}".format(value, painting))

if __name__ == "__main__":
    main()

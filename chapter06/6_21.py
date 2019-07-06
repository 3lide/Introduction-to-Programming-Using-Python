def sqrt(n):
    lastGuess = 1
    nextGuess = 2
    while nextGuess - lastGuess > 0.0001:
        lastGuess = nextGuess
        nextGuess = (lastGuess + (n / lastGuess)) / 2
    return nextGuess

print(sqrt(25))
def createGPIOList():
    GPIO = 0
    GPIOs = []
    for i in range(27):
        GPIOs.append(GPIO)
        GPIO = GPIO + 1
    return GPIOs
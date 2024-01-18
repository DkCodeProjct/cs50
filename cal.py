while True:
    fuelFraction = input('Fraction: ')
    try:
        x,y = fuelFraction.split('/')

        newX = int(x)
        newY = int(y)


        devisionOfPrecent = newX / newY
        if devisionOfPrecent <= 1:
            break
    except (ValueError, ZeroDivisionError):
        pass
#mul by 100 to get the % ,, ex:= 1 / 3 * 100 == 33.333333
outPut = devisionOfPrecent * 100

if outPut <= 1:
    print('E')

elif outPut >= 99:
    print('F')

else:
    print('{:.0f}%'.format(outPut)) # round the decimal points in division := 33.333 into 33%

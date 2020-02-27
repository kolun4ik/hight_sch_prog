def odometer(*args):
    distance = 0
    if (len(args) >= 2) and (len(args) % 2 == 0):
        counter = 0
        for value in args:
            if counter == 0:
                distance += value * args[counter + 1]
            elif not counter % 2:
                distance += value * (args[counter + 1] - args[counter - 1])
            counter += 1
        return int(distance)

def odometer(data = list()):
    distance = 0
    if (len(data) >= 2) and (len(data) % 2 == 0):
        for counter, value in enumerate(data):
            if counter % 2 == 0:
                distance += value
        return int(distance)
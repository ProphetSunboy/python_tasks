def what_time_is_it(angle):
    '''
    Given the angle (in degrees) of the hour-hand,
    return the time in 12 hour HH:MM format.
    Rounds down the result to the nearest minute.
    '''
    return f'{str(int((angle * 2) // 60)).zfill(2).replace("00", "12")}:{str(int((angle * 2) % 60)).zfill(2)}'
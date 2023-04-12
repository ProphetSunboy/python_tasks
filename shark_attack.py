def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    if dolphin:
        shark_speed /= 2
    c = 0
    while pontoon_distance > 0:
        pontoon_distance -= you_speed
        shark_distance = shark_distance - shark_speed
        c+=1
        if shark_distance <= 0:
            return 'Shark Bait!'
        
    return 'Alive!',c

print(shark(11, 65, 1, 12, True))
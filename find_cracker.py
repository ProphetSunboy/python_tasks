def find_hack(arr):
    scores = {'A': 30, 'B': 20, 'C': 10, 'D': 5}
    hacked = []
    
    for record in arr:
        if record[1] > 200:
            hacked.append(record[0])
            continue
        true_score = 0
        if len(record[2]) >= 5 and set(record[2]) - {'A', 'B'} == set():
            true_score += 20
        for grade in record[2]:
            true_score += scores.get(grade, 0)
        if true_score > 200: true_score = 200
        if true_score != record[1]:
            hacked.append(record[0])
    return hacked
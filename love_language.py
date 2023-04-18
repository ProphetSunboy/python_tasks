def love_language(partner, weeks):
    languages = ['words', 'acts', 'gifts', 'time', 'touch', 'acts']
    responses = {'words': [0,0], 'acts': [0,0], 'gifts': [0,0], 'time': [0,0], 'touch': [0,0]}
    for day in range(weeks * 7):
        language = languages[day // (weeks * 7 // 5)]
        response = partner.response(language)
        
        if response == 'positive':
            responses[language][0] += 1
        else:
            responses[language][1] += 1
            
    res = [response[0] / sum(response) for response in responses.values()]
    return languages[res.index(max(res))]
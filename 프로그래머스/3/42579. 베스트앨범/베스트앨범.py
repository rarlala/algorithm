def solution(genres, plays):
    music_dict = {}
    
    idx = 0
    for (g, p) in zip(genres, plays):
        if g in music_dict:
            music_dict[g]['count'] += p
            music_dict[g]['list'].append({'idx' : idx, 'p' : p})
        else:
            music_dict[g] = {'count': p, 'list': [{'idx' : idx, 'p' : p}]}
        idx += 1
    
    sorted_data = dict(sorted(music_dict.items(), key=lambda x: x[1]['count'], reverse=True))
    
    result = []
    
    for i in sorted_data:
        i_list = sorted(music_dict[i]['list'], key=lambda x:x['p'], reverse=True)
        result.append(i_list[0]['idx'])
        if len(i_list) > 1:
            result.append(i_list[1]['idx'])
        
    return result

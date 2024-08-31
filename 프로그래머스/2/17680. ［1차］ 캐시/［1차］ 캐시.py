def solution(cacheSize, cities):
    cache_arr = []
    time = 0
    
    if cacheSize == 0:
        return len(cities) * 5
    
    for city in cities:
        city = city.lower()
        if city in cache_arr:
            time += 1
            cache_arr.remove(city)
            cache_arr.append(city)
            continue
        if len(cache_arr) == cacheSize:
            cache_arr.pop(0)
        cache_arr.append(city)
        time += 5
    
    return time
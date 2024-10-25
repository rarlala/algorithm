function solution(genres, plays) {
    const dict = {}

    genres.forEach((g, i) => {
        if (dict[g]) {
            dict[g].push({index : i, count: plays[i]})
        } else {
            dict[g] = [{index : i, count: plays[i]}]
        }
    })
    
    const sortedGenres = Object.entries(dict).sort((a, b) => {
        const totalA = a[1].reduce((acc, curr) => acc + curr.count, 0);
        const totalB = b[1].reduce((acc, curr) => acc + curr.count, 0);
        return totalB - totalA;
    })
    
    const result = []
    sortedGenres.forEach(([genres, songs]) => {
        songs.sort((a, b) => b.count - a.count)
        result.push(...songs.slice(0, 2).map(song => song.index))
    })
    
    return result
}
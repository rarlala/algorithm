function solution(participant, completion) { 
    const people = {}
    
    participant.forEach(p => {
        if (people[p]) {
            people[p] += 1
        } else {
            people[p] = 1
        }
    })
    
    completion.forEach(p => {
        if (people[p]) {
            people[p] -= 1
        }
    })
    
    return Object.entries(people).filter(([key, value]) => value === 1)[0][0]
}
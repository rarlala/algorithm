let NM = readLine()!.split(separator: " ").map{ Int($0)! }
let (N, M) = (NM[0], NM[1])
let times = readLine()!.split(separator: " ").map{ Int($0)! }.sorted()

var left = 0
var right = times[times.count - 1] * M

while left <= right {
    let mid = (left + right) / 2
    
    var balloon = 0
    for time in times {
        balloon += mid / time
    }
    
    if balloon >= M {
        right = mid - 1
    } else {
        left = mid + 1
    }
}

print(left)

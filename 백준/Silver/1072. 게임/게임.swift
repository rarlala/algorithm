let xy = readLine()!.split(separator: " ").map { Int($0)! }
let (x, y) = (xy[0], xy[1])

func getPercent(num1: Int, num2: Int) -> Int {
    return num1 * 100 / num2
}

let z = getPercent(num1: y, num2: x)

if z < 99 {
    var left = 0
    var right = 1_000_000_000

    while left <= right {
        let mid = (left + right) / 2

        let newZ = getPercent(num1: y + mid, num2: x + mid)
        if z >= newZ {
            left = mid + 1
        } else {
            right = mid - 1
        }
    }

    print(left)
} else {
    print(-1)
}
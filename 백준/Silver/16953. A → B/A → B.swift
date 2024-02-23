let nm = readLine()!.split(separator: " ").map{ Int($0)! }
let (n, m) = (nm[0], nm[1])

var stack = [(n, 1)]
var result = [Int]()

func loop(num: Int, count: Int) {
    if num == m {
        result.append(count)
        return
    } else if num > m {
        return
    }

    stack.append((num * 2, count + 1))
    stack.append((Int("\(num)1")!, count + 1))
}

while !stack.isEmpty {
    let data = stack.popLast()
    guard let data = data else { break }
    loop(num: data.0, count: data.1)
}

print(result.isEmpty ? -1 : result.min()!)

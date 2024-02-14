let num = Int(readLine()!)!

var datas = [Int]()

var currentNum = 1
var result = ""

for _ in 0..<num {
    let num = Int(readLine()!)!

    while currentNum <= num {
        result += "+\n"
        datas.append(currentNum)
        currentNum += 1
    }

    if !datas.isEmpty && datas.last! == num {
        let _ = datas.popLast()
        result += "-\n"
    }
}

result.popLast()
print(datas.count > 0 ? "NO" : result)
function solution(phone_book) {
    phone_book.sort()
    
    let result = true
    phone_book.forEach((p, i) => {
        if (i === phone_book.length - 1) { return }
        if (phone_book[i+1].startsWith(p)) {
            result = false
        }
    })
    
    return result
}
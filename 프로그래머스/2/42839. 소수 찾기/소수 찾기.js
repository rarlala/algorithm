function solution(numbers) {
    const digits = numbers.split("")
    const combinations = new Set()
    
    function getPermutations(arr, prefix = '') {
        if (prefix.length > 0) {
            combinations.add(Number(prefix))
        }
        
        for (let i = 0; i < arr.length; i++) {
            getPermutations(arr.slice(0, i).concat(arr.slice(i + 1)), prefix + arr[i])
        }
    }
    
    getPermutations(digits)
    
    function isPrime(n) {
        if (n < 2) return false
        for (let i = 2; i <= Math.sqrt(n); i++) {
            if (n % i === 0) return false;
        }
        return true
    }
    
    let primeCount = 0;
    combinations.forEach((num) => {
        if (isPrime(num)) {
            primeCount++
        }
    })
    
    return primeCount
    
}
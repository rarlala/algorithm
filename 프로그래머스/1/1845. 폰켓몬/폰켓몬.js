function solution(nums) {
    const kind = new Set(nums)
    const maxCount = parseInt(nums.length / 2)
    return maxCount < kind.size ? maxCount : kind.size
}
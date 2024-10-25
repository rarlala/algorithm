function solution(phone_book) {
  let result = true;
  return !phone_book.sort().some((p, i) => {
    if (i === phone_book.length - 1) return false;
    return phone_book[i + 1].startsWith(p);
  });
}

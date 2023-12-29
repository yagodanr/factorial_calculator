
def factorial():
    memorized = {0: 1,
                 1: 1,
                 2: 2,
                 3: 6,
                 4: 24,
                 5: 120}
    max_known = 5

    def inner(n: int) -> int:
        nonlocal memorized
        ans = memorized.get(n)
        if ans is not None:
            return ans
        ans = memorized[max_known]
        for i in range(max_known+1, n+1):
            ans *= i
            memorized[n] = ans
        return ans

    return inner
factorial = factorial()



user_input = int(input("Введіть число для визначення факторіалу:\n"))

print(factorial(user_input))

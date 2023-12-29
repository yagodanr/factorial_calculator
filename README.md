# factorial_calculator
___
LogikaSchool test project for git


* [X] [Notion git](https://copper-chef-4bb.notion.site/Git-a70a20390ec349c6b3a200cf59e94690?pvs=4)
* [X] [Notion venv](https://copper-chef-4bb.notion.site/Venv-e7e489e3cf33424789f7f87a3381c83a?pvs=4)


Experiments `with` readme.md:

:vhs:
:white_check_mark: 

```python
def factorial():
    memorized = {0: 1,
                 1: 1,
                 2: 2,
                 3: 6,
                 4: 24,
                 5: 120}
    max_known = 5

    def inner(n: int) -> int:
        if n < 0:
            raise ValueError("Number has to be positive(>0)")

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
```

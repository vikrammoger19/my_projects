def both(N):
    yield from range(N)
    yield from (x ** 2 for x in range(N))


class Wrapper:
    def __init__(self, foo) -> None:
        self.my_foo = foo

    def __next__(self):
        try:
            _value = next(self.my_foo)
            return _value
        except StopIteration:
            return 'All numbers have been processed.'


new_result = Wrapper(both(4))
for i in range(10):
    print(next(new_result))

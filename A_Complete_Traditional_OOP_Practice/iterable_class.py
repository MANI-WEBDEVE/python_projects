class CountRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        else:
            print(f"1◘ Current value: {self.current}")
            current = self.current
            print(f"2 Current value: {current}")
            self.current += 1
            print(f"next Current value: {self.current}")
            return current

counter = CountRange(1,5)
for i in counter:
    print(i)
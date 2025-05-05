class Counter:
    counte=0

    def __init__(self):
        Counter.counte += 1

    @classmethod
    def show_countes(cls):
        print(cls.counte)

c1=Counter()
c2=Counter()

c2.show_countes()
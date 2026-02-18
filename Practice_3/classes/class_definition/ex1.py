class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

# Usage
my_tally = Counter()
my_tally.increment()
my_tally.increment()
print(my_tally.value)
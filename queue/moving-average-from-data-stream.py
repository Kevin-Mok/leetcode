from collections import deque

class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.sum = 0
        self.nums = deque()
        
    def next(self, val: int) -> float:
        if len(self.nums) >= self.size:
            self.sum -= self.nums.popleft()
        self.sum += val
        self.nums.append(val)
        return self.sum / len(self.nums)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)


if __name__ == "__main__":
    size = 3
    values = [1, 10, 3, 5]
    expected = [1.0, 5.5, 14 / 3, 6.0]

    print("Window size:", size)
    print("Input values:", values)
    print("Expected outputs:", expected)

    try:
        moving_average = MovingAverage(size)
        actual = [moving_average.next(value) for value in values]
        print("Actual outputs:", actual)
        print("Matches expected:", actual == expected)
        if actual != expected:
            print(f"Diff: actual {actual} != expected {expected}")
    except NotImplementedError as exc:
        print("Actual outputs: not implemented")
        print("Matches expected: False")
        print("Note:", exc)

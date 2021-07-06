class Value_Calculator:
    def __init__(self,val: str):
        self.val = val
    def __add__(self, other):
        return self.val + other.val


if __name__ == "__main__":
    print('hi')


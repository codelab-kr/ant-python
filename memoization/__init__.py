import sys

class AntSequence:
    def __init__(self):
        self.memo = ['1']

    def get_ln(self, n):
        while len(self.memo) < n:
            prev_ln = self.memo[-1]
            result = ''
            i = 0
            while i < len(prev_ln):
                count = 1
                while i + 1 < len(prev_ln) and prev_ln[i] == prev_ln[i+1]:
                    i += 1
                    count += 1
                result += str(count) + prev_ln[i]
                i += 1
            self.memo.append(result)
        return self.memo[n-1]

    def get_m(self, n):
        ln = self.get_ln(n)
        length = len(ln)
        i = length // 2 - 1
        return ln[i:i+2]

if __name__ == "__main__":
    ant = AntSequence()
    n = int(sys.argv[1])
    print(ant.get_m(n))
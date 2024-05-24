import sys

# 부르트 포스
class AntSequence:
    # 초기화
    def __init__(self):
        self.n = 1
        self.ln = '1'

    # ln을 구하는 함수
    def get_ln(self):
        result = ''
        prev_ln = self.ln
        i = 0
        while i < len(prev_ln):
            count = 1
            while i + 1 < len(prev_ln) and prev_ln[i] == prev_ln[i+1]:
                i += 1
                count += 1
            result += str(count) + prev_ln[i]
            i += 1
        self.ln = result
        self.n += 1
        # print(self.n, result)
        return result

    #  위 함수를 반복
    def repeat(self, n):
        while self.n < n:
            self.get_ln()
        return self.ln

    # m을 구하는 함수
    def get_m(self, n):
        ln = self.repeat(n)
        length = len(ln)
        i = length // 2 - 1
        return ln[i:i+2]

if __name__ == "__main__":
    ant = AntSequence()
    n = int(sys.argv[1])
    print(ant.get_m(n))

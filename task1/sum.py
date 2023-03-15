def solution(n: int) -> int:
    return n * (n+1) // 2


if __name__ == "__main__":
    n = int(input())
    print(f"Sum of numbers from 1 to {n} is {solution(n)}")



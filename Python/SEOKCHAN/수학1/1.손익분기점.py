#!/usr/bin/env python3

def main():
    a, b, c = map(int, input().split())
    if c <= b:
        print(-1)
        return

    result = int(a / (c - b))
    print(result + 1)


if __name__ == '__main__':
    main()


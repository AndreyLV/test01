from itertools import groupby
import sys


def main() -> None:
    words = sys.stdin.read().split()
    if not words:
        return

    words.sort(key=lambda word: (len(word), word))

    for length, group in groupby(words, key=len):
        words_of_length = list(group)
        print(f"{length} -> {', '.join(words_of_length)}")


if __name__ == "__main__":
    main()

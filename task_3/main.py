from timeit import timeit
from pathlib import Path
from boyer_moore_search import boyer_moore_search
from kmp_search import kmp_search
from rabin_karp_search import rabin_karp_search


def read_file(file_path_str):
    file_path = Path(file_path_str)
    text = file_path.read_text(encoding="utf-8")
    return text


def benchmark(algorithm, main_string, substring):
    return timeit(lambda: algorithm(main_string, substring), number=10)


def main():
    content = [
        ("article_1.txt", "основне завдання програміста", "nonexistent text"),
        (
            "article_2.txt",
            "Перевага розгорнутого списку над іншими",
            "nonexistent text",
        ),
    ]

    algorithms = [
        ("Boyer-Moore", boyer_moore_search),
        ("Knuth-Morris-Pratt", kmp_search),
        ("Rabin-Karp", rabin_karp_search),
    ]

    for file, substring, nonexistent_substring in content:
        print(f"\n=== File: {file} ===")

        main_string = read_file(file)

        print(f"\n--- Substring exists ---")
        for name, func in algorithms:
            elapsed = benchmark(func, main_string, substring)
            print(f"{name:20s} -> {elapsed:.6f} seconds")

        print(f"\n--- Substring does not exist ---")
        for name, func in algorithms:
            elapsed = benchmark(func, main_string, nonexistent_substring)
            print(f"{name:20s} -> {elapsed:.6f} seconds")


if __name__ == "__main__":
    main()

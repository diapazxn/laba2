import re
from collections import Counter

def count_pairs_in_line(line: str) -> Counter:
    """
    Повертає лічильник пар букв у рядку.
    Пари рахуємо тільки всередині слів (не через пробіл).
    """
    line = line.lower()
    words = re.findall(r"[a-zа-яіїєґ]+", line)

    counter = Counter()

    for word in words:
        if len(word) < 2:
            continue
        for i in range(len(word) - 1):
            pair = word[i:i + 2]
            counter[pair] += 1

    return counter

def pairs_generator(filename: str, top_n: int = 3):
    """
    Генератор:
    - читає файл пострічково
    - для кожного рядка повертає топ-3 найчастіші пари букв
    """
    with open(filename, "r", encoding="utf-8") as f:
        for line_number, line in enumerate(f, start=1):
            pairs_counter = count_pairs_in_line(line)

            if not pairs_counter:
                yield line_number, []
                continue

            top_pairs = pairs_counter.most_common(top_n)
            yield line_number, top_pairs

if __name__ == "__main__":
    filename = "text100.txt"

    for line_no, pairs in pairs_generator(filename):
        print(f"Рядок {line_no}:")
        if not pairs:
            print("  (немає пар букв)")
        else:
            for pair, count in pairs:
                print(f"  '{pair}' → {count}")

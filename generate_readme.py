import os
import re

# -------------------------
# Topic classification rules
# -------------------------
TOPICS = {
    "Array": [
        "Two-Sum", "Remove-Element", "Buy", "Stock", "Duplicate",
        "Subarray", "Running-Sum", "Maximum-Ones", "Sorting",
        "Missing", "Repeating"
    ],
    "Binary Search": [
        "Median", "Rotated", "Search", "Position", "Minimum",
        "Peak", "Single-Element", "Kth-Missing", "Ship", "Divisor",
        "Bouquets"
    ],
    "String": [
        "String", "Roman", "Prefix", "Find-the-Index",
        "Reverse-Words", "Isomorphic", "Anagram", "Compression",
        "Frequency", "Rotate", "Parenthesis", "Depth",
        "Odd-Number", "Beauty"
    ],
    "Linked List": [
        "Linked-List", "Remove-Duplicates", "Reverse", "Delete-Node",
        "Middle"
    ],
    "Sliding Window": [
        "Repeating-Character", "Subarray", "Binary-Subarrays",
        "K-Different", "Nice-Subarrays", "Substrings"
    ],
    "Math": [
        "Plus-One", "Sqrt", "Power-of-Two", "Fibonacci",
        "Tribonacci"
    ],
    "Matrix": [
        "2D-Matrix", "Peak-Element-II", "Maximum-Ones"
    ],
    "Dynamic Programming": [
        "Palindromic-Substring", "Fibonacci", "Tribonacci",
        "Product-Subarray"
    ],
    "Miscellaneous": [
        "Basic", "Program"
    ]
}

# Header template
README_HEADER = """# 🧠 DSA

[LeetCode Profile](https://leetcode.com/u/mdsamiahmad/)

## 📘 LeetCode Topics

---
"""

def classify_problem(folder_name):
    fname = folder_name.lower()
    for topic, keywords in TOPICS.items():
        for key in keywords:
            if key.lower() in fname:
                return topic
    return "Miscellaneous"


def generate_readme():
    print("[+] Scanning folders...")

    all_folders = [
        f for f in os.listdir(".")
        if os.path.isdir(f) and re.match(r"^\d{4}-", f)
    ]

    categorized = {}

    for folder in all_folders:
        topic = classify_problem(folder)

        if topic not in categorized:
            categorized[topic] = []
        categorized[topic].append(folder)

    # Sort categories and problems numerically
    for topic in categorized:
        categorized[topic].sort(key=lambda x: int(x.split("-")[0]))

    # Build README
    print("[+] Generating README.md...")

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(README_HEADER)

        for topic in sorted(categorized.keys()):
            f.write(f"\n### {topic}\n\n")
            f.write("| Problems |\n|---|\n")

            for folder in categorized[topic]:
                url = f"https://github.com/mdsamiahmad/DSA/tree/main/{folder}"
                f.write(f"| [{folder}]({url}) |\n")

            f.write("\n---\n")

    print("[✓] README.md updated successfully!")


if __name__ == "__main__":
    generate_readme()

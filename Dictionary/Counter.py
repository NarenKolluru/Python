from collections import Counter

def top_three_frequent(elements):
    freq= Counter(elements)
    top_three = freq.most_common(3)
    return dict(top_three)


elements = [1, 2, 2, 3, 4, 4, 4, 5, 5, 5]
print("Top three most frequent elements:", top_three_frequent(elements))

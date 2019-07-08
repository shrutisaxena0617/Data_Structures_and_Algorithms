def sol(words, word1, word2):
    if words and word1 and word2:
        p1, p2 = -1, -1
        min_diff = float('INF')
        for i in range(len(words)):
            if words[i] == word1:
                p1 = i
            if words[i] == word2:
                p2 = i
            if p1 != -1 and p2 != -1:
                min_diff = min(min_diff, abs(p1 - p2))
        return min_diff

print(sol(["practice", "makes", "perfect", "coding", "makes"], "coding", "practice"))

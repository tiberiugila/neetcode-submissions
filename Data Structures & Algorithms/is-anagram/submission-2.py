class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_s = Counter(s)
        seen_t = Counter(t)
        return seen_s == seen_t
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        _map = {}
        _mapped = {}
        for i in range(len(s)):
            if _map.get(s[i]) is None and t[i] not in _mapped:
                _map[s[i]] = t[i]
                _mapped[t[i]] = True
            if _map.get(s[i]) != t[i]:
                return False
        return True

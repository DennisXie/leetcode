class Solution:

    def removeDuplicateLetters(self, s: str) -> str:
        dic = {}
        ch_set = []
        for i in range(len(s)):
            if dic.get(s[i]) is None:
                dic[s[i]] = [i]
                ch_set.append(s[i])
            else:
                dic[s[i]].append(i)
        ch_set.sort()
        ans = ""
        while len(dic) > 0:
            for ch in ch_set:
                if dic.get(ch) is None:
                    continue

                dest = dic[ch][0]
                valid = True
                for key, key_indexes in dic.items():
                    if key_indexes[-1] < dest:
                        valid = False
                        break

                if valid:
                    ans = ans + ch
                    for key in dic.keys():
                        key_indexes = dic[key]
                        max_idx = 0
                        for i in range(len(key_indexes)):
                            if key_indexes[i] > dest:
                                max_idx = i
                                break
                        dic[key] = key_indexes[max_idx:]
                    del dic[ch]
                    break
        return ans


if __name__ == "__main__":
    print(Solution().removeDuplicateLetters("cbacdcbc"))

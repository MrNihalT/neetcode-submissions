class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = {}
        for w in strs:
            key= "".join(sorted(w))

            if key not in a:
                a[key] = []
            a[key].append(w)

        return list(a.values())
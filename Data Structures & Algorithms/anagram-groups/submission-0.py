class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {}

        for strings in strs:
            letters = [0] * 26
            for char in strings:
                letters[ord(char) - ord('a')]+=1
            
            key = tuple(letters)
            if key not in groups:
                groups[key] = []
            groups[key].append(strings)
        
        return list(groups.values())


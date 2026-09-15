class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups_by_signature = defaultdict(list)
        for s in strings:
            signature = self.shift_signature(s)
            groups_by_signature[signature].append(s)

        return list(groups_by_signature.values())
        
    def shift_signature(self, s: str) -> str:

        shifts = []
        for prev_char, next_char in zip(s, s[1:]):
            shift = (ord(next_char) - ord(prev_char)) % 26
            shifts.append(chr(shift + ord('a')))
        return ''.join(shifts)
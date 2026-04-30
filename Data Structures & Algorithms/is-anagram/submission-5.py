class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        freq_a = {}
        for letter in s:
            if letter in freq_a:
                freq_a[letter] += 1
            else:
                freq_a[letter] = 1
        freq_b = {}
        for letter in t:
            if letter in freq_b:
                freq_b[letter] += 1
            else:
                freq_b[letter] = 1       
        
        if (freq_a == freq_b):
            return True
        else:
            return False

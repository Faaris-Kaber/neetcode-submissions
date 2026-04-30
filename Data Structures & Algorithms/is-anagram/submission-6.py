class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        freq_a = {}
        
        for char in s:
            freq_a[char] = freq_a.get(char, 0) + 1 
            # this will assign the value of this key a number determined in next step#this means get the num of repeats of this char and add one, if there is none then it will return 0 + 1, remember this will only return values

        freq_b = {}

        for char in t:
            freq_b[char] = freq_b.get(char, 0) + 1
        
        if (freq_a == freq_b):
            return True
        else:
            return False
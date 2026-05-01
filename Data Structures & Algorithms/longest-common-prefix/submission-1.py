class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        counter = 0
        #loops through  length of each word, i.e. if the first word is bat then this will be three
        for i in range (len(strs[0])):
            
            #this will loop through the num of words in this array
            for j in range(len(strs) - 1):
                
                #compare the same index char from each array
                if (i >= len ( strs[j+1])) or (strs[j][i] != strs[j+1][i]):
        
                    return (strs[0][:counter])
        
            counter += 1
        
        
        return strs[0][:counter]
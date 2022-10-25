class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        if (len(word1) == 1 and len(word2) == 1):
            return word1[0] == word2[0]
        
        else:
            word1_complete = ""
            word2_complete = ""
            for i in word1:
                word1_complete += i
            
            for j in word2:
                word2_complete += j
            
            return word1_complete == word2_complete
            
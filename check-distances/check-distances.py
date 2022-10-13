class Solution(object):
    def checkDistances(self, s, distance):
        """
        :type s: str
        :type distance: int
        :rtype: bool
        """
        letterDict = {"a":0, "b":1, "c":2, "d":3, "e":4,
                "f":5, "g":6, "h":7, "i":8, "j":9,
                "k":10, "l":11, "m":12, "n":13, "o":14,
                "p":15, "q":16, "r":17, "s":18, "t":19,
                "u":20, "v":21, "w":22, "x":23, "y":24,
                "z":25}
        
        notSeenChar = []
        for i in range(len(s)):
            if s[i] not in notSeenChar:
                notSeenChar.append(s[i])

        counter = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                varAux = letterDict[s[i]]

                if s[i] == s[j] and abs(i - abs(j-1)) == distance[varAux] and s[i] in notSeenChar:
                    counter += 1

        if counter < len(notSeenChar):
            return False
        return True

if __name__ == "__main__":
    s = Solution()
    #print(s.checkDistances("abbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzza", [49,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))
    print(s.checkDistances("abcabc", [0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))

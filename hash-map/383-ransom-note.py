class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomNoteChars = {}
        for letter in ransomNote:
            ransomNoteChar = self.addToDict(letter, ransomNoteChars)
        #  print(ransomNoteChars)
        magazineChars = {}
        for letter in magazine:
            magazineChars = self.addToDict(letter, magazineChars)
        #  print(magazineChars)
        for letter in ransomNoteChars.keys():
            #  if magazineChars == {}:
                #  return False
            if ((letter not in magazineChars) or
                (magazineChars[letter] < ransomNoteChars[letter])):
                return False
        return True

    def addToDict(self, letter, dict_add):
        #  print(letter, dict_add)
        if letter in dict_add:
            dict_add[letter] += 1
        else: 
            dict_add[letter] = 1
        return dict_add
        
        
if __name__ == "__main__":
    sol = Solution()
    #  base
    r = "a"
    m = "b"
    #  r = "aa"
    #  m = "aab"

    #  wrong
    #  nums1 = [-1,0,0,0,3,0,0,0,0,0,0]
    #  m = 5
    #  nums2 = [-1,-1,0,0,1,2]
    #  n = 6

    print(sol.canConstruct(r, m))

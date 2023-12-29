# 49. Group Anagrams

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_map = defaultdict(list)
        print(anagram_map)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
            print(anagram_map)
        
        return list(anagram_map.values())
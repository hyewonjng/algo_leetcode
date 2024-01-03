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
            # n* clogc (where c is the max length of characters in given words)
            sorted_word = ''.join(sorted(word))
            # map_name['key_name'].append('value_name')
            # defaultdict 사용법: https://dongdongfather.tistory.com/69
            anagram_map[sorted_word].append(word)
            print(anagram_map)
        
        return list(anagram_map.values())
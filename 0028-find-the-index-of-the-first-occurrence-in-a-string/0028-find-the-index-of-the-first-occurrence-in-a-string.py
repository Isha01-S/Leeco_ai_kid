class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        haystack_length = len(haystack)
        needle_length = len(needle)
        if needle == "":
            return -1
        index = 0
        j= 0
        k=0
        while index < haystack_length and j <haystack_length:
            if needle[k]!=haystack[j]:
                index+=1
                j=index
                k=0
            else:
                if k==needle_length-1:
                    return index
                
                j+=1
                k+=1
        return -1

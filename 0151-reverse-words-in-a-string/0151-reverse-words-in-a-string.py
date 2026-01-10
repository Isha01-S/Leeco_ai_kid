class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=s.strip()
        array = []
        st=""
        result=""
        for ch in s:
            if ch == " ":
                if st=="":
                    continue
                array.append(st)
                st = ""
            else:
                st+=ch
        array.append(st)
        for i in range(len(array)-1,-1,-1):
            result+=array[i]
            if i==0:
                break
            result+=" "
        return result

            
        
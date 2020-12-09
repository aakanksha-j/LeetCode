class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        Runtime: 28 ms
        Memory: 12.8 MB
        """
        if len(a)==0:  return b
        if len(b)==0:  return a
        if a[-1]=='0' and b[-1]=='0':
            print '00'
            return self.addBinary(a[0:-1],b[0:-1])+'0'
        elif a[-1]=='1' and b[-1]=='1':
            print '11'
            return self.addBinary(self.addBinary(a[0:-1],b[0:-1]),'1')+'0'
        else:
            print '10or01'
            return self.addBinary(a[0:-1],b[0:-1])+'1'

s= Solution()
print s.addBinary('1','1')

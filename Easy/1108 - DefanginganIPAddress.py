#link to the problem - https://leetcode.com/problems/defanging-an-ip-address/

#Given a valid (IPv4) IP address, return a defanged version of that IP address.
#A defanged IP address replaces every period "." with "[.]".

#link to submission - https://leetcode.com/submissions/detail/685500901/

class Solution(object):
    def defangIPaddr(self, address):
        address=address.replace('.','[.]')
        return address

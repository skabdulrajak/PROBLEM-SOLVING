class Solution(object):
    def convertTemperature(self, celsius):
        fah=celsius*1.80+32.00
        kelvin=celsius+273.15
        ans=[kelvin,fah]
        return ans
        """
        :type celsius: float
        :rtype: List[float]
        """
        
class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ''
        if num >= 1000:
            mul = num // 1000
            ans += mul * 'M'
            num -= 1000 * mul

        if num >= 900:
            ans += 'CM'
            num -= 900

        if num >= 500:
            ans += 'D'
            num -= 500

        if num >= 400:
            ans += 'CD'
            num -= 400

        if num >= 100:
            mul = num // 100
            ans += mul * 'C'
            num -= 100 * mul

        if num >= 90:
            ans += 'XC'
            num -= 90

        if num >= 50:
            ans += 'L'
            num -= 50

        if num >= 40:
            ans += 'XL'
            num -= 40

        if num >= 10:
            mul = num // 10
            ans += mul * 'X'
            num -= 10 * mul

        if num >= 9:
            ans += 'IX'
            num -= 9

        if num >= 5:
            ans += 'V'
            num -= 5

        if num >= 4:
            ans += 'IV'
            num -= 4

        if num >= 1:
            ans += num * 'I'
            num -= num

        return ans
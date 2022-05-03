class Solution:

    def intToRoman(self, num: int) -> str:
        dic2 = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }

        romans = []
        for k, v in dic2.items():
            romans.append((k, v))
        romans.sort(key=lambda x: x[1], reverse=True)

        rom = ''
        for roman in romans:
            while num >= roman[1]:
                t = num // roman[1]
                rom = rom + roman[0] * t
                num = num % roman[1]
        return rom


if __name__ == "__main__":
    print(Solution().intToRoman(1994))

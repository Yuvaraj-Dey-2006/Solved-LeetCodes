class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # list -> str -> int -> str -> list
        # str_digit = "".join(map(str, digits))   list -> str
        # int_digit = int(str_digit) + 1          str -> int
        # str_digit = str(int_digit)              int -> str
        # return in list as int dtype             str -> list

        return list(int(n) for n in (str(int("".join(map(str, digits))) + 1)))

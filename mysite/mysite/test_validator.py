import re

val = "01012341234"
pattern = r"^01[016789][1-9]\d{6,7}$"
#pattern = "^01[016789][1-9]\\d{6,7}$" 위의 코드와 상동
"""
if len(val) == 11 andval[:3] in ("010", "011", "016", "017", "018", "019"):
    print("OK")

정규 표현식을 쓰면
"""
if re.match(pattern,val):
    print("OK")
else:
    print("Valid")

#이렇게 간단히 된다
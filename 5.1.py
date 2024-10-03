import keyword
import string


test_data = ["_", "__", "___", "x", "get_value", "get value", "get!value", "some_super_puper_value", "Get_value", "get_Value", "getValue", "3m", "m3", "assert", "assert_exception"  ]

for test_variable in test_data:
    if test_variable[0].isdigit() and "_" not in test_variable:
        print("False")
        continue
    elif not test_variable.islower() and "_" not in test_variable:
        print("False")
        continue
    if any(char in string.whitespace or char in string.punctuation for char in test_variable if char != "_"):
        print("False")
        continue
    elif test_variable in keyword.kwlist:
        print("False")
        continue
    elif test_variable.count("_") > 1:
        print("False")
        continue
    elif test_variable[0].isdigit():
        print("False")
        continue
    else:
        print("True")
        continue

# _ => True
# __ => False
# ___ => False
# x => True
# get_value => True
# get value => False
# get!value => False
# some_super_puper_value => True
# Get_value => False
# get_Value => False
# getValue => False
# 3m => False
# m3 => True
# assert => False
# assert_exception => True



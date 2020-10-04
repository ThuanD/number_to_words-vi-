from num2words import num2words

def write_small_number(number):
    """ number < 10^9 """
    result = ""
    if number < 1000 or number % 100 == 0:
        result = num2words(number, lang = "vi")
    else:
        result = num2words(number // 100 * 100, lang = "vi")
        if ((number // 100) % 10 == 0):
            result += " không trăm"
        if ((number % 100 > 10)):
            result += " " + num2words(number % 100, lang = "vi")
        else:
            result += " lẻ " + num2words(number % 100, lang = "vi")
    return result
def write_number(number):
    """ number > 10^9 """
    result = ""
    unit = " tỷ"
    leng_number = len(str(number))
    # chia thành 9 chữ số 1 cụm, tính từ phải sang trái
    index = leng_number // 9
    if leng_number % 9 == 0:
        index = index -1
    while (index >= 0):
        # những chứ số đầu tiên
        begin_number = number // (10**(index*9))
        if begin_number % 10**9 != 0:
            if index == 0 and begin_number < 10:
                # 9 chữ số cuối cùng là 00000000X
                result += "lẻ "
            if index == 0:
                result += write_small_number(begin_number) + index * unit
            elif index != 0:
                result += write_small_number(begin_number) + index * unit + ", "
        number = number - begin_number * (10**(index*9))
        index -= 1
    return result

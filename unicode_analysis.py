#Input any character and determine to which Unicode encoding range it belongs.
def unicode_name_of_char(character_list):
   
    uni_path = "unicode.txt"
    with open(uni_path,'r',encoding='utf-8')as f: 
        lines = f.read().splitlines()
    code_list = []
    code_dict = {}
    for line in lines:
        code_range, name = line[:9], line[10:]
        code_list.append(code_range)
        code_dict[code_range] = name     

    hex_ranges = []
    for r in code_list:
        start, end = r.split('-')
        hex_start = int(start, 16)
        hex_end = int(end, 16)
        hex_ranges.append((hex_start, hex_end))

    for char in character_list:
        hex_char = ord(char)

        # Determine if the hexadecimal encoding of a character is within the specified range.
        for idx, (start, end) in enumerate(hex_ranges):
            if start <= hex_char <= end:
                print(f"Char: '{char}' hex code: {str(hex(hex_char))} in the range {code_dict[code_list[idx]]}")
                break


def divide_char_in_need(character_list):
    uni_path = "unicode_need.txt"
    with open(uni_path,'r',encoding='utf-8')as f: 
        lines = f.read().splitlines()
    code_list = []
    code_dict = {}
    for line in lines:
        code_range, name = line[:9], line[10:]
        code_list.append(code_range)
        code_dict[code_range] = name     
 
    hex_ranges = []
    for r in code_list:
        start, end = r.split('-')
        hex_start = int(start, 16)
        hex_end = int(end, 16)
        hex_ranges.append((hex_start, hex_end))

    in_need = []
    no_need = []
    for char in character_list:
        hex_char = ord(char)
      
        for idx, (start, end) in enumerate(hex_ranges):
            if start <= hex_char <= end:
                in_need.append(char)
                # print(f"The char'{char}' hex code {str(hex(hex_char))} in the range {code_dict[code_list[idx]]}")
                break
        else:
            no_need.append(char)
    print("the char you need:",in_need)
    print("the char you don't need:",no_need)

if __name__ == "__main__":
    char_list = ['\x01', '\x02', '\x07', '\x0e', '\x0f', '\x15', '\x18', '\x1e', '\x1f', '\x7f', '\x80', \
                 '\x81', '\x82', '\x83', '\x84', '\x86', '\x87', '\x88', '\x89', '\x8a', '\x8b', '\x8c', \
                '\x8d', '\x8e', '\x8f', '\x90', '\x91', '\x92', '\x93', '\x94', '\x95', '\x96', '\x97', \
                '\x98', '\x99', '\x9a', '\x9b', '\x9c', '\x9d', '\x9e', '\x9f','\u200b', '\u200c', \
                '\u200d', '\u200e', '\u200f','\u2060', '\u2061','\u202a', '\u202b', '\u202c']
    '''func#1
    Check the range to which each character belongs
    https://www.qqxiuzi.cn/zh/unicode-zifu.php?plane=0&ks=1000&js=1FFF
    '''
    unicode_name_of_char(char_list)
    
    '''func#2
    After modifying unicode_need.txt, select the characters that are needed or not needed.'''
    divide_char_in_need(char_list)
      
  
import json
import pdb
import re
import os
import torch
from tqdm import tqdm
import copy

def one_example():
    # char = '☕' #U+00002615
    # char = '😌' #U+0001F60C
    # char = '💯' #U+0001F60C
    # char = '🔺' #U+0001F53A
    # char = '👴' #U+0001F474
    char = '☸'
    # json_path = r"tokenizer.json"
    # with open(json_path, 'r', encoding='utf-8') as f:
    #     json_data = json.load(f)
    # vocab = json_data['model']['vocab']
    # chars = [key for key, value in vocab.items() if value == 37426]

    
    unicode_code_point = ord(char)
    hex_code_point = f"U+{unicode_code_point:08X}"
    
    print(hex_code_point)
    pdb.set_trace()


def is_in_ranges(c, ranges):
    code_point = ord(c)
    for start, end in ranges:
        if start <= code_point <= end:
            return True
    return False

def is_string_in_ranges(s, ranges):
    return all(is_in_ranges(c, ranges) for c in s)

def find_unicode():

    with open(r"unicode_cleaned_need.txt", 'r',encoding='utf-8', errors='ignore') as f: #input
        lines = f.read().splitlines()
    need_ranges = []
    for line in lines:
        code_range, name = line[:9], line[10:]
        parts = code_range.split('-')
        start = int(parts[0], 16) 
        end = int(parts[1], 16)   
        need_ranges.append((start, end))

    # with open("unicode_cleaned_noneed.txt", 'r',encoding='utf-8', errors='ignore') as f: #input
    #     lines = f.read().splitlines()
    # noneed_ranges = []
    # for line in lines:
    #     code_range, name = line[:9], line[10:]
    #     parts = code_range.split('-')
    #     start = int(parts[0], 16) 
    #     end = int(parts[1], 16)   
    #     noneed_ranges.append((start, end))

    emoji_pattern = re.compile(r'[\U00010000-\U0001FFFF]')
    json_path = r"tokenizer.json"
    with open(json_path, 'r', encoding='utf-8') as f:
        json_data = json.load(f)

    new_json_data = copy.deepcopy(json_data)
    need_dict = {}
    noneed_dict = {}
    vocab = json_data['model']['vocab']
    for word, word_token_id in tqdm(vocab.items()):
        if emoji_pattern.search(word):
            noneed_dict[word] = word_token_id 
            del new_json_data['model']['vocab'][word]
            continue
            
        if is_string_in_ranges(word, need_ranges):
            need_dict[word] = word_token_id
        else:
            noneed_dict[word] = word_token_id
            del new_json_data['model']['vocab'][word]

    with open(r'need.json', 'w', encoding='utf8') as f:
        json.dump(need_dict, f, indent= 4, ensure_ascii=False)
    with open(r'noneed.json', 'w', encoding='utf8') as f:
        json.dump(noneed_dict, f, indent= 4, ensure_ascii=False)

    new_id = 0
    for word, word_token_id in tqdm(new_json_data['model']['vocab'].items()):
        new_json_data['model']['vocab'][word] = new_id
        new_id += 1


    # with open(r'tokenizer.json', 'w', encoding='utf8') as f:
    #     json.dump(new_json_data, f, indent= 4, ensure_ascii=False)
        
if __name__ == "__main__":
    pass

    # one_example()
    # find_unicode()
import re

# 1
def match_a_zero_plus_b(text):
    pattern = r'ab*'
    return re.fullmatch(pattern, text) is not None

# 2
def match_a_two_three_b(text):
    pattern = r'ab{2,3}'
    return re.fullmatch(pattern, text) is not None

# 3
def match_a_anything_b(text):
    pattern = r'a.*b$'
    return re.fullmatch(pattern, text) is not None

# 4
def find_snake_sequences(text):
    return re.findall(r'[a-z]+_[a-z]+', text)

# 5
def find_title_sequences(text):
    return re.findall(r'[A-Z][a-z]+', text)

# 6
def replace_with_colon(text):
    return re.sub(r'[ ,.]', ':', text)

# 7
def snake_to_camel(text):
    return ''.join(word.capitalize() for word in text.split('_'))

# 8
def camel_to_snake(text):
    str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower()

# 9
def split_at_uppercase(text):
    return re.findall(r'[A-Z][^A-Z]*', text)

# 10
def insert_spaces(text):
    return re.sub(r'(\w)([A-Z])', r'\1 \2', text)
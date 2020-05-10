import os
import random
import datetime
import config

phrase_list = []
opener_list = []
keyword_list = []
finisher_list = []

REPORT_NO = None
DATE_RANGE = None

def load_items(folder, filename):
    items = []

    items_file = os.path.join(folder, filename)
    if os.path.exists(items_file):
        with open(items) as f:
            for word in f.read().rstrip().split(','):
                items.append(word)
    else:
        print("ERROR: Can't find {} to read from!".format(items_file))

    return items

def load_keywords(project_folder, keywords_file)
    return load_items(project_folder, keywords_file)

def load_openers(path=None):
    if path is None:
        path = config.CONFIG_FOLDER

    return load_items(path, config.OPENERS)

def load_phrases(path=None):
    if path is None:
        path = config.CONFIG_FOLDER

    return load_items(path, config.PHRASES)

def get_report_count(project_folder):
    count = 0

    for root, dirs, files in os.walk(project_folder):
        for f in files:
            if f.endswith('.report'):
                count += 1

    return count

def get_date_range():
    today = datetime.today()
    first_day = today + datetime.timedelta(days=-5)
    today = today.strftime('%d.%m.%G')
    first_day = first_day.strftime('%d.%m.%G')

    return first_day + ' - ' + today

def load_constants(project_folder, report_no=None, date_range=None):
    global REPORT_NO
    global DATE_RANGE

    if report_no is None:
        report_no = get_report_count(project_folder) + 1

    if date_range is None:
        date_range = get_date_range()

    REPORT_NO = report_no
    DATE_RANGE = date_range

def load_header(header_file=""):
    if header_file == "":
        header_file = config.HEADER_FILE

    with open(header_file) as f:
        header = f.read().rstrip().split(' ')

    return header

def check_word(word):
    if word == "KEYWORD":
        return random.choice(keywords_list)
    elif "REPORT_NO" in word:
        return str(REPORT_NO).join(word.split("REPORT_NO"))
    elif "DATE_RANGE" in word:
        return str(DATE_RANGE).join(word.split("DATE_RANGE"))
    else:
        return word

def format_header(header):
    text = [check_word(word) for word in header]
    return ' '.join(text)

def format_string(text):
    lst = text.split(' ')
    new_text = [check_word(x) for x in lst]
    return ' '.join(new_text)

def count_length(text):
    count = 0

    for c in text:
        if c == ' ':
            count += 1

    return count

def get_opener():
    phrase = random.choice(opener_list)
    phrase = format_string(phrase)
    length = count_length(phrase)

    return phrase, length

def get_phrase(count):
    phrase = ""
    length = 0

    if count == 0:
        phrase, length = get_opener()
    else:
        random_select = random.choice(phrase_list)
        phrase = format_string(random_select)
        length = count_length(phrase)

    return phrase, length

def generate_text(limit):
    text = ""
    count = 0

    while count < limit:
        phrase, length = get_phrase(count)
        text += ' ' + phrase
        count += length

    text = add_header(text)

    return text
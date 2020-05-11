import os
import random
import datetime
import argparse
import config

header = None
phrase_list = []
opener_list = []
keyword_list = []

PROJECT_FOLDER = None
KEYWORDS_FILE = None
REPORT_NO = None
DATE_RANGE = None

def load_items(folder, filename):
    items = []

    items_file = os.path.join(folder, filename)
    if os.path.exists(items_file):
        with open(items_file) as f:
            items = f.read().rstrip().split(';')
    else:
        print("ERROR: Can't find {} to read from!".format(items_file))

    return items

def load_keywords(path=None, keywords_file=None):
    if keywords_file is None:
        keywords_file = KEYWORDS_FILE

    if path is None:
        path = config.CONFIG_FOLDER

    return load_items(path, keywords_file)

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
    today = datetime.date.today()
    first_day = today + datetime.timedelta(days=-5)
    today = today.strftime(config.DATE_FORMAT)
    first_day = first_day.strftime(config.DATE_FORMAT)

    return first_day + ' - ' + today

def load_constants(args):
    global REPORT_NO
    global DATE_RANGE
    global KEYWORDS_FILE
    global PROJECT_NAME

    PROJECT_NAME = args.project
    KEYWORDS_FILE = args.keywords

    if args.number == -1:
        report_no = get_report_count(PROJECT_NAME) + 1
    else:
        report_no = args.number

    date_range = get_date_range()

    REPORT_NO = report_no
    DATE_RANGE = date_range

def load_header(header_file=""):
    if header_file == "":
        header_file = config.HEADER

    with open(header_file) as f:
        header = f.read().rstrip().split(' ')

    return header

def check_word(word):
    if "KEYWORD" in word:
        return random.choice(keyword_list)
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

def generate_report(limit):
    text = ""
    count = 0

    while count < limit:
        phrase, length = get_phrase(count)
        text += ' ' + phrase
        count += length

    return text

def write_report(project, report):
    if not os.path.exists(project):
        os.mkdir(project)

    report_file = os.path.join(project, str(get_report_count(project) + 1) + '.report')
    with open(report_file, "w") as f:
        f.write(report)

def init():
    global header
    global phrase_list
    global keyword_list
    global opener_list

    parser = argparse.ArgumentParser()

    parser.add_argument('-l', '--limit', type=int, default=config.WORD_LIMIT)
    parser.add_argument('-p', '--project', type=str, default=config.PROJECT_NAME)
    parser.add_argument('-n', '--number', type=int, default=-1)
    parser.add_argument('-k', '--keywords', type=str, default=config.KEYWORDS_FILE)

    args = parser.parse_args()

    load_constants(args)

    keyword_list = load_keywords()
    opener_list  = load_openers()
    phrase_list  = load_phrases()
    header       = load_header()

    return args

def main():
    args = init()

    report = generate_report(args.limit)
    write_report(args.project, report)

if __name__ == "__main__":
    main()

from functools import cmp_to_key
from pypinyin import lazy_pinyin, Style

def toPinyin(str_info):
    return lazy_pinyin(str_info, style=Style.TONE3)

def comparePaper(paper1, paper2):
    if paper1.year > paper2.year:
        return 1
    if paper1.year < paper2.year:
        return -1

    if paper1.pub_time > paper2.pub_time:
        return 1
    if paper1.pub_time < paper2.pub_time:
        return -1

    d1 = toPinyin(paper1.degree)
    d2 = toPinyin(paper2.degree)

    if d1 > d2:
        return 1
    if d1 < d2:
        return -1

    a1 = toPinyin(paper1.author)
    a2 = toPinyin(paper2.author)

    if a1 > a2:
        return 1
    if a1 < a2:
        return -1

    return 0

def sortPaper(paper_list) -> bool:
    paper_list.sort(key=cmp_to_key(comparePaper))
    return True

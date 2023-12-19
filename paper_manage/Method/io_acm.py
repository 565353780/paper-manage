import os

from paper_manage.Config.teacher import TEACHERS
from paper_manage.Data.paper import Paper

def loadACMFile(acm_file_path):
    if not os.path.exists(acm_file_path):
        print('[ERROR][io::loadACMFile]')
        print('\t acm file not exist!')
        print('\t acm_file_path:', acm_file_path)
        return None

    with open(acm_file_path, 'r') as f:
        lines = f.readlines()

    paper_list = []

    paper = Paper()
    paper.section = 'Unknown'
    paper.degree = 'Unknown'

    for line in lines:
        if line == '\n':
            continue

        full_info = line.split('\n')[0]

        info = full_info.split('. ACM Trans.')[0]
        paper_start_idx = info.rfind('.', 0)
        title = info[paper_start_idx + 2:]
        res_info = info[:paper_start_idx]
        year_start_idx = res_info.rfind('.', 0)
        year = res_info[year_start_idx + 2:]
        authors = res_info[:year_start_idx]
        if ',' not in authors:
            authors = authors.split(' and ')
        else:
            authors = authors.replace('and ', '').split(', ')

        pub_time = full_info.split('(')[1].split(')')[0]

        teachers = []
        for author in authors:
            if author in TEACHERS:
                teachers.append(author)

        paper.title = title
        paper.author = authors[0]
        paper.school = 'University of Science and Technology of China'
        paper.year = year
        paper.teachers = teachers
        paper.pub_time = pub_time
        paper.full_info = full_info

        if not paper.isValid():
            print('[ERROR][io_acm::loadACMFile]')
            print('\t paper isValid failed!')
            print('\t line:', line)
            paper.outputInfo(1)
            exit()

        paper_list.append(paper.copy())
        paper.reset()
        paper.section = 'Unknown'
        paper.degree = 'Unknown'

    return paper_list

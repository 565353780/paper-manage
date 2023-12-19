import os

from paper_manage.Data.paper import Paper

def loadZhiwangFile(zhiwang_file_path):
    if not os.path.exists(zhiwang_file_path):
        print('[ERROR][io::loadZhiwangFile]')
        print('\t zhiwang file not exist!')
        print('\t zhiwang_file_path:', zhiwang_file_path)
        return None

    with open(zhiwang_file_path, 'r') as f:
        lines = f.readlines()

    paper_list = []

    paper = Paper()
    paper.section = 'Unknown'
    paper.full_info = 'Unknown'

    for line in lines:
        if paper.isValid():
            paper_list.append(paper.copy())
            paper.reset()
            paper.section = 'Unknown'
            paper.full_info = 'Unknown'
            continue

        if 'Title-题名' in line:
            if paper.title is not None:
                print('[ERROR][io::loadZhiwangFile]')
                print('\t title already exist!')
                paper.outputInfo(1)
                exit()
            paper.title = line.split('\n')[0].split('Title-题名: ')[1]
            continue
        if 'Author-作者' in line:
            if paper.author is not None:
                print('[ERROR][io::loadZhiwangFile]')
                print('\t author already exist!')
                paper.outputInfo(1)
                exit()
            paper.author = line.split('\n')[0].split('Author-作者: ')[1]
            continue
        if 'Source-学位授予单位' in line:
            if paper.school is not None:
                print('[ERROR][io::loadZhiwangFile]')
                print('\t school already exist!')
                paper.outputInfo(1)
                exit()
            paper.school = line.split('\n')[0].split('Source-学位授予单位: ')[1]
            continue
        if 'Year-年' in line:
            if paper.year is not None:
                print('[ERROR][io::loadZhiwangFile]')
                print('\t year already exist!')
                paper.outputInfo(1)
                exit()
            paper.year = line.split('\n')[0].split('Year-年: ')[1]
            continue
        if 'Teacher-导师' in line:
            if len(paper.teachers) > 0:
                print('[ERROR][io::loadZhiwangFile]')
                print('\t teachers already exist!')
                paper.outputInfo(1)
                exit()
            paper.teachers = line.split('\n')[0].split('Teacher-导师: ')[1].split(';')
            continue
        if 'Degree-学位' in line:
            if paper.degree is not None:
                print('[ERROR][io::loadZhiwangFile]')
                print('\t degree already exist!')
                paper.outputInfo(1)
                exit()
            paper.degree = line.split('\n')[0].split('Degree-学位: ')[1]
            continue
        if 'PubTime-发表时间' in line:
            if paper.pub_time is not None:
                print('[ERROR][io::loadZhiwangFile]')
                print('\t pub_time already exist!')
                paper.outputInfo(1)
                exit()
            paper.pub_time = line.split('\n')[0].split('PubTime-发表时间: ')[1]
            continue

    return paper_list

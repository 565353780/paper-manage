import os

from paper_manage.Data.paper import Paper

def loadWanfangFile(wanfang_file_path):
    if not os.path.exists(wanfang_file_path):
        print('[ERROR][io::loadWanfangFile]')
        print('\t wanfang file not exist!')
        print('\t wanfang_file_path:', wanfang_file_path)
        return None

    with open(wanfang_file_path, 'r') as f:
        lines = f.readlines()

    paper_list = []

    paper = Paper()

    for line in lines:
        if paper.isValid():
            paper_list.append(paper.copy())
            paper.reset()
            continue

        if '{Title}' in line:
            if paper.title is not None:
                print('[ERROR][io::loadWanfangFile]')
                print('\t title already exist!')
                paper.outputInfo(1)
                exit()
            paper.title = line.split('\n')[0].split('{Title}: ')[1]
            continue
        if '{Author}' in line:
            if paper.author is not None:
                print('[ERROR][io::loadWanfangFile]')
                print('\t author already exist!')
                paper.outputInfo(1)
                exit()
            paper.author = line.split('\n')[0].split('{Author}: ')[1]
            continue
        if '{Publisher}' in line:
            if paper.school is not None:
                continue

                print('[ERROR][io::loadWanfangFile]')
                print('\t school already exist!')
                paper.outputInfo(1)
                exit()
            paper.school = line.split('\n')[0].split('{Publisher}: ')[1]
            continue
        if '{Section}' in line:
            if paper.section is not None:
                print('[ERROR][io::loadWanfangFile]')
                print('\t section already exist!')
                paper.outputInfo(1)
                exit()
            paper.section = line.split('\n')[0].split('{Section}: ')[1]
            continue
        if '{Year}' in line:
            if paper.year is not None:
                print('[ERROR][io::loadWanfangFile]')
                print('\t year already exist!')
                paper.outputInfo(1)
                exit()
            paper.year = line.split('\n')[0].split('{Year}: ')[1]
            continue
        if '{Tertiary Author}' in line:
            if len(paper.teachers) > 0:
                print('[ERROR][io::loadWanfangFile]')
                print('\t teachers already exist!')
                paper.outputInfo(1)
                exit()
            paper.teachers = line.split('\n')[0].split('{Tertiary Author}: ')[1][1:-1].split(', ')
            continue
        if '{Type of Work}' in line:
            if paper.degree is not None:
                print('[ERROR][io::loadWanfangFile]')
                print('\t degree already exist!')
                paper.outputInfo(1)
                exit()
            paper.degree = line.split('\n')[0].split('{Type of Work}: ')[1]
            continue
        if '{Date}' in line:
            if paper.pub_time is not None:
                print('[ERROR][io::loadWanfangFile]')
                print('\t pub_time already exist!')
                paper.outputInfo(1)
                exit()
            paper.pub_time = line.split('\n')[0].split('{Date}: ')[1]
            continue

    return paper_list



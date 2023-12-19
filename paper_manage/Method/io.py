from paper_manage.Method.io_wanfang import loadWanfangFile
from paper_manage.Method.io_zhiwang import loadZhiwangFile
from paper_manage.Method.io_acm import loadACMFile

def saveToSheet(sheet, paper_list: list) -> bool:
    sheet.write(0, 0, 'Author')
    sheet.write(0, 1, 'Title')
    sheet.write(0, 2, 'School')
    sheet.write(0, 3, 'Section')
    sheet.write(0, 4, 'Year')
    sheet.write(0, 5, 'Teachers')
    sheet.write(0, 6, 'Degree')
    sheet.write(0, 7, 'PubTime')
    sheet.write(0, 8, 'FullInfo')

    for i, paper in enumerate(paper_list):
        sheet.write(i + 1, 0, paper.author)
        sheet.write(i + 1, 1, paper.title)
        sheet.write(i + 1, 2, paper.school)
        sheet.write(i + 1, 3, paper.section)
        sheet.write(i + 1, 4, paper.year)
        sheet.write(i + 1, 5, paper.getTeachersStr())
        sheet.write(i + 1, 6, paper.degree)
        sheet.write(i + 1, 7, paper.pub_time)
        sheet.write(i + 1, 8, paper.full_info)
    return True

import os
import xlwt

from paper_manage.Method.path import createFileFolder, removeFile

from paper_manage.Module.paper_filter import PaperFilter

class PaperManager(PaperFilter):
    def __init__(self) -> None:
        super().__init__()
        return

    def toExcel(self, save_excel_file_path: str, overwrite: bool=False) -> bool:
        if os.path.exists(save_excel_file_path):
            if overwrite:
                removeFile(save_excel_file_path)
            else:
                print('[ERROR][PaperManager::toExcel]')
                print('\t save excel file already exist!')
                print('\t save_excel_file_path:', save_excel_file_path)
                return False

        createFileFolder(save_excel_file_path)

        workbook = xlwt.Workbook(encoding='utf-8')
        sheet = workbook.add_sheet('Papers')

        papers = self.paper_list
        if len(self.filter_papers) > 0:
            papers = self.filter_papers

        sheet.write(0, 0, 'Author')
        sheet.write(0, 1, 'Title')
        sheet.write(0, 2, 'School')
        sheet.write(0, 3, 'Section')
        sheet.write(0, 4, 'Year')
        sheet.write(0, 5, 'Teachers')
        sheet.write(0, 6, 'Degree')
        sheet.write(0, 7, 'PubTime')

        for i, paper in enumerate(papers):
            sheet.write(i + 1, 0, paper.author)
            sheet.write(i + 1, 1, paper.title)
            sheet.write(i + 1, 2, paper.school)
            sheet.write(i + 1, 3, paper.section)
            sheet.write(i + 1, 4, paper.year)
            sheet.write(i + 1, 5, paper.teachers)
            sheet.write(i + 1, 6, paper.degree)
            sheet.write(i + 1, 7, paper.pub_time)

        workbook.save(save_excel_file_path)
        return True

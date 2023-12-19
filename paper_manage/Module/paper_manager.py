import os
import xlwt
from typing import Union
from copy import deepcopy

from paper_manage.Module.paper_loader import PaperLoader
from paper_manage.Method.path import createFileFolder, removeFile
from paper_manage.Method.filter import filterPapersByDegree, filterPapersBySchool
from paper_manage.Method.sort import sortPaper
from paper_manage.Method.io import saveToSheet

class PaperManager(PaperLoader):
    def __init__(self) -> None:
        super().__init__()
        return

    def toExcel(self, save_excel_file_path: str, valid_schools: Union[list, None]=None, overwrite: bool=False) -> bool:
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
        sheet1 = workbook.add_sheet('Papers1')
        sheet2 = workbook.add_sheet('Papers2')

        valid_papers = deepcopy(self.paper_list)
        if valid_schools is not None:
            valid_papers = filterPapersBySchool(valid_papers, valid_schools)
        papers1 = filterPapersByDegree(valid_papers, ['硕士'])
        papers2 = filterPapersByDegree(valid_papers, ['博士'])

        sortPaper(papers1)
        sortPaper(papers2)

        saveToSheet(sheet1, papers1)
        saveToSheet(sheet2, papers2)

        workbook.save(save_excel_file_path)
        return True

    def toACMExcel(self, save_excel_file_path: str, overwrite: bool=False) -> bool:
        if os.path.exists(save_excel_file_path):
            if overwrite:
                removeFile(save_excel_file_path)
            else:
                print('[ERROR][PaperManager::toACMExcel]')
                print('\t save excel file already exist!')
                print('\t save_excel_file_path:', save_excel_file_path)
                return False

        createFileFolder(save_excel_file_path)

        workbook = xlwt.Workbook(encoding='utf-8')
        sheet = workbook.add_sheet('Papers')

        papers = deepcopy(self.paper_list)

        sortPaper(papers)

        saveToSheet(sheet, papers)

        workbook.save(save_excel_file_path)
        return True

import os

from paper_manage.Data.paper import Paper
from paper_manage.Method.io import loadWanfangFile, loadZhiwangFile

class PaperLoader(object):
    def __init__(self) -> None:
        self.paper_list = []
        return

    def reset(self) -> bool:
        self.paper_list = []
        return True

    def addPaper(self, paper: Paper, ignore_same: bool=True) -> bool:
        for i in range(len(self.paper_list)):
            if self.paper_list[i].title == paper.title:
                if ignore_same:
                    return True

                print('[WARN][PaperLoader::addPaper]')
                print('\t paper title already exist!')
                print('\t paper:')
                paper.outputInfo(1)
                print('\t already exist paper:')
                self.paper_list[i].outputInfo(1)
                return False

        self.paper_list.append(paper)
        return True

    def loadWanfangPapers(self, wanfang_data_file_path: str, ignore_same: bool=True) -> bool:
        paper_list = loadWanfangFile(wanfang_data_file_path)

        if paper_list is None:
            print('[ERROR][PaperLoader::loadWanfangPapers]')
            print('\t loadWanfangFile failed!')
            return False

        for paper in paper_list:
            self.addPaper(paper, ignore_same)
        return True

    def loadWanfangPapersFolder(self, wanfang_data_folder_path: str, ignore_same: bool=True) -> bool:
        if not os.path.exists(wanfang_data_folder_path):
            print('[ERROR][PaperLoader::loadWanfangPapers]')
            print('\t wanfang data folder not exist!')
            print('\t wanfang_data_folder_path:', wanfang_data_folder_path)
            return False

        wanfang_data_file_name_list = os.listdir(wanfang_data_folder_path)

        for wanfang_data_file_name in wanfang_data_file_name_list:
            if wanfang_data_file_name[-4:] != '.txt':
                continue
            wanfang_data_file_path = wanfang_data_folder_path + wanfang_data_file_name

            self.loadWanfangPapers(wanfang_data_file_path, ignore_same)
        return True

    def loadZhiwangPapers(self, zhiwang_data_file_path: str, ignore_same: bool=True) -> bool:
        paper_list = loadZhiwangFile(zhiwang_data_file_path)

        if paper_list is None:
            print('[ERROR][PaperLoader::loadZhiwangPapers]')
            print('\t loadZhiwangFile failed!')
            return False

        for paper in paper_list:
            self.addPaper(paper, ignore_same)
        return True

    def loadZhiwangPapersFolder(self, zhiwang_data_folder_path: str, ignore_same: bool=True) -> bool:
        if not os.path.exists(zhiwang_data_folder_path):
            print('[ERROR][PaperLoader::loadZhiwangPapers]')
            print('\t zhiwang data folder not exist!')
            print('\t zhiwang_data_folder_path:', zhiwang_data_folder_path)
            return False

        zhiwang_data_file_name_list = os.listdir(zhiwang_data_folder_path)

        for zhiwang_data_file_name in zhiwang_data_file_name_list:
            if zhiwang_data_file_name[-4:] != '.txt':
                continue
            zhiwang_data_file_path = zhiwang_data_folder_path + zhiwang_data_file_name

            self.loadZhiwangPapers(zhiwang_data_file_path, ignore_same)
        return True

import os

from paper_manage.Config.filter import MODES
from paper_manage.Data.paper import Paper
from paper_manage.Method.io import loadWanfangFile, loadZhiwangFile, loadACMFile
from paper_manage.Method.sort import toPinyin

class PaperLoader(object):
    def __init__(self) -> None:
        self.paper_list = []
        return

    def reset(self) -> bool:
        self.paper_list = []
        return True

    def addPaperByTitle(self, paper: Paper, ignore_same: bool=True) -> bool:
        for i in range(len(self.paper_list)):
            if self.paper_list[i].title == paper.title:
                if ignore_same:
                    if self.paper_list[i].year > paper.year:
                        self.paper_list.pop(i)
                        self.paper_list.append(paper.copy())
                    return True

                print('[WARN][PaperLoader::addPaperByTitle]')
                print('\t paper title already exist!')
                print('\t paper:')
                paper.outputInfo(1)
                print('\t already exist paper:')
                self.paper_list[i].outputInfo(1)
                return False

        self.paper_list.append(paper.copy())
        return True

    def addPaperByAuthor(self, paper: Paper, ignore_same: bool=True) -> bool:
        for i in range(len(self.paper_list)):
            if self.paper_list[i].author == paper.author:
                if ignore_same:
                    d1 = toPinyin(self.paper_list[i].degree)
                    d2 = toPinyin(paper.degree)
                    if d1 > d2:
                        self.paper_list.pop(i)
                        self.paper_list.append(paper.copy())
                    return True

                print('[WARN][PaperLoader::addPaperByAuthor]')
                print('\t paper title already exist!')
                print('\t paper:')
                paper.outputInfo(1)
                print('\t already exist paper:')
                self.paper_list[i].outputInfo(1)
                return False

        self.paper_list.append(paper.copy())
        return True

    def addPaper(self, paper: Paper, ignore_same: bool=True, filter_mode: str='title') -> bool:
        match filter_mode:
            case 'title':
                return self.addPaperByTitle(paper, ignore_same)
            case 'author':
                return self.addPaperByAuthor(paper, ignore_same)
            case _:
                print('[ERROR][PaperLoader::addPaper]')
                print('\t filter mode not defined!')
                print('\t filter_mode:', filter_mode)
                print('\t valid modes:', ['title', 'author'])
                return False

    def loadWanfangPapers(self, wanfang_data_file_path: str, ignore_same: bool=True, filter_mode: str='title') -> bool:
        paper_list = loadWanfangFile(wanfang_data_file_path)

        if paper_list is None:
            print('[ERROR][PaperLoader::loadWanfangPapers]')
            print('\t loadWanfangFile failed!')
            return False

        for paper in paper_list:
            self.addPaper(paper, ignore_same, filter_mode)
        return True

    def loadWanfangPapersFolder(self, wanfang_data_folder_path: str, ignore_same: bool=True, filter_mode: str='title') -> bool:
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

            self.loadWanfangPapers(wanfang_data_file_path, ignore_same, filter_mode)
        return True

    def loadZhiwangPapers(self, zhiwang_data_file_path: str, ignore_same: bool=True, filter_mode: str='title') -> bool:
        paper_list = loadZhiwangFile(zhiwang_data_file_path)

        if paper_list is None:
            print('[ERROR][PaperLoader::loadZhiwangPapers]')
            print('\t loadZhiwangFile failed!')
            return False

        for paper in paper_list:
            self.addPaper(paper, ignore_same, filter_mode)
        return True

    def loadZhiwangPapersFolder(self, zhiwang_data_folder_path: str, ignore_same: bool=True, filter_mode: str='title') -> bool:
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

            self.loadZhiwangPapers(zhiwang_data_file_path, ignore_same, filter_mode)
        return True

    def loadACMPapers(self, acm_data_file_path: str, ignore_same: bool=True, filter_mode: str='title') -> bool:
        paper_list = loadACMFile(acm_data_file_path)

        if paper_list is None:
            print('[ERROR][PaperLoader::loadACMPapers]')
            print('\t loadACMFile failed!')
            return False

        for paper in paper_list:
            self.addPaper(paper, ignore_same, filter_mode)
        return True

    def loadACMPapersFolder(self, acm_data_folder_path: str, ignore_same: bool=True, filter_mode: str='title') -> bool:
        if not os.path.exists(acm_data_folder_path):
            print('[ERROR][PaperLoader::loadACMPapers]')
            print('\t acm data folder not exist!')
            print('\t acm_data_folder_path:', acm_data_folder_path)
            return False

        acm_data_file_name_list = os.listdir(acm_data_folder_path)

        for acm_data_file_name in acm_data_file_name_list:
            if acm_data_file_name[-4:] != '.txt':
                continue
            acm_data_file_path = acm_data_folder_path + acm_data_file_name

            self.loadACMPapers(acm_data_file_path, ignore_same, filter_mode)
        return True

from paper_manage.Module.paper_filter import PaperFilter

def demo():
    data_folder_path = '/home/chli/Nutstore Files/My-Materials/GCL年会/视频/毕业论文数据/'
    wanfang_data_folder_path = data_folder_path + '万方/'
    zhiwang_data_folder_path = data_folder_path + '知网/'
    ignore_same = True
    valid_schools = ['中国科学技术大学']

    paper_filter = PaperFilter()
    paper_filter.loadWanfangPapersFolder(wanfang_data_folder_path, ignore_same)
    paper_filter.loadZhiwangPapersFolder(zhiwang_data_folder_path, ignore_same)

    paper_filter.filterPapersBySchool(valid_schools)
    print(len(paper_filter.filter_papers))
    return True

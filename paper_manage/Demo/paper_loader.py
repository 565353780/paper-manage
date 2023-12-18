from paper_manage.Module.paper_loader import PaperLoader

def demo():
    data_folder_path = '/home/chli/Nutstore Files/My-Materials/GCL年会/视频/毕业论文数据/'
    wanfang_data_folder_path = data_folder_path + '万方/'
    zhiwang_data_folder_path = data_folder_path + '知网/'
    ignore_same = True
    valid_schools = ['中国科学技术大学']

    paper_loader = PaperLoader()
    paper_loader.loadWanfangPapersFolder(wanfang_data_folder_path, ignore_same)
    paper_loader.loadZhiwangPapersFolder(zhiwang_data_folder_path, ignore_same)

    papers = paper_loader.getPapersBySchool(valid_schools)
    print(len(papers))
    return True

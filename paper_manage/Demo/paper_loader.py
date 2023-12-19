from paper_manage.Module.paper_loader import PaperLoader

def demo():
    data_folder_path = '/home/chli/Nutstore Files/My-Materials/GCL年会/视频/毕业论文数据/Source/'
    wanfang_data_folder_path = data_folder_path + 'Wanfang/'
    zhiwang_data_folder_path = data_folder_path + 'Zhiwang/'
    ignore_same = True

    paper_loader = PaperLoader()
    paper_loader.loadWanfangPapersFolder(wanfang_data_folder_path, ignore_same)
    paper_loader.loadZhiwangPapersFolder(zhiwang_data_folder_path, ignore_same)

    print('load papers num =', len(paper_loader.paper_list))
    return True

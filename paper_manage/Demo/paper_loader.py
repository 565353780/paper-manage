from paper_manage.Module.paper_loader import PaperLoader

def demo():
    data_folder_path = '/home/chli/Nutstore Files/My-Materials/GCL年会/视频/毕业论文数据/'
    wanfang_data_file_path = data_folder_path + '万方/陈仁杰.txt'

    paper_loader = PaperLoader()
    paper_loader.loadWanfangData(wanfang_data_file_path)
    return True

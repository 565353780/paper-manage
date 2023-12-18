from paper_manage.Module.paper_manager import PaperManager

def demo():
    data_folder_path = '/home/chli/Nutstore Files/My-Materials/GCL年会/视频/毕业论文数据/'
    wanfang_data_folder_path = data_folder_path + '万方/'
    zhiwang_data_folder_path = data_folder_path + '知网/'
    ignore_same = True
    save_excel_file_path = '/home/chli/Nutstore Files/My-Materials/GCL年会/视频/毕业论文数据/all.xls'
    valid_schools = ['中国科学技术大学']
    overwrite = True

    paper_manager = PaperManager()
    paper_manager.loadWanfangPapersFolder(wanfang_data_folder_path, ignore_same)
    paper_manager.loadZhiwangPapersFolder(zhiwang_data_folder_path, ignore_same)

    paper_manager.toExcel(save_excel_file_path, valid_schools, overwrite)
    return True

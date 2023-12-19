from paper_manage.Module.paper_manager import PaperManager

def demo():
    data_folder_path = '/home/chli/Nutstore Files/My-Materials/GCL年会/视频/毕业论文数据/Source/'
    wanfang_data_folder_path = data_folder_path + 'Wanfang/'
    zhiwang_data_folder_path = data_folder_path + 'Zhiwang/'
    ignore_same = True
    filter_mode = 'author'
    save_excel_file_path = '/home/chli/Nutstore Files/My-Materials/GCL年会/视频/毕业论文数据/all.xls'
    valid_schools = ['中国科学技术大学']
    overwrite = True

    paper_manager = PaperManager()
    paper_manager.loadWanfangPapersFolder(wanfang_data_folder_path, ignore_same, filter_mode)
    paper_manager.loadZhiwangPapersFolder(zhiwang_data_folder_path, ignore_same, filter_mode)

    paper_manager.toExcel(save_excel_file_path, valid_schools, overwrite)
    return True

def demo_acm():
    data_folder_path = '/home/chli/Nutstore Files/My-Materials/GCL年会/视频/毕业论文数据/Source/'
    acm_data_folder_path = data_folder_path + 'ACM/'
    ignore_same = True
    filter_mode = 'title'
    save_excel_file_path = '/home/chli/Nutstore Files/My-Materials/GCL年会/视频/毕业论文数据/all_acm.xls'
    overwrite = True

    paper_manager = PaperManager()
    paper_manager.loadACMPapersFolder(acm_data_folder_path, ignore_same, filter_mode)

    paper_manager.toACMExcel(save_excel_file_path, overwrite)
    return True

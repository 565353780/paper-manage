from paper_manage.Module.paper_loader import PaperLoader

class PaperFilter(PaperLoader):
    def __init__(self) -> None:
        super().__init__()
        return

    def getPapersBySchool(self, valid_schools: list) -> list:
        paper_list = []

        for paper in self.paper_list:
            if paper.school not in valid_schools:
                continue

            paper_list.append(paper.copy())

        return paper_list

from paper_manage.Module.paper_loader import PaperLoader

class PaperFilter(PaperLoader):
    def __init__(self) -> None:
        super().__init__()

        self.filter_papers = []
        return

    def reset(self) -> bool:
        super().reset()

        self.filter_papers = []
        return True

    def filterPapersBySchool(self, valid_schools: list) -> bool:
        self.filter_papers = []

        for paper in self.paper_list:
            if paper.school not in valid_schools:
                continue

            self.filter_papers.append(paper.copy())

        return True

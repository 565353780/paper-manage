def filterPapersBySchool(paper_list, valid_schools: list) -> list:
    filter_papers = []

    for paper in paper_list:
        if paper.school not in valid_schools:
            continue

        filter_papers.append(paper.copy())

    return filter_papers

def filterPapersByDegree(paper_list, valid_degrees: list) -> list:
    filter_papers = []

    for paper in paper_list:
        if paper.degree not in valid_degrees:
            continue

        filter_papers.append(paper.copy())

    return filter_papers

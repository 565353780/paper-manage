class Paper(object):
    def __init__(self,
                 title: str,
                 author: str,
                 school: str,
                 year: int,
                 teachers: list,
                 degree: str,
                 pub_time: str) -> None:
        self.title = title
        self.author = author
        self.school = school
        self.year = year
        self.teachers = teachers
        self.degree = degree
        self.pub_time = pub_time
        return

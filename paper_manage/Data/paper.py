from typing import Union
from copy import deepcopy

class Paper(object):
    def __init__(self,
                 title: Union[str, None]=None,
                 author: Union[str, None]=None,
                 school: Union[str, None]=None,
                 section: Union[str, None]=None,
                 year: Union[str, None]=None,
                 teachers: list=[],
                 degree: Union[str, None]=None,
                 pub_time: Union[str, None]=None,
                 pub_location: Union[str, None]=None,
                 full_info: Union[str, None]=None) -> None:
        self.title = title
        self.author = author
        self.school = school
        self.section = section
        self.year = year
        self.teachers = teachers
        self.degree = degree
        self.pub_time = pub_time
        self.pub_location = pub_location
        self.full_info = full_info
        return

    def reset(self) -> bool:
        self.title = None
        self.author = None
        self.school = None
        self.section = None
        self.year = None
        self.teachers = []
        self.degree = None
        self.pub_time = None
        self.pub_location = None
        self.full_info = None
        return True

    def isValid(self) -> bool:
        if self.title is None:
            return False
        if self.author is None:
            return False
        if self.school is None:
            return False
        if self.section is None:
            return False
        if self.year is None:
            return False
        if len(self.teachers) == 0:
            return False
        if self.degree is None:
            return False
        if self.pub_time is None:
            return False
        if self.pub_location is None:
            return False
        if self.full_info is None:
            return False
        return True

    def copy(self):
        return deepcopy(self)

    def getTeachersStr(self) -> str:
        teachers_str = self.teachers[0]
        for i in range(1, len(self.teachers)):
            teachers_str += ', ' + self.teachers[i]
        return teachers_str

    def outputInfo(self, info_level=0) -> bool:
        start = '\t' * info_level
        print(start + '[Paper]')
        print(start + '\t title:', self.title)
        print(start + '\t author:', self.author)
        print(start + '\t school:', self.school)
        print(start + '\t section:', self.section)
        print(start + '\t year:', self.year)
        print(start + '\t teachers:', self.teachers)
        print(start + '\t degree:', self.degree)
        print(start + '\t pub_time:', self.pub_time)
        print(start + '\t pub_location:', self.pub_location)
        print(start + '\t full_info:', self.full_info)
        return True

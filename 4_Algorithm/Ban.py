class Ban:
    def __init__(self, no=None):
        self.no = no
        self.student_list = []

    def __str__(self):
        return "<{}반> {}명".format(self.no, self.count_student())

    def __lt__(self, other):
        if isinstance(other, Ban):
            return self.no < other.no
        else:
            return self.no < other

    def __eq__(self, other):
        if isinstance(other, Ban):
            return self.no == other.no
        else:
            return self.no == other
        
    def count_student(self):
        """
        해당 반에 속에있는 학생들 수
        :return:
        """
        return len(self.student_list)
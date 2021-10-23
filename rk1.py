from operator import itemgetter

class course:
    def __init__(self, id, number, faculty):
        self.id = id
        self.number = number
        self.faculty = faculty

class group:
    def __init__(self, id, name, amount, course_id):
        self.id = id
        self.name = name
        self.amount = amount
        self.course_id = course_id

class group_course:
    def __init__(self, group_id, course_id):
        self.group_id = group_id
        self.course_id = course_id

courses = [
    course(1, 2 , 'ИУ'),
    course(2, 1, 'ИУ'),
    course(3, 3, 'ИУ'),
    course(4, 1, 'БМТ'),
    course(5, 2, 'БМТ'),
]

group_s = [
    group(1, 'ИУ-21', 20, 1),
    group(2, 'ИУ-31', 25, 3),
    group(3, 'ИУ-14', 30, 2),
    group(4, 'БМТ-12', 31, 4),
    group(5, 'ИУ-13', 28, 2),
]

group_course_s = [
    group_course(1, 2),
    group_course(2, 3),
    group_course(3, 2),
    group_course(4, 4),
    group_course(5, 2),
]

def main():
    one_to_many = [(g.name, g.amount, c.faculty)
        for g in group_s
        for c in courses
        if g.course_id == c.id]

    many_to_many_temp = [(c.faculty, gc_s.course_id, gc_s.group_id)
        for c in courses
        for gc_s in group_course_s
        if c.id == gc_s.course_id]

    many_to_many = [(g.name, g.amount, course_name)
        for course_name, course_id, group_id in many_to_many_temp
        for g in group_s if g.id == group_id]

    print('Задание Б1')
    res_11 = sorted(one_to_many, key=itemgetter(0))
    print(res_11)

    print('\nЗадание Б2')
    res_12_unsorted = []
    for c in courses:
        courses_s = list(filter(lambda i: i[2]==c.faculty, one_to_many))
        if len(courses_s) > 0:
            courses_amount = [amount for _,amount,_ in courses_s]
            courses_amount_sum = sum(courses_amount)
            res_12_unsorted.append((c.faculty, courses_amount_sum))

    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)

    print('\nЗадание Б3')
    res_13 = {}
    for c in courses:
        if len(c.faculty) > 0:
            courses_s = list(filter(lambda i: i[2]==c.faculty, many_to_many))
            courses_s_name = [x for x,_,_ in courses_s]
            res_13[c.faculty] = courses_s_name

    print(res_13)

if __name__ == '__main__':
    main()
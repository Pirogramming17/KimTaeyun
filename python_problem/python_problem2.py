# 함수 이름은 변경 가능합니다.
class Student:
    def __init__(self, name, mid, final):
        self.name = name
        self.mid = mid
        self.final = final
        self.avg = (self.mid + self.final) / 2
        self.grade = ''

    def grading(self):
        if self.avg >= 90:
            self.grade = 'A'
        elif self.avg >= 80:
            self.grade = 'B'
        elif self.avg >= 70:
            self.grade = 'C'
        else:
            self.grade = 'D'


class alrExists(Exception):
    def __init__(self):
        super().__init__('Already exist name!')


class nobodyPresent(Exception):
    def __init__(self):
        super().__init__('No student data!')


class ungraded(Exception):
    def __init__(self):
        super().__init__('There is a student who didn\'t get grade.')


class notPresent(Exception):
    def __init__(self):
        super().__init__('Not exist name!')


studentList = []


##############  menu 1
def Menu1(name, mid, final):
    student = Student(name, mid, final)
    studentList.append(student)


##############  menu 2
def Menu2():
    for student in studentList:
        if student.grade == '':
            student.grading()


##############  menu 3
def Menu3():
    print('-------------------------')
    print('name  mid  final  grade')
    print('-------------------------')
    for student in studentList:
        print(student.name, student.mid, student.final, student.grade, sep='    ')


##############  menu 4
def Menu4(leavingName):
    for student in studentList:
        if student.name == leavingName:
            studentList.remove(student)


# 학생 정보를 저장할 변수 초기화
print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True:
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1":
        # 학생 정보 입력받기
        # 예외사항 처리(데이터 입력 갯수, 이미 존재하는 이름, 입력 점수 값이 양의 정수인지)
        # 예외사항이 아닌 입력인 경우 1번 함수 호출
        try:
            name, mid, final = input('Enter name mid-score final-score : ').split(' ')
        except ValueError:
            print('Num of data is not 3!')
        else:
            try:
                for student in studentList:
                    if student.name == name:
                        raise alrExists
                lastMid, lastFinal = int(mid), int(final)
            except alrExists as e:
                print(e)
            except ValueError:
                print('Score is not positive Integer!')
            else:
                if lastMid < 0 or lastFinal < 0:
                    print('Score is not positive Integer!')
                    break
                else:
                    # no errors found ... can move onto to next step
                    Menu1(name, lastMid, lastFinal)

    elif choice == "2":
        # 예외사항 처리(저장된 학생 정보의 유무)
        # 예외사항이 아닌 경우 2번 함수 호출
        # "Grading to all students." 출력
        try:
            if len(studentList) == 0:
                raise nobodyPresent
        except nobodyPresent as e:
            print(e)
        else:
            print('Grading to all students.')
            Menu2()

    elif choice == "3":
        # 예외사항 처리(저장된 학생 정보의 유무, 저장되어 있는 학생들의 학점이 모두 부여되어 있는지)
        # 예외사항이 아닌 경우 3번 함수 호출
        try:
            if len(studentList) == 0:
                raise nobodyPresent
        except nobodyPresent as e:
            print(e)
        else:
            try:
                for student in studentList:
                    if student.grade == '':
                        raise ungraded
            except ungraded as e:
                print(e)
            else:
                Menu3()

    elif choice == "4":
        # 예외사항 처리(저장된 학생 정보의 유무)
        # 예외사항이 아닌 경우, 삭제할 학생 이름 입력 받기
        # 입력 받은 학생의 존재 유무 체크 후, 없으면 "Not exist name!" 출력
        # 있으면(예를 들어 kim 이라 하면), 4번 함수 호출 후에 "kim student information is deleted." 출력
        try:
            if len(studentList) == 0:
                raise nobodyPresent
        except nobodyPresent as e:
            print(e)
        else:
            try:
                leavingName = input('Enter the name to delete : ')
                present = False
                for student in studentList:
                    if student.name == leavingName:
                        present = True
                if not present:
                    raise notPresent
            except notPresent as e:
                print(e)
            else:
                Menu4(leavingName)
                print(leavingName, ' student information is deleted.', sep='')
    elif choice == "5":
        # 프로그램 종료 메세지 출력
        # 반복문 종료
        print("Exit program!")
        exit()

    else:
        # "Wrong number. Choose again." 출력
        print('Wrong number. Choose again.')

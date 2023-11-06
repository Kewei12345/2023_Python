class Course:

    def __init__(self, Title, Max):

        self.CourseTitle = Title
        self.MaxStudents = Max
        self.NumberOfLessons = 0
        self.CourseLesson = []
        self.CourseAssessment = None


    def AddLesson(self, Lesson):

        if self.NumberOfLessons < 50:
            self.NumberOfLessons += 1
            self.CourseLesson.append(Lesson)
        else:
            print("Lesson Full")


    def AddAssessment(self, Assessment):

        self.CourseAssessment = Assessment


    def OutputCourseDetails(self):

        print(f"Course Title: {self.CourseTitle}")
        print(f"Max Students: {self.MaxStudents}")
        print(f"Number of Lessons: {self.NumberOfLessons}")
        print("Course Lessons:")
        for Lesson in self.CourseLesson: 
            print(f" {Lesson}")
        print(f"Course Assessment: {self.CourseAssessment}")
    

class Lesson:

    def __init__(self, Title, Minutes, Lab):
    
        self.LessonTitle = Title
        self.DurationMinutes = Minutes
        self.RequiresLab = Lab


    def OutputLessonDetails(self):
        
        print(self.LessonTitle)
        print(self.DurationMinutes)
        print(self.RequiresLab)

    
class Assessment:

    def __init__(self, Title, Marks):

        self.Title = Title
        self.Marks = Marks

    def OutputAssessmentDetails(self):

        print(self.Title)
        print(self.Marks)

Kewei = Course("My Title", 20)
MyLesson1 = Lesson("Lesson Title", 20, "Lab 3")
Kewei.AddLesson(MyLesson1)
MyAssessment = Assessment("Assessment Title", 69)
Kewei.AddAssessment(MyAssessment)
MyLesson2 = Lesson("Lesson 2", 30, "lab gay")
Kewei.OutputCourseDetails()
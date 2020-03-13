from django.db import models

# University model
class University(models.Model):
    university_short_title = models.CharField('Название Вуза(Сокращенно)', max_length = 20)
    university_title = models.CharField('Название Вуза', max_length = 200)

    def __str__(self):
        return self.university_short_title

    class Meta:
        verbose_name = 'ВУЗ'
        verbose_name_plural = 'ВУЗЫ'

# Faculty model
class Faculty(models.Model):
    university = models.ForeignKey(University, on_delete = models.CASCADE)
    faculty_short_title = models.CharField('Название Факультета(Сокращенно)', max_length = 20)
    faculty_title = models.CharField('Название Факультета', max_length = 200)
    
    def __str__(self):
        return self.faculty_short_title 

    class Meta:
        verbose_name = 'Факультет'
        verbose_name_plural = 'Факультеты'

# Department model
class Department(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete = models.CASCADE)
    department_short_title = models.CharField('Название Кафедры(Сокращенно)', max_length = 20)
    department_title = models.CharField('Название Кафедры', max_length = 200)
    
    def __str__(self):
        return self.department_short_title

    class Meta:
        verbose_name = 'Кафедра'
        verbose_name_plural = 'Кафедры'

# Specialty model
class Specialty(models.Model):
    department = models.ForeignKey(Department, on_delete = models.CASCADE)
    specialty_title = models.CharField('Название Специальности', max_length = 200)
    
    def __str__(self):
        return self.specialty_title
    
    class Meta:
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'

# Group model
class Group(models.Model):
   specialty = models.ForeignKey(Specialty, on_delete = models.CASCADE)
   group_title = models.CharField('Название Группы', max_length = 50)
   
   def __str__(self):
       return self.group_title
   
   class Meta:
       verbose_name = 'Группа'
       verbose_name_plural = 'Группы'

# Student model
class Student(models.Model):
    student_surname = models.CharField('Фамилия', max_length = 200)
    student_name = models.CharField('Имя', max_length = 200)
    student_patronymic = models.CharField('Отчество', max_length = 200)
    student_sex = models.CharField('Пол', max_length = 1)
    group = models.ForeignKey(Group, on_delete = models.CASCADE)
	
    def __str__(self):
        return self.student_surname
    
    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

# Teacher model
class Teacher(models.Model):
    teacher_surname = models.CharField('Фамилия', max_length = 200)
    teacher_name = models.CharField('Имя', max_length = 200)
    teacher_patronymic = models.CharField('Отчество', max_length = 200)
    teacher_sex = models.CharField('Пол', max_length = 1)
	
    def __str__(self):
        return self.teacher_surname
	
    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'

# Subject model alpha v1
class Subject(models.Model):
   specialty = models.ForeignKey(Specialty, on_delete = models.CASCADE)
   group = models.ForeignKey(Group, on_delete = models.CASCADE)
   subject_title = models.CharField('Название Предмета', max_length = 50)
   
   def __str__(self):
       return self.subject_title
   
   class Meta:
       verbose_name = 'Предмет'
       verbose_name_plural = 'Предметы'

# Mark model alpha v1
class Mark(models.Model):
   subject = models.ForeignKey(Subject, on_delete = models.CASCADE)
   student = models.ForeignKey(Student, on_delete = models.CASCADE)
   # maybe mark can be integer/ but we have marks as 'A' 'B' 'F' 
   mark_title = models.CharField('Оценка', max_length = 5)
   
   def __str__(self):
       return self.mark_title
   
   class Meta:
       verbose_name = 'Оценка'
       verbose_name_plural = 'Оценки'


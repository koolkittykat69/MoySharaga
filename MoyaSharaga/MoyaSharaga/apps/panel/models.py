from django.db import models

class University(models.Model):
	university_short_title = models.CharField('Название Вуза(Сокращенно)', max_length = 20)
	university_title = models.CharField('Название Вуза', max_length = 200)

	def __str__(self):
		return self.university_short_title
	class Meta:
		verbose_name = 'ВУЗ'
		verbose_name_plural = 'ВУЗЫ'

class Faculty(models.Model):
	university = models.ForeignKey(University, on_delete = models.CASCADE)
	faculty_short_title = models.CharField('Название Факультета(Сокращенно)', max_length = 20)
	faculty_title = models.CharField('Название Факультета', max_length = 200)
	def __str__(self):
		return self.faculty_short_title 
	class Meta:
		verbose_name = 'Факультет'
		verbose_name_plural = 'Факультеты'

class Department(models.Model):
	faculty = models.ForeignKey(Faculty, on_delete = models.CASCADE)
	department_short_title = models.CharField('Название Кафедры(Сокращенно)', max_length = 20)
	department_title = models.CharField('Название Кафедры', max_length = 200)
	def __str__(self):
		return self.department_short_title 
	class Meta:
		verbose_name = 'Кафедра'
		verbose_name_plural = 'Кафедры'

class Specialty(models.Model):
	department = models.ForeignKey(Department, on_delete = models.CASCADE)
	specialty_title = models.CharField('Название Специальности', max_length = 200)
	def __str__(self):
		return self.specialty_title
	class Meta:
		verbose_name = 'Специальность'
		verbose_name_plural = 'Специальности'

class Student(models.Model):
	student_surname = models.CharField('Фамилия', max_length = 200)
	student_name = models.CharField('Имя', max_length = 200)
	student_patronymic = models.CharField('Отчество', max_length = 200)
	student_group = models.CharField('Группа', max_length = 20)
	student_sex = models.CharField('Пол', max_length = 1)
	specialty = models.ForeignKey(Specialty, on_delete = models.CASCADE)
	def __str__(self):
		return self.specialty_title
	class Meta:
		verbose_name = 'Студент'
		verbose_name_plural = 'Студенты'

class Teacher(models.Model):
	teacher_surname = models.CharField('Фамилия', max_length = 200)
	teacher_name = models.CharField('Имя', max_length = 200)
	teacher_patronymic = models.CharField('Отчество', max_length = 200)
	teacher_sex = models.CharField('Пол', max_length = 1)
	def __str__(self):
		return self.specialty_title
	class Meta:
		verbose_name = 'Преподователь'
		verbose_name_plural = 'Преподователи'

# Create your models here.

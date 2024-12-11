from django.db import models

class CompanyType(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')

    class Meta:
        verbose_name = 'Тип компании'
        verbose_name_plural = 'Типы компаний'

    def __str__(self):
        return self.title


class Client(models.Model):
    company_name = models.CharField(max_length=100, verbose_name='Название')
    logo = models.ImageField(upload_to="media/clients/logos/", verbose_name='Логотип')
    type = models.ForeignKey(CompanyType, on_delete=models.CASCADE, verbose_name='Тип')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.company_name
    

class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')

    class Meta:
        verbose_name = 'Категория проекта'
        verbose_name_plural = 'Категории проектов'

    def __str__(self):
        return self.title


class Project(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.CharField(max_length=255, verbose_name='Краткое описание')
    about = models.TextField(verbose_name='О проекте')
    tasks = models.TextField(verbose_name='Задачи')
    solution = models.TextField(verbose_name='Решение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='projects', verbose_name='Категория')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='projects', verbose_name='Клиент')

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.name


class ProjectPhoto(models.Model):
    image = models.ImageField(upload_to='media/projects/photos/', verbose_name='Изображение')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='photos', verbose_name='Проект')

    class Meta:
        verbose_name = 'Фото проекта'
        verbose_name_plural = 'Фото проектов'

    def __str__(self):
        return f"Photo for {self.project.name}"
from django.db import models


class User(models.Model):
    username = models.CharField(verbose_name='Имя', max_length=50)
    password = models.CharField(widget=forms.PasswordInput)
    email = models.EmailField(max_length=100)

    class Meta:
        verbose_name = 'Создать имя'
        verbose_name_plural = 'Создать имена'


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Основная часть')
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Создать пост'
        verbose_name_plural = 'Создать посты'
        ordering = ('created_at',)

    def __str__(self):
        return self.title

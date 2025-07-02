# Создать двух пользователей
from django.contrib.auth.models import User
user1 = User.objects.create_user('user1')
user2 = User.objects.create_user('user2')

# Создать два объекта модели Author
from godbans.models import Author
author1 = Author.objects.create(user=user1)
author2 = Author.objects.create(user=user2)

# Добавить 4 категории
from godbans.models import Category
category1 = Category.objects.create(name='Спорт')
category2 = Category.objects.create(name='Политика')
category3 = Category.objects.create(name='Образование')
category4 = Category.objects.create(name='Наука')

# Добавить 2 статьи и 1 новость
from godbans.models import Post
post1 = Post.objects.create(author=author1, type='article', title='Статья 1', text='Текст статьи 1')
post2 = Post.objects.create(author=author1, type='article', title='Статья 2', text='Текст статьи 2')
news1 = Post.objects.create(author=author2, type='news', title='Новость 1', text='Текст новости 1')

# Присвоить им категории
post1.categories.set([category1, category2])
post2.categories.set([category3])
news1.categories.set([category4])

# Создать как минимум 4 комментария
from godbans.models import Comment
comment1 = Comment.objects.create(post=post1, user=user1, text='Комментарий 1')
comment2 = Comment.objects.create(post=post1, user=user2, text='Комментарий 2')
comment3 = Comment.objects.create(post=post2, user=user1, text='Комментарий 3')
comment4 = Comment.objects.create(post=news1, user=user2, text='Комментарий 4')

# Применение функций like() и dislike()
post1.like()
post2.like()
post2.like()
news1.dislike()
comment1.like()
comment2.dislike()
comment3.like()
comment4.dislike()

# Обновление рейтинга пользователей
author1.update_rating()
author2.update_rating()

# Вывести username и рейтинг лучшего пользователя
best_author = Author.objects.order_by('-rating').first()
print(best_author.user.username, best_author.rating)

# Вывести информацию о лучшей статье
best_post = Post.objects.order_by('-rating').first()
print(best_post.created_at, best_post.author.user.username, best_post.rating, best_post.title, best_post.preview())

# Вывести все комментарии к лучшей статье
for comment in best_post.comment_set.all():
    print(comment.created_at, comment.user.username, comment.rating, comment.text)
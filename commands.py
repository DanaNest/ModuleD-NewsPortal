# from news.models import *
#
#
# 1. ������� ���� ������������� (� ������� ������ User.objects.create_user('username')).
# u1 = User.objects.create_user('������')
# u2 = User.objects.create_user('������')
#
# 2. ������� ��� ������� ������ Author, ��������� � ��������������.
# Author.objects.create(nickname = u1)
# Author.objects.create(nickname = u2)
# author = Author.objects.get(id=1)
# author2 = Author.objects.get(id=2)
#
# 3. �������� 4 ��������� � ������ Category.
# Category.objects.create(title = '������')
# Category.objects.create(title = '�����')
# Category.objects.create(title = '��������')
# Category.objects.create(title = '��������')
#
# 4. �������� 2 ������ � 1 �������.
# Post.objects.create(author=author, categoryType = 'NW', title = '������� �������� �� �������� � ������', text='�������� ������� �������� (�� 2�3 ��������) ����������� �������� �� ������� ������ (������� �����, ����, ������, �������, �������������� ������ � �������). �������� ����� (�������� 1�2 �������) ������� ������� �� �������� �������, �����, � ������ � �������� � �� ��������. �� ������� ������������ �������� �� ��������������, �� ����������� ��� �������� �������. � �������� � ����������� ���� �������� ���������� ����� �� 20�40 %.')
# Post.objects.create(author=author, categoryType = 'AR', title = '������ � ������', text='������� � ��� ����������� ������������� ���������, ������������� ������������ ��� ��������������� ��������� ����������������� ��������� �� ����� ���������������� ������������ ��� �� � ������ ������-�������������� ��������. �� ��, ������ ���������� �������� ��� ��� ���� ������ ������ ��� ������, ��� �������� �� ������������. � �����, ����������������� �������� ������ ������������� ���������� ����� ���� ���������� ����������������. ��� �������, ���������� ������� ���������� ������, �� �������� ����������� ������ ������������ ������������. �� ������� �� ������������ �����, � ����� ��������� �������� ������������ �������������� ��������.')
# Post.objects.create(author=author2, categoryType = 'AR', title = '�������� � �����', text='� XXI �. ����� ���� ������������ ������ ��������, ������������ ������������ ����������� ������ ������. ������ ��������� ������������ ������ � �������� ������ �� �������� �������� �������� ������� ����� �����������. � ������ ����������� ���� ���������� ��������� ����������� ��� � ���������� ������� - ����� �����, �����, ���, ��� � � ������, ������������� ������ ���������� �������� �������� ������� ����� � ����� ������.')
#
# 5. ��������� �� ��������� (��� ������� � ����� ������/������� ������ ���� �� ������ 2 ���������).
# Post.objects.get(id=1).postCategory.add(Category.objects.get(id=1))
# Post.objects.get(id=2).postCategory.add(Category.objects.get(id=2))
# Post.objects.get(id=3).postCategory.add(Category.objects.get(id=2))
# Post.objects.get(id=3).postCategory.add(Category.objects.get(id=3))
#
# 6. ������� ��� ������� 4 ����������� � ������ �������� ������ Post (� ������ ������� ������ ���� ��� ������� ���� �����������).
# Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=1).nickname, text='������������� ���������.')
# Comment.objects.create(commentPost=Post.objects.get(id=2), commentUser=Author.objects.get(id=1).nickname, text='������ - ���� ������������.')
# Comment.objects.create(commentPost=Post.objects.get(id=3), commentUser=Author.objects.get(id=2).nickname, text='�������� � ������ �� �����!')
# Comment.objects.create(commentPost=Post.objects.get(id=3), commentUser=Author.objects.get(id=2).nickname, text='����� ����� ������!')
# Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=1).nickname, text='�������� ��������.')
# Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id=2).nickname, text='�� ����� ������!')
#
# 7. �������� ������� like() � dislike() � �������/�������� � ������������, ��������������� �������� ���� ��������.
# for i in range(30):
#     Post.objects.get(id=1).like()
# for i in range(17):
#     Post.objects.get(id=2).like()
# for i in range(37):
#     Post.objects.get(id=3).like()
#
# for i in range(7):
#     Comment.objects.get(id=1).like()
# for i in range(5):
#     Comment.objects.get(id=2).like()
# for i in range(9):
#     Comment.objects.get(id=3).like()
# for i in range(12):
#     Comment.objects.get(id=4).like()
#
# Comment.objects.get(id=2).dislike()
#
# 8. �������� �������� �������������.
# a = Author.objects.get(id=1)
# b = Author.objects.get(id=2)
# a.update_rating()
# b.update_rating()
# a.ratingAuthor
# b.ratingAuthor
#
# 9. ������� username � ������� ������� ������������ (�������� ���������� � ��������� ���� ������� �������).
# Author.objects.all().order_by('-ratingAuthor').values('nickname__username', 'ratingAuthor')[0]
#
# 10. ������� ���� ����������, username ������, �������, ��������� � ������ ������ ������, ����������� �� ������/��������� � ���� ������.
# print(Post.objects.all().order_by('-rating').values('dataCreation', 'author__nickname__username', 'rating', 'title')[0],
#       Post.objects.all().order_by('-rating')[0].preview())
#
# 11. ������� ��� ����������� (����, ������������, �������, �����) � ���� ������.
# print(Post.objects.all().order_by('-rating')[0].comment_set.all().values('dateCreation', 'commentUser__username', 'text'))
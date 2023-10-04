from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from news.models import PostCategory, Subscriber
from news.tasks import task_about_new_post


@receiver(m2m_changed, sender=PostCategory)
def notify_new_post(sender, instance, **kwargs):
    print('Я задача!!!!!!!!')
    if kwargs['action'] == 'post_add':
        categories = instance.category.all()
        subscribers_emails = []

        for cat in categories:
            subscribers = cat.subscribers.all()
            subscribers_emails += [s.email for s in subscribers]  #список почт подписчиков
        task_about_new_post.delay(instance.preview(), instance.pk, instance.title, subscribers_emails)


# @receiver(m2m_changed, sender=PostCategory)
# def task_about_new_post(sender, instance, **kwargs):
#     if kwargs['action'] == 'post_add':
#         categories = instance.category.all()
#         subscribers_emails = []
#
#         for cat in categories:
#             subscribers = Subscriber.objects.filter(category=cat)
#             subscribers_emails += [s.user.email for s in subscribers]
#
#         send_email.delay(instance.preview(), instance.pk, instance.title, subscribers_emails)




# from django.conf import settings
# from django.core.mail import EmailMultiAlternatives
# from django.db.models.signals import m2m_changed
# from django.dispatch import receiver
# from django.template.loader import render_to_string
#
# from news.models import PostCategory, Subscriber
#
#
# def send_notifications(preview, pk, title, subscribers_emails):
#     html_context = render_to_string(
#         'post_created_email.html',
#         {
#             'text': preview,
#             'link': f'{settings.SITE_URL}/news/{pk}'
#         }
#     )
#
#     msg = EmailMultiAlternatives(
#         subject=title,
#         body='',
#         from_email=settings.DEFAULT_FROM_EMAIL,
#         to=[],
#         bcc=subscribers_emails,        # скрывает адреса получателей
#     )
#
#     msg.attach_alternative(html_context, "text/html")
#     msg.send()
#
#
# @receiver(m2m_changed, sender=PostCategory)
# def notify_about_new_post(sender, instance, **kwargs):
#     if kwargs['action'] == 'post_add':
#         categories = instance.category.all()
#         subscribers_emails = []
#
#         for cat in categories:
#             subscribers = Subscriber.objects.filter(category=cat)
#             subscribers_emails += [s.user.email for s in subscribers]
#             print(subscribers_emails)
#
#         send_notifications(instance.preview(), instance.pk, instance.title, subscribers_emails)
#
#

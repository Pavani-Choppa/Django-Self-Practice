from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Student


@receiver(pre_save, sender=Student)
def student_pre_save(sender, instance, **kwargs):
    print("Before saving student:", instance.name)


@receiver(post_save, sender=Student)
def student_post_save(sender, instance, created, **kwargs):
    if created:
        print("New student created:", instance.name)
    else:
        print("Student updated:", instance.name)
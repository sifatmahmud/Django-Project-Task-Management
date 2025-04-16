from django.db.models.signals import post_save, pre_save, m2m_changed, post_delete
from django.dispatch import receiver
from django.core.mail import send_mail
from tasks.models import Task


@receiver(m2m_changed, sender=Task.assigned_to.through)
def notify_employees_on_task_creation(sender, instance,action, **kwargs):
    if action == 'post_add':
        assigned_emails = [emp.email for emp in instance.assigned_to.all()]

        print("checking", assigned_emails)

        def send_email():
            subject = "New Task Assigned"
            message = f"You have been assigned to the task: {instance.title}"
            from_email = 'codewithsifat@gmail.com'
            recipient_list = assigned_emails

            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

        send_email()


@receiver(post_delete, sender=Task)
def delete_associte_details(sender, instance, **kwargs):
    if instance.details:
        print(instance)
        instance.details.delete()
        print("Deleted successfully")
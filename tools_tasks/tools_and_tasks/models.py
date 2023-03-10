
from django.db import models
from django.contrib.auth.models import User
import datetime
import pytz
from tinymce.models import HTMLField
from django.utils.translation import gettext_lazy as _

utc = pytz.UTC


class Bill(models.Model):
    date = models.DateField(verbose_name=_('Date'), null=True, blank=True)
    number = models.CharField(verbose_name=_('Number of bill'), max_length=10, unique=True)
    client = models.ForeignKey(to='Client', verbose_name=_('Client'), on_delete=models.SET_NULL, null=True, blank=True)
    construction_object = models.ForeignKey(to='ConstructionObject', verbose_name=_('Construction object'),
                                            on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.FloatField(verbose_name=_('Amount'))
    payment_date = models.DateField(verbose_name=_('Payment by date'), null=True, blank=True)
    status_choices = (
        ('p', _('Paid')),
        ('u', _('Unpaid')),
        ('c', _('Canceled'))
    )
    status = models.CharField(verbose_name=_('Status'), max_length=1, choices=status_choices, default='u')

    class Meta:
        ordering = ['payment_date']

    def deadline_overdue(self):
        if self.payment_date:
            return datetime.date.today() > self.payment_date
        else:
            return False

    def unpaid(self):
        if self.status == 'u':
            return True
        else:
            return False

    def __str__(self):
        return f'Date: {self.date},  Number: {self.number}, Amount: {self.amount}'


class Client(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=100, null=True, blank=True)
    contact_phone = models.CharField(verbose_name=_('Contact phone'), max_length=50, null=True, blank=True)
    contact_email = models.CharField(verbose_name=_('Contact email'), max_length=100, null=True, blank=True)
    contact_address = models.CharField(verbose_name=_('Contact address'), max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.title}"


class ConstructionObject(models.Model):
    address = models.CharField(verbose_name=_('Address'), max_length=200)
    manager = models.ForeignKey(User, verbose_name=_('Manager'), on_delete=models.SET_NULL, null=True, blank=True)
    client = models.ForeignKey(to='Client', verbose_name=_('Client'), on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.address}"

    def display_conobj_comments(self):
        return ' | '.join(comment.text for comment in self.construction_object_comments.all())

    display_conobj_comments.short_description = _('Comments')


class ConstructionObjectComment(models.Model):
    construction_object = models.ForeignKey(to='ConstructionObject', verbose_name=_('Construction object'),
                                            on_delete=models.SET_NULL, null=True, blank=True,
                                            related_name='construction_object_comments')
    employee = models.ForeignKey(User, verbose_name=_('Employee'), on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(verbose_name=_('Date'), auto_now_add=True)
    text = models.TextField(verbose_name=_('Comment'), max_length=2000)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.employee} - {self.text}"


class Task(models.Model):
    manager = models.ForeignKey(User, verbose_name=_('Manager'), on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(verbose_name=_("Date"), auto_now_add=True)
    title = models.CharField(verbose_name=_('Task'), max_length=100)
    description = HTMLField(verbose_name=_('Description'), null=True, blank=True)
    deadline = models.DateTimeField(verbose_name=_("Accomplish till"), null=True, blank=True)
    employee = models.ForeignKey(User, verbose_name=_('Employee'), on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name='employee')
    status_choices = (
        ('a', _('Assigned')),
        ('p', _('In progress')),
        ('f', _('Finished')),
        ('c', _('Canceled'))
    )
    status = models.CharField(verbose_name=_('Status'), max_length=1, choices=status_choices, default='a')

    class Meta:
        ordering = ['-date']

    def deadline_overdue(self):
        if self.deadline:
            return datetime.datetime.today().replace(tzinfo=utc) > self.deadline.replace(tzinfo=utc)
        else:
            return False

    def not_finished(self):
        if self.status == 'a' or self.status == 'p':
            return True
        else:
            return False

    def __str__(self):
        return f'{self.title}'

    def display_task_comments(self):
        return ' | '.join(comment.text for comment in self.task_comments.all())

    display_task_comments.short_description = _('Comments')


class TaskComment(models.Model):
    task = models.ForeignKey(to='Task', verbose_name=_('Task'), on_delete=models.SET_NULL, null=True, blank=True,
                             related_name='task_comments')
    employee = models.ForeignKey(User, verbose_name=_('Employee'), on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(verbose_name=_('Date'), auto_now_add=True)
    text = models.TextField(verbose_name=_('Comment'), max_length=2000)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.employee} - {self.text}"


class Tool(models.Model):
    title = models.CharField(verbose_name=_('Tool'), max_length=100)
    inventory_number = models.CharField(verbose_name=_('Inventory number'), max_length=100, unique=True)
    employee = models.ForeignKey(User, verbose_name=_('Employee'), on_delete=models.SET_NULL, null=True, blank=True)
    construction_object = models.ForeignKey(to='ConstructionObject', verbose_name=_('Construction object'),
                                            on_delete=models.SET_NULL, null=True, blank=True)
    status_choices = (
        ('a', _('Available')),
        ('b', _('Broken')),
        ('r', _('In repair')),
        ('t', _('Taken'))
    )
    status = models.CharField(verbose_name=_('Status'), max_length=1, choices=status_choices, default='a')
    picture = models.ImageField(verbose_name=_('Picture'), upload_to='pictures', null=True, blank=True)

    def __str__(self):
        return f'{self.title}'

    def ready(self):
        if self.status == 'a':
            return True
        else:
            return False

    def display_tool_comments(self):
        return ' | '.join(comment.text for comment in self.tool_comments.all())

    display_tool_comments.short_description = _('Comments')


class ToolComment(models.Model):
    tool = models.ForeignKey(to='Tool', verbose_name=_('Tool'), on_delete=models.SET_NULL, null=True, blank=True,
                             related_name='tool_comments')
    employee = models.ForeignKey(User, verbose_name=_('Employee'), on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(verbose_name=_('Date'), auto_now_add=True)
    text = models.TextField(verbose_name=_('Comment'), max_length=2000)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.employee} - {self.text}"

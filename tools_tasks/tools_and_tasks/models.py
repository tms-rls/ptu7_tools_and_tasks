
from django.db import models
# import datetime


class Bill(models.Model):
    date = models.DateField(verbose_name='Date', null=True, blank=True)
    number = models.CharField(verbose_name='Number of bill', max_length=10, help_text='Insert number of bill')
    client = models.ForeignKey(to='Client', on_delete=models.SET_NULL, null=True, blank=True)
    construction_object = models.ForeignKey(to='ConstructionObject', on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.FloatField(verbose_name='Amount', help_text='Insert amount of the bill')
    payment_date = models.DateField(verbose_name='Payment by date', null=True, blank=True)
    status_choices = (
        ('p', 'Paid'),
        ('u', 'Unpaid'),
        ('c', 'Canceled')
    )
    status = models.CharField(verbose_name='Status', max_length=1, choices=status_choices, default='u',
                              help_text='Status of the bill')

    class Meta:
        ordering = ['payment_date']

    def __str__(self):
        return f'Date: {self.date},  Number: {self.number}, Amount: {self.amount}'


class Client(models.Model):
    title = models.CharField(verbose_name='Title', max_length=100, null=True, blank=True,
                             help_text="Insert client's title")
    contact_phone = models.CharField(verbose_name='Contact phone', max_length=50,
                                     help_text="Insert client's contact phone number", null=True, blank=True)
    contact_email = models.CharField(verbose_name='Contact email', max_length=100,
                                     help_text="Insert client's contact email", null=True, blank=True)
    contact_address = models.CharField(verbose_name='Contact address', max_length=50,
                                       help_text="Insert client's contact address", null=True, blank=True)

    def __str__(self):
        return f"{self.title}"


class Employee(models.Model):
    name = models.CharField(verbose_name='Name', max_length=100, help_text="Insert employee's name")
    surname = models.CharField(verbose_name='Surname', max_length=100, help_text="Insert employee's surname")
    position = models.CharField(verbose_name='Position', max_length=100, null=True, blank=True,
                                help_text="Insert employee's position")

    def __str__(self):
        return f"{self.name} {self.surname}"


class ConstructionObject(models.Model):
    address = models.CharField(verbose_name='Address', max_length=200,
                               help_text='Insert address of construction object')
    manager = models.ForeignKey(to='Employee', on_delete=models.SET_NULL, null=True, blank=True)
    client = models.ForeignKey(to='Client', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.address}"


class Task(models.Model):
    date = models.DateTimeField(verbose_name="Date", auto_now_add=True)
    title = models.CharField(verbose_name='Task', max_length=100, help_text='Insert task')
    notes = models.TextField(verbose_name='Notes', max_length=2000, null=True, blank=True,
                             help_text="Insert task's notes")
    deadline = models.DateTimeField(verbose_name="Accomplish till", null=True, blank=True)
    employee = models.ForeignKey(to='Employee', on_delete=models.SET_NULL, null=True, blank=True)
    status_choices = (
        ('a', 'Assigned'),
        ('p', 'In progress'),
        ('f', 'Finished'),
        ('c', 'Canceled')
    )
    status = models.CharField(verbose_name='Status', max_length=1, choices=status_choices, default='a',
                              help_text='Status of the task')

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f'{self.title} {self.deadline}'


class Tool(models.Model):
    title = models.CharField(verbose_name='Tool', max_length=100, help_text='Insert tool')
    inventory_number = models.CharField(verbose_name='Inventory number', max_length=100,
                                        help_text='Insert inventory number')
    employee = models.ForeignKey(to='Employee', on_delete=models.SET_NULL, null=True, blank=True)
    construction_object = models.ForeignKey(to='ConstructionObject', on_delete=models.SET_NULL, null=True, blank=True)
    status_choices = (
        ('a', 'Available'),
        ('b', 'Broken'),
        ('r', 'In repair'),
        ('t', 'Taken')
    )
    status = models.CharField(verbose_name='Status', max_length=1, choices=status_choices, default='a',
                              help_text='Status of the tool')

    def __str__(self):
        return f'{self.title}'

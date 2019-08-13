from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse


# Create your models here.
class Book(models.Model):
    book_id=models.IntegerField()
    book_title=models.CharField(max_length=200)
    number_of_copies=models.IntegerField()
    #borrower_id=models.IntegerField()
    #borrower_id=models.ForeignKey(library.Borrower, related_name='library')
    borrowed_on=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.book_title

class Borrower(models.Model):
    borrower_id = models.IntegerField()
    book=models.ForeignKey(Book)
    borrower_name=models.CharField(max_length=200)
    borrower_emailid=models.EmailField(max_length=250)

    def __str__(self):
        return self.borrower_name


class Reviewer(models.Model):
    reviewer_id=models.IntegerField()
    reviewer_name=models.CharField(max_length=200)
    reviewer_emailid=models.EmailField(max_length=250)
    reviewer_comments=models.TextField(default='', blank=True)

class Transaction(models.Model):
    sender_id=models.IntegerField()
    receiver_id = models.IntegerField()
    OTP_sent=models.IntegerField()
    OTP_receved=models.IntegerField()
    transaction_status=models.BooleanField()

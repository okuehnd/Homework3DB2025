from django.db import models

# Create your models here.
class Book(models.Model):
    bid = models.IntegerField(primary_key=True)
    title = models.CharField(blank=True, null=True)
    genre = models.CharField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book'


class BookCopy(models.Model):
    copyid = models.IntegerField(primary_key=True)
    bid = models.ForeignKey(Book, models.DO_NOTHING, db_column='bid', blank=True, null=True)
    lid = models.ForeignKey('LibraryBranch', models.DO_NOTHING, db_column='lid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_copy'


class LibraryBranch(models.Model):
    lid = models.IntegerField(primary_key=True)
    lname = models.CharField(blank=True, null=True)
    laddress = models.CharField(blank=True, null=True)        

    class Meta:
        managed = False
        db_table = 'library_branch'


class Loan(models.Model):
    mid = models.OneToOneField('Member', models.DO_NOTHING, db_column='mid', primary_key=True)  # The composite primary key (mid, copyid, loandate) found, that is not supported. The first column is selected.
    copyid = models.ForeignKey(BookCopy, models.DO_NOTHING, db_column='copyid')
    loandate = models.DateField()
    returndate = models.DateField(blank=True, null=True)      

    class Meta:
        managed = False
        db_table = 'loan'
        unique_together = (('mid', 'copyid', 'loandate'),)    


class Member(models.Model):
    mid = models.IntegerField(primary_key=True)
    mname = models.CharField(blank=True, null=True)
    mphone = models.CharField(blank=True, null=True)
    maddress = models.CharField(blank=True, null=True)
    membership_type = models.CharField(blank = True, null = True)

    class Meta:
        managed = False
        db_table = 'member'
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,timedelta


class Book(models.Model):
    catchoice= [
        ('education', 'Education'),
        ('entertainment', 'Entertainment'),
        ('comics', 'Comics'),
        ('adventure', 'Adventure'),
        ('humour', 'Humour'),
        ]
    name=models.CharField(max_length=30)
    isbn=models.PositiveIntegerField()
    author=models.CharField(max_length=40)
    publication = models.CharField(max_length=40)
    category=models.CharField(max_length=30,choices=catchoice,default='education')
    def __str__(self):
        return str(self.name)+"["+str(self.isbn)+']'


class StudentExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    enrollment = models.IntegerField()
    #used in issue book
    def __str__(self):
        return self.user.first_name+'['+str(self.enrollment)+']'
    @property
    def get_name(self):
        return self.user.first_name
    @property
    def getuserid(self):
        return self.user.id

def get_expiry():
    return datetime.today() + timedelta(days=7)
class IssuedBook(models.Model):
    enrollment=models.CharField(max_length=30)
    isbn=models.CharField(max_length=30)
    issuedate=models.DateField(auto_now=True)
    expirydate=models.DateField(default=get_expiry)
    def __str__(self):
        return self.enrollment

    # def get_absolute_url(self):
    #     """Returns the URL to access a particular student instance."""
    #     return reverse('student-detail', args=[str(self.id)])

    #def __str__(self):
     #   """String for representing the Model object."""
      #  return f'{self.last_name}, {self.first_name}'



class BookInstance(models.Model):
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    book_title = models.ForeignKey('book', on_delete=models.RESTRICT, null=True)
    due_back = models.DateField(null=True, blank=True)

    BOOK_STATUS = (
        ('B', 'borrowed'),
        ('A', 'Available'),
    )

    status = models.CharField(
        max_length=1,
        choices=BOOK_STATUS,
        blank=True,
        default='d',
        help_text='Book availability',
    )

    class Meta:
        ordering = ['due_back']
     
    def __str__(self):
        return str(self.title)

    # def get_absolute_url(self):
    #     """Returns the URL to access a detail record for this book."""
    #     return reverse('book-detail', args=[str(self.id)])


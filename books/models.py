from django.db import models

# Create your models here.
class Author(models.Model):
    AuthorID = models.CharField(max_length=30, blank = True,primary_key = True)
    Name = models.CharField(max_length=30)
    Age = models.CharField(max_length=3, blank = True)
    Country = models.CharField(max_length=30, blank = True)
    def __unicode__(self):
        return u'%s' % (self.AuthorID)
class Book(models.Model):
    ISBN = models.CharField(max_length=10, primary_key = True)
    Title = models.CharField(max_length=100)
    AuthorID = models.ForeignKey(Author)
    Publisher =  models.CharField(max_length=30, blank = True)
    PublishDate = models.DateField(blank = True)
    Price = models.CharField(max_length = 10, blank = True)
#    def __unicode__(self):
#        return u'%s %s %s %s %s %s' % (self.ISBN, self.AuthorID.Name, self.Title, self.Publisher, self.PublishDate, self.Price)
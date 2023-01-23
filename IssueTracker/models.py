from django.db import models
from django.contrib.auth.models import AbstractUser

LEVEL = (
    (0,'level zero'),
    (1,'Level one'),
    (2,'Level two'),
    (3,'Level three'),
)

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
    
class User(AbstractUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=20,unique=True)
    company = models.CharField(max_length=120)
    mobile_number = models.CharField(max_length=10, unique=True)
    level = models.CharField(choices=LEVEL,max_length=20,default=0)

    def __str__(self):
        return self.name
    
class Issue(BaseModel):
    PRIORITY = (
        (3,'HIGH'),
        (2,'MEDIUM'),
        (1,'LOW')
    )
    STATUS = (
        ('pending','Pending'),
        ('solved','Solved'),
        ('forward','Forward')
    )
    MODULE = (
        ('attendence','Attendence'),
        ('payroll','PayRoll'),
        ('leave','Leave'),
        ('calender','Calender'),
        ('worklog','Worklog'),
        ('other','Other'),
    )
    STATUS_CODE = (
        ('404','404'),
        ('304','404'),
        ('500','500'),
        ('501','500'),
        ('502','502'),
        ('other','Other'),
    )

    level = models.CharField(max_length=20,choices=LEVEL,default=1)
    user = models.ForeignKey(User,related_name = 'issues',on_delete = models.CASCADE)
    status_code = models.CharField(choices=STATUS_CODE,max_length=30,default='other')
    module = models.CharField(choices = MODULE,max_length =30,default='other')
    priority = models.CharField(choices = PRIORITY,max_length=30,default='low')
    company_name = models.CharField(max_length=100,blank=True)
    description = models.TextField(blank=True)
    status = models.CharField(choices=STATUS,max_length=20,default='pending')
    upload_file=models.FileField(upload_to='issue_file/',blank=True,null=True,max_length=250)
    
    class Meta:
        permissions = (
            ('view_Issue','can see issue'),
            ('report_issue','user can report issue'),
            ('forward_issue','user can forwad isuue to senior level'),
            ('solve_Issue','can solve Issue'),
        )
    def __str__(self):
        return " Issue priority:  %s, status code:  %s, " % (self.status,self.status_code)


import json
from urllib import response
from rest_framework.test import APIRequestFactory, force_authenticate,APIClient,APITestCase
from IssueTracker.models import Issue, User
from IssueTracker.views import UserView
from django.test import Client
from django.urls import reverse
from rest_framework.authtoken.models import Token
from django.test import Client

# "detail": "Authentication credentials were not provided."
# /api-auth/login/?next=/


class TestAbc(APITestCase):
    Issue = {
        "id":1,
        "status_code": 404,
        "module": "attendence",
        "priority": "1",
        "company_name": "Ayyulogic",
        "description": "it is test",
        "status": "pending",
    }
    # userUrl=reverse('Issue:user-detail',kwargs={"pk":1372})
    
    def userUrl(self, id):
        return reverse('Issue:user-detail',kwargs={"pk":id})
    
    def IssueUrl(self,id):
        return reverse('Issue:issues-detail',kwargs={"pk":id})
    def setUp(self):
        user = User.objects.create(username='admin',is_staff=True,is_active='True')
        user.set_password('12345')
        user.save()
        for i in range(0,3):
            user = User.objects.create(
                username=f'testuser{i}', 
                level=i,
                mobile_number=f'986629030{i}',
                email=f'testuser{i}@gmail.com')
            user.set_password(f'12345{i}')
            user.save()
        self.client.login(username='testuser0', password='123450')
        self.client.post('/user-specific-issue/',data=self.Issue)
    def test_level_zero_post_Issue(self):
        response = self.client.post('/user-specific-issue/',data=self.Issue)
        self.assertEqual(response.status_code,201,response.json())

    def test_user_detail(self):
        id = User.objects.get(username='testuser0')
        response=self.client.get(self.userUrl(id.id))
        self.assertEqual(response.status_code,200)
    
    def test_user_level_one(self):
        self.client.login(username='testuser1', password='123451')
        self.Issue["status"]="forward"
        self.Issue["level"]="1"
        print("-------",self.Issue)
        responseGet=self.client.get('/assigned-issues/')
        self.assertEqual(responseGet.status_code,200,responseGet.json())
        Issueid = Issue.objects.get(status_code=404)
        response =self.client.put(self.IssueUrl(Issueid.id),data=self.Issue)
        self.assertEqual(response.status_code, 200,response.json())
 






data = {
            'username':'hariparsad',
            'first_name':'hariparsad',
            'name':'hariparsad',
            'email':'hariparsad@gmail.com',
            'company':'aayulogic',
            'level':'1',
            'mobile_number':98663820300
        }
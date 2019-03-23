# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from .models import UserProfile

class userView(View):
    def get(self,request):
        all_user=UserProfile.objects.all()
        return render(request,'main.html')



class yonghuView(View):
    def get(self,request):
        return render(request,'yonghu.html')
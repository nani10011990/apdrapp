from django.shortcuts import render
from os import name
from django.shortcuts import render
from django.shortcuts import render
from django.template import Context, loader
from rest_framework import generics
from .models import *
import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core import serializers
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
import json
from datetime import datetime
from django.http import JsonResponse
from fpdf import FPDF 

from django.conf import settings
from django.core.files import File
from django.http import FileResponse
import uuid
import base64
 
def home(request):
         
    template = loader.get_template("index.html")
    
    return HttpResponse(template.render())
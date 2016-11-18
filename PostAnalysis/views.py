from django.shortcuts import render
from senti_classifier import polarity_scores
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse
# Create your views here.
import os
#	print os.path.dirname 



def postanalysis(request):
    return render(request, 'PostAnalysis/PostAnsys.html', {})


def postajax(request):
    if request.method == 'POST' and request.is_ajax():
        texty = request.POST.get('stringy')
        if texty == "post1":
            comments_post1 = []
            with open('C:\\Users\\Vibhore\\Desktop\\PostAnsys\\PostAnalysis\\post1-reviews.txt', 'r') as f:
                for line in f.readlines():
                    comments_post1.append(line.strip('\n'))
            print comments_post1
#            return render(request, 'PostAnalysis/PostAnsys.html', {'post': comments_post1})
            return HttpResponse(json.dumps({'post': comments_post1}), content_type="application/json")
        elif texty == "post2":
            comments_post2 = []
            with open('C:\\Users\\Vibhore\\Desktop\\PostAnsys\\PostAnalysis\\post2-reviews.txt', 'r') as f:
                for line in f.readlines():
                    comments_post2.append(line.strip('\n'))
            print comments_post2    
#            return render(request, 'PostAnalysis/PostAnsys.html', {'post': comments_post2})
            return HttpResponse(json.dumps({'post': comments_post2}), content_type="application/json")
        elif texty == "post3":
            comments_post3 = []
            with open('C:\\Users\\Vibhore\\Desktop\\PostAnsys\\PostAnalysis\\post3-reviews.txt', 'r') as f:
                for line in f.readlines():
                    comments_post3.append(line.strip('\n'))
            print comments_post3
#            return render(request, 'PostAnalysis/PostAnsys.html', {'post': comments_post3})
            return HttpResponse(json.dumps({'post': comments_post3}), content_type="application/json")

        else:
            comments_post1 = []
            with open('C:\\Users\\Vibhore\\Desktop\\PostAnsys\\PostAnalysis\\post1-reviews.txt', 'r') as f:
                for line in f.readlines():
                    comments_post1.append(line.strip('\n'))
            print comments_post1
#            return render(request, 'PostAnalysis/PostAnsys.html', {'post': comments_post1})
            return HttpResponse(json.dumps({'post': comments_post1}), content_type="application/json")
#    else:
#        return render(request, 'PostAnalysis/PostAnsys.html', {})
	
	
	
	
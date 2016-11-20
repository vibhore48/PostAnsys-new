from django.shortcuts import render
from senti_classifier import polarity_scores
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
import json
from django.http import HttpResponse
# Create your views here.
import os
#	print os.path.dirname 


##@csrf_protect
#def postanalysis(request):
#    return render(request, 'PostAnalysis/PostAnsys.html', {})

#@csrf_protect
def postanalysis(request):
    # print "before if statement"
    # print "not dummy"
    if request.method == 'POST' and request.is_ajax():
        # print "in here"
        # texty = request.POST.get('posting')
        post, texty = request.body.split('=')
        print post, texty
        # print "texty: -" + texty

        if texty == "post1":
            comments_post1 = []
            with open('C:\\Users\\Vibhore\\Desktop\\PostAnsys\\PostAnalysis\\post1-reviews.txt', 'r') as f:
                for line in f.readlines():
                    comments_post1.append(line.strip('\n'))
            print comments_post1
            pos, neg = polarity_scores(comments_post1)
            print pos, neg
#            return render(request, 'PostAnalysis/PostAnsys.html', {'post': comments_post1})
            return HttpResponse(json.dumps({'post': comments_post1, 'pos': pos, 'neg': neg}), content_type="application/json")
        elif texty == "post2":
            comments_post2 = []
            with open('C:\\Users\\Vibhore\\Desktop\\PostAnsys\\PostAnalysis\\post2-reviews.txt', 'r') as f:
                for line in f.readlines():
                    comments_post2.append(line.strip('\n'))
            print comments_post2
            pos, neg = polarity_scores(comments_post2)
            print pos, neg
#            return render(request, 'PostAnalysis/PostAnsys.html', {'post': comments_post2})
            return HttpResponse(json.dumps({'post': comments_post2, 'pos': pos, 'neg': neg}), content_type="application/json")

        elif texty == "post3":
            comments_post3 = []
            with open('C:\\Users\\Vibhore\\Desktop\\PostAnsys\\PostAnalysis\\post3-reviews.txt', 'r') as f:
                for line in f.readlines():
                    comments_post3.append(line.strip('\n'))
            print comments_post3
            pos, neg = polarity_scores(comments_post3)
            print pos, neg
#            return render(request, 'PostAnalysis/PostAnsys.html', {'post': comments_post3})
            return HttpResponse(json.dumps({'post': comments_post3, 'pos': pos, 'neg': neg}), content_type="application/json")

        elif texty == "post4":
            comments_post4 = []
            with open('C:\\Users\\Vibhore\\Desktop\\PostAnsys\\PostAnalysis\\post4-reviews.txt', 'r') as f:
                for line in f.readlines():
                    comments_post4.append(line.strip('\n'))
            print comments_post4
            pos, neg = polarity_scores(comments_post4)
            print pos, neg
#            return render(request, 'PostAnalysis/PostAnsys.html', {'post': comments_post3})
            return HttpResponse(json.dumps({'post': comments_post4, 'pos': pos, 'neg': neg}), content_type="application/json")

        elif texty == "post5":
            comments_post5 = []
            with open('C:\\Users\\Vibhore\\Desktop\\PostAnsys\\PostAnalysis\\post5-reviews.txt', 'r') as f:
                for line in f.readlines():
                    comments_post5.append(line.strip('\n'))
            print comments_post5
            pos, neg = polarity_scores(comments_post5)
            print pos, neg
#            return render(request, 'PostAnalysis/PostAnsys.html', {'post': comments_post3})
            return HttpResponse(json.dumps({'post': comments_post5, 'pos': pos, 'neg': neg}), content_type="application/json")

        else:
            comments_post1 = []
            with open('C:\\Users\\Vibhore\\Desktop\\PostAnsys\\PostAnalysis\\post1-reviews.txt', 'r') as f:
                for line in f.readlines():
                    comments_post1.append(line.strip('\n'))
            print comments_post1
#            return render(request, 'PostAnalysis/PostAnsys.html', {'post': comments_post1})
            return HttpResponse(json.dumps({'post': comments_post1}), content_type="application/json")
    else:
        # print "i am in else"
        return render(request, 'PostAnalysis/PostAnsys.html', {})
	
	
	
	
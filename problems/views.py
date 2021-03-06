from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from problems.models import Country, Answer, Question
from django.http import JsonResponse
from django.core import serializers
import csv
import json
import pdb


class CountryModel():
    def __init__(self,name):
        self.label = name

def autocomplete(request):
    if 'term' in request.GET:
        queryset = Country.objects.filter(name__istartswith=request.GET.get('term',None))
        countries =list()
        for i in queryset:
            temp = CountryModel(i.name)
            country_string = json.dumps(temp.__dict__)
            country_json = json.loads(country_string)
            countries.append(country_json)
        clearSession(request)
    return JsonResponse(countries, safe=False)

class homePage(TemplateView):
    template_name = 'home.html'

def QuestionList(request):
     if request.is_ajax():
         correctAnswer = request.session['check']
         if request.GET.get('clicked') == request.session['check']:
            request.session['correct_answer_count'] += 1
         return JsonResponse({'answerKey':correctAnswer},status = 200)

     if 'country_id' not in request.session:
         search_item = request.GET.get('item')
         request.session['item'] =search_item
         search_destination = Country.objects.filter(name= search_item)

         if len(search_destination) == 0:
              context = {
               'reply' : 'Sorry not available'
               }
              return render(request,'sorry.html',context)
         request.session['country_id']= Country.objects.filter(name = search_item).values('id')[0]['id']

         if 'user_attended_questions' not in request.session:
             context = {
                'question' :Question.objects.filter(country = request.session['country_id']).first()
             }
             total_question = Question.objects.filter(country =request.session['country_id']).count()
             request.session['total_question'] = total_question
             request.session['pending_questions_count'] = total_question
             request.session['user_attended_questions'] = []
             request.session['correct_answer_count'] = 0
             request.session['current_question_id'] = context['question'].id
             answer = Answer.objects.filter(question =context['question'].id)
             request.session['pending_questions_count'] -= 1
             for ans in answer:
                 request.session['check'] = ans.correct
             context['answer'] = answer
             request.session['user_attended_questions'].append(context['question'].id)
             context['total_questions_show'] = len(request.session['user_attended_questions'])
             return render(request, 'problems/question.html',context)

     else:
        context = {
        'question' : Question.objects.filter(country = request.session['country_id']).exclude(id__in = request.session['user_attended_questions'] ).first()
         }
        if context['question'] is None:
            total = len(request.session['user_attended_questions'])
            result = request.session['correct_answer_count']
            context['result'] = result
            context['total'] = total
            clearSession(request)
            return render(request,'result.html',context)

        request.session['current_question_id'] = context['question'].id
        request.session['user_attended_questions'].append(context['question'].id)
        answer = Answer.objects.filter(question =context['question'].id)
        for ans in answer:
           request.session['check'] = ans.correct
        request.session['pending_questions_count'] -= 1
        context['answer'] = answer
        context['total_questions_show'] = len(request.session['user_attended_questions'])
        return render(request, 'problems/question.html',context)


def clearSession(request):
    if  'user_attended_questions' in request.session:
        del request.session['user_attended_questions']
    if 'country_id' in request.session:
        del request.session['country_id']
    if 'correct_answer_count' in request.session:
        del request.session['correct_answer_count']


class indexPage (TemplateView):
    template_name = 'index.html'

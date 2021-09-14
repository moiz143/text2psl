from django.shortcuts import render
from django.http import HttpResponse, request
from django.shortcuts import redirect
from django.template import loader

from .textprocessor import preprocess_text
from .models import Code

from django.http import JsonResponse

from .forms import CodeForm

from googletrans import Translator

from .HamNoSys2SiGML.Original.HamNoSys2SiGML import convert

# import pymysql

def home(request):
    return render(request, 'PROJECTAPP/home.html')


def demo(request):
  if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        # text = request.POST['EngTextarea']
        print('+++++++++++++++++++')
        print(request.POST)
        form = CodeForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
          print('Form is valid')
          print(form.cleaned_data['text'])
          words = preprocess_text(form.cleaned_data['text'])

          print(words)

          hamnosys = ''

          for w in words:
            try:
              code = Code.objects.get(text=w)
              hamnosys = hamnosys + ' ' + code.code
            except:
              print("---------------> Cannot find code for {} in the DB.".format(w))

          xml = convert(hamnosys=hamnosys)

          print(xml)


          # return HttpResponseRedirect('/thanks/')
  return render(request, 'PROJECTAPP/demo.html')


# def demo(request):
#     if request.method == "POST":
#         EngTextarea = request.POST['EngTextarea']
#         print(EngTextarea)
#         connection = pymysql.connect(host="localhost" , user = "root" , passwd = "" , db="pakparse")
#         mycursor = connection.cursor()
#         mycursor.execute("select 'hamnosys' from 'hamtable' where text = EngTextarea")
#         print("ok")
#         connection.commit()
#         connection.close()

#     return render(request, 'PROJECTAPP/demo.html')


def contact(request):
    return render(request, 'PROJECTAPP/contact.html')


def about(request):
    return render(request, 'PROJECTAPP/about.html')


def about_team(request):
    return render(request, 'PROJECTAPP/about_team.html')


def about_credits(request):
    return render(request, 'PROJECTAPP/about_credits.html')


def hamnosys(request):
    return render(request, 'PROJECTAPP/hamnosys.html')

def getCodes(text):
    words = preprocess_text(text.lower())

    hamnosys = ''

    for i, w in enumerate(words):
      try:
        print("===== Words =====")
        print(i , ' -- ', w)
        print(words)
        code = Code.objects.get(text=w)
        print("Fetched Code: ", code.code, " Against: ", w)
        hamnosys = hamnosys + ' ' + code.code
      except:
        if len(w) > 1:
          print("Cannot find code for {}. Breaking it down.".format(w))
          split_word = list(w)
          print(split_word)
          loop_index = i+1
          for x in split_word:
            words.insert(loop_index, x)
            loop_index += 1
          # del(words[len(split_word)+i])
        else:
          print("Cannot find code for {}. Unable to break it down.".format(w))


    xml = convert(hamnosys=hamnosys)

    return xml

def getEnglish(request):
    print('Get Codes Function Executed')
    if request.method == 'POST':
        post_text = request.POST.get('text')
        print(post_text)
        response_data = {}

        form = CodeForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
          print('Form is valid')
          print(form.cleaned_data['text'])

          response_data['xml'] = getCodes(form.cleaned_data['text'])

        return JsonResponse(response_data)
    else:
        return JsonResponse({'details': 'Nothing to see here!'})

def getUrdu(request):
    print('Get Urdu Codes Function Executed')
    if request.method == 'POST':
        post_text = request.POST.get('text')
        print(post_text)
        response_data = {}

        form = CodeForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
          print('Urdu Form is valid')
          print(form.cleaned_data['text'])

          try:

            translator = Translator()

            translated = translator.translate(form.cleaned_data['text'], dest='en')
            print("----------->>> Translated text")
            print(translated.text)
            response_data['xml'] = getCodes(translated.text)
          except:
            print("Unable to perform translation.")


        return JsonResponse(response_data)
    else:
        return JsonResponse({'details': 'Nothing to see here!'})

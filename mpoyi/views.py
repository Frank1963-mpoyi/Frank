from django.shortcuts import render

def paul_draft(request):
    
    
    #context={'paul_draft': }
    template_name ='draft.html'
    return render(request, template_name , context)

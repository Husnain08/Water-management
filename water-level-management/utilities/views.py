from django.shortcuts import render
from django.http import HttpResponse



def index(request):

    return render(request , 'utilities/index.html' )


def data_vis_height(request):

    return render(request , 'utilities/data_vis_height.html' )




#ef data_vis_height(request):
    #return render(request , 'utilities/data_vis_height.html')


#    HttpResponse(


  #      ''' <b> We are at the index function  </b> '''
 #   )

#def level_generator()

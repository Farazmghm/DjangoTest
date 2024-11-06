from django.urls import path
from . import views




urlpatterns = [
    
    path('',views.index),
    path('step1/',views.step1,name='page1'),
    path('step2/',views.step2,name="template2"),
    path('step4/',views.step4,name='page4'),
    path('step5/',views.step5,name='page5'),
    path('step7/',views.step7,name='step7'),
    path('detail/<int:id_feild>',views.detail,name='detail'),
    path('form1/',views.form1),
    path('form2/',views.form2),
    path('render1',views.render1,name="index"),
]
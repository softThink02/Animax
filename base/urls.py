from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'home' ),
    path('signup/', views.signupform, name = 'signup'),
    path('signin/', views.signinform, name='signin'),
    path('logout/', views.logoutUser, name='logout'),
    path('about/', views.about, name='about'),
    path('reset/', views.reset, name='reset'),
    path('resetdone/', views.resetdone, name='resetdone'),
    path('resetconfirm/', views.resetconfirm, name='resetconfirm'),
    path('resetcomplete/', views.resetcomplete, name='resetcomplete'),
    
    path('animation/', views.animation, name='animation'),
    path('faq/', views.faq, name='faq'),
    path('doc_type1/', views.doc_page1, name='doc_page1'),
    path('doc_type2/', views.doc_page2, name='doc_page2'),
    path('doc_type3/', views.doc_page3, name='doc_page3'),
    path('doc_page4/', views.doc_page4, name='doc_page4'),
    path('anim-blink/', views.animation, name='anim-blink'),
    path('anim-blink_two/', views.animation_two, name='anim-blink_two'),
    path('anim-cloud/', views.animation_cloud, name='anim-cloud'),
    path('anim-move/', views.animation_move, name='anim-move'),
    path('anim-move_two/', views.animation_two, name='anim-move_two'),
    path('anim-move3/', views.animation_move3, name='anim-move3'),
    path('anim-move4/', views.animation_move4, name='anim-move4'),
    path('anim-pulse/', views.animation_pulse, name='anim-pulse'),
    path('anim-pulse_two/', views.animation_pulse_two, name='anim-pulse_two'),
    path('anim-rotate_two/', views.animation_rotate_two, name='anim-rotate_two'),
    path('anim-rotate/', views.animation_rotate, name='anim-rotate'),
    path('anim-rotate3/', views.animation_rotate3, name='anim-rotate3'),
    path('anim-rotate4/', views.animation_rotate4, name='anim-rotate4'),
    path('anim-stretch/', views.animation_stretch, name='anim-stretch'),
    path('anim-stretch_two/', views.animation_stretch_two, name='anim-stretch_two'),
    path('anim-stretch3/', views.animation_stretch3, name='anim-stretch3'),
    path('anim-fade/', views.animation_fade, name='anim-fade'),
    path('anim-fade3/', views.animation_fade3, name='anim-fade3'),
    path('anim-fade4/', views.animation_fade4, name='anim-fade4'),
    path('anim-fade_two/', views.animation_fade_two, name='anim-fade_two'),
    path('anim-bounce/', views.animation_bounce, name='anim-bounce'),
    path('anim-bounce_two/', views.animation_bounce, name='anim-bounce_two')
]
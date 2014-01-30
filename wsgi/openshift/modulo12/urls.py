from django.conf.urls import patterns, url

urlpatterns = patterns('openshift.modulo12.views',

            url(r'^estudiantes/$','estudiantesView', name='estudiantesView'),
            url(r'^estudiantes/(?P<id_e>\d+)/$', 'estudianteView', name='estudiante'),
            url(r'^desarrollo/fase1/$','definicionView', name='definicionView'),
            url(r'^desarrollo/$','desarrolloView', name='desarrolloView'),
            url(r'^defensa/$','defensaView', name='defensaView'),
            url(r'^correccion/$','correccionDocenteView', name='correccionDocenteView'),
            url(r'^xxx/$','fasesView', name='fasesView'),


)


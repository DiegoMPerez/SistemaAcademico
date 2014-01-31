from django.conf.urls import patterns, url

urlpatterns = patterns('openshift.modulo12.views',

            url(r'^estudiantes/$','estudiantesView', name='estudiantesView'),
            # Estudiantes con las fases de desarrollo
            url(r'^estudiantes/(?P<id_e>\d+)/desarrollo/$','estudianteView', name='estudianteView'),
            url(r'^estudiantes/(?P<id_e>\d+)/desarrollo/fase(?P<id_f>\d+)/$','definicionView', name='definicionView'),
            url(r'^defensa/$','defensaView', name='defensaView'),
            url(r'^correccion/$','correccionDocenteView', name='correccionDocenteView'),
            url(r'^xxx/$','fasesView', name='fasesView'),
            url(r'^acerca/$','acercaDe_View', name='acercaDe_View'),

            #LOGIN ****************************************************
            url(r'^login/$','loginView', name='loginView'),
            url(r'^logout/$','logoutView', name='logoutView'),
            #LOGIN ****************************************************
)


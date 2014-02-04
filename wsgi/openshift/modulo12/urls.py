from django.conf.urls import patterns, url

urlpatterns = patterns('openshift.modulo12.views',

            url(r'^docente/estudiantes/$','docenteListaEstudiantesView', name='docenteListaEstudiantesView'),
            url(r'^docente/estudiantes/(?P<id_e>\d+)/correccion/$','docenteFasesView', name='docenteFasesView'),
            url(r'^docente/estudiantes/(?P<id_e>\d+)/correccion/fase(?P<id_f>\d+)/$','docenteCorreccionView', name='docenteCorreccionView'),
            # Estudiantes con las fases de desarrollo
            url(r'^estudiantes/$','estudiantesView', name='estudiantesView'),
            url(r'^estudiantes/(?P<id_e>\d+)/desarrollo/$','estudianteView', name='estudianteView'),
            url(r'^estudiantes/(?P<id_e>\d+)/desarrollo/fase(?P<id_f>\d+)/$','definicionView', name='definicionView'),
            url(r'^estudiantes/(?P<id_e>\d+)/defensa/$','defensaView', name='defensaView'),

            url(r'^acerca/$','acercaDe_View', name='acercaDe_View'),

            #LOGIN ****************************************************
            url(r'^accounts/login/$','loginView', name='loginView'),
            url(r'^logout/$','logoutView', name='logoutView'),
            #LOGIN ****************************************************

            url(r'^fases/$','fasesView', name='fasesView'),
            url(r'^registro/$','signup', name='signup'),
            url(r'^$','main', name='main'),

)


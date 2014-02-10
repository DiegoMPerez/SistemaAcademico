from django.conf.urls import patterns, url

urlpatterns = patterns('openshift.modulo12.views',


            #DOCENTES
            url(r'^docente/estudiantes/$','docenteListaEstudiantesView', name='docenteListaEstudiantesView'),
            url(r'^docente/estudiantes/(?P<id_e>\d+)/correccion/$','docenteFasesView', name='docenteFasesView'),
            url(r'^docente/estudiantes/(?P<id_e>\d+)/correccion/fase(?P<id_f>\d+)/$','docenteCorreccionView', name='docenteCorreccionView'),
            url(r'^docente/estudiantes/(?P<id_e>\d+)/defensa/$','defensaView', name='defensaView'),

            # Estudiantes con las fases de desarrollo
            url(r'^estudiantes/$','estudiantesView', name='estudiantesView'),
            url(r'^estudiantes/(?P<id_e>\d+)/desarrollo/$','estudianteView', name='estudianteView'),
            url(r'^estudiantes/(?P<id_e>\d+)/desarrollo/fase(?P<id_f>\d+)/$','definicionView', name='definicionView'),


            #LOGIN ****************************************************
            url(r'^accounts/login/$','loginView', name='loginView'),
            url(r'^logout/$','logoutView', name='logoutView'),

            url(r'^registro/$','signup', name='signup'),

            #JURADOS
            url(r'^jurados/$','juradosView', name='juradosView'),

            #AUDITORIA
            url(r'^auditor/usuarios$','auditoriaUsuariosView', name='auditoriaUsuariosView'),
            url(r'^auditor/modelos$','auditoriaModelosView', name='auditoriaModelosView'),

            #ADMINISTRACION
            #$ FASES
            url(r'^fases/lista/$','fasesView', name='fasesView'),
            url(r'^fases/anadir/$','fasesAddView', name='fasesAddView'),
            url(r'^fases/fase(?P<id_f>\d+)/editar/$','fasesEditView', name='fasesEditView'),
            url(r'^fases/fase(?P<id_f>\d+)/eliminar/$','fasesElimView', name='fasesElimView'),

            #$ ACERCA
            url(r'^acerca/$','acercaDe_View', name='acercaDe_View'),
            url(r'^$','main', name='main'),
            url(r'^pruebaq/$','prueba', name='prueba'),

            #$$  MAESTRO
            url(r'^maestro/$','padreView', name='padreView'),




)


from django.contrib import admin
from safeeduAPI.core.models import Escola, Comentario, Motd, Imagem, LoginLog

admin.site.register(Escola)
admin.site.register(Comentario)
admin.site.register(Motd)
admin.site.register(Imagem)
admin.site.register(LoginLog)

admin.site.site_header = 'Administração da SafeEdu API'                # default: "Django Administration"
#admin.site.index_title = 'Administração do Site'                 # default: "Site administration"
#admin.site.site_title = 'HTML title from adminsitration'            # default: "Django site admin"
from django.contrib import admin
from .models import AcessoMedico, TiposExames, SolicitacaoExame, PedidoExames

admin.site.register(TiposExames)
admin.site.register(SolicitacaoExame)
admin.site.register(PedidoExames)
admin.site.register(AcessoMedico)
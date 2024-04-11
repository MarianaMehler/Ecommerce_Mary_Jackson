from django.urls import path
from app_MJ.views import *

urlpatterns = [
    path('', home, name='home'),
    path('cestas/', cestas, name="cestas"),
    path('sobre/', sobre, name="sobre"),
    path('contato/', contato, name="contato"),
    path('produto-detalhe/<int:produto_id>', produto_detalhe, name="produto_detalhe"),
    path('busca/', busca, name='busca'),
    path('produtos/', produtos, name='produtos'),
    path('cadastro/', cadastro, name='cadastro'),
    path('login/', login_usuario, name='login'),
    path('logout/', logout_usuario, name='logout'),
    path('carrinho/<int:produto_id>', carrinho, name='carrinho'), 
    path('carrinhoproduto/', carrinhoproduto, name='carrinho'),
    
]

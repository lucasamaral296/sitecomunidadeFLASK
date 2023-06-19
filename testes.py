from comunidadeimpressionadora import database, app
from comunidadeimpressionadora.models import Usuario

# with app.app_context():
#     database.create_all()

# with app.app_context():
#     usuario = Usuario(username='Lira', email='Lira@gmail.com', senha='123456')
#     usuario2 = Usuario(username='João', email='Joao@gmail.com', senha='123123123')
#
#     database.session.add(usuario)
#     database.session.add(usuario2)
#
#     database.session.commit()

# with app.app_context():
#     usuario_teste = Usuario.query.all()
#     # usuario2 =Usuario.query.filter_by(username='NovoLucas').first()
#     print(usuario_teste)

   # print(usuario_teste.senha)

# with app.app_context():
#     meu_post = Post(id_usuario=1, titulo='Primeiro posto do lira', corpo='Lira voando')
#     database.session.add(meu_post)
#     database.session.commit()

# with app.app_context():
#     post = Post.query.first()
#     print(post.autor.email)

# with app.app_context():
#     database.drop_all()
#     database.create_all()
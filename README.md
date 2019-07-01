# Centro Quatro Patas

Projecto de Programação em Rede, implementado em Django. Site de uma organização de acolha de animais.

O conteúdo do site é gerado automaticamente de acordo com a base de dados a si ligada. A página inicial mostra os animais contidos na base de dados, e um layout flexbox ajusta o número de colunas à resolução da janela. Clicando na fotografia vai-se para uma página com informação sobre o animal.

O site permite fazer a criação de contas de utilizador. Utilizadores com o login feito podem deixar comentários na página dos animais, marcar encontro para adopção, ou fazer uma doação ao centro. Visto isto ser apenas uma prova deconceito, o mecanismo de doação não está ligado a nenhum banco, mas guarda a quantia da doação, a sua data e hora e o utilizador que a fez na base de dados, e mostra a doação mais recente na página inicial.

Apenas contas de administrador podem manipular a base de dados directamente, e para isso usa-se a página de administração do Django, personalizada para o tipo de conteúdo que esta base de dados tem.

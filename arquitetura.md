

    Projeto/
    ├── __init__.py                    # Pacote Python
    ├── apps/                          # Aplicativos Django
    ├── db.sqlite3                     # Banco de dados SQLite
    ├── media/                         # Arquivos de mídia (por exemplo, uploads de usuários)
    ├── static/                        # Arquivos estáticos (CSS, JavaScript, etc.)
    ├── tests/                         # Testes automatizados
    ├── wsgi.py                        # Configuração para servir a aplicação via WSGI
    ├── __pycache__/                   # Arquivos cache compilados (Python)
    ├── configs/                       # Configurações específicas do projeto
    ├── fixtures/                      # Dados de exemplo para o banco de dados
    ├── middleware.py                  # Middleware personalizado
    ├── templates/                     # Modelos HTML para as views
    ├── urls.py                        # Padrões de URL e configuração de roteamento
├── manage.py                          # Utilitário de linha de comando para gerenciar o projeto


Arquitetura para criar app direto na pasta apps
nomedoprojeto/
├── app/
│   ├── management/
│   │   └── commands/
│   │       └── startapp.py
└── nomedoprojeto/


----------------------------------
configs/settings.py
>STATICFILES_DIRS: Esta configuração define uma lista de diretórios onde o Django procurará arquivos estáticos, como arquivos CSS, JavaScript e imagens. O Django procura esses arquivos em aplicativos individuais e nas pastas especificadas em STATICFILES_DIRS. Aqui, você está adicionando um diretório chamado 'static' no diretório raiz do seu aplicativo ao qual o Django procurará arquivos estáticos.

>FIXTURE_DIRS: As fixtures são arquivos de dados que podem ser usados para preencher o banco de dados com dados iniciais. Esta configuração define uma lista de diretórios onde o Django procurará por esses arquivos de fixtures. No seu caso, você está adicionando um diretório chamado 'fixtures' no diretório raiz do seu aplicativo.

>MEDIA_ROOT: Este é o diretório raiz onde os arquivos de mídia enviados pelos usuários serão armazenados no servidor. Aqui, você está configurando o diretório raiz como 'media/' no diretório raiz do seu aplicativo.

>MEDIA_URL: Esta configuração define o URL base para servir arquivos de mídia. Quando os usuários fazem upload de arquivos, eles podem ser acessados via URL usando esse prefixo. Por padrão, você está configurando isso como 'media/'.

>SESSION_EXPIRE_AT_BROWSER_CLOSE: Esta configuração controla se as sessões de usuário expiram quando o navegador é fechado. Se definido como False, as sessões permanecerão ativas mesmo depois que o navegador for fechado. Se definido como True, as sessões expirarão quando o navegador for fechado.
>SESSION_EXPIRE_AT_BROWSER_CLOSE: Esta configuração controla se as sessões de usuário expiram quando o navegador é fechado. Se definido como False, as sessões permanecerão ativas mesmo depois que o navegador for fechado. Se definido como True, as sessões expirarão quando o navegador for fechado.
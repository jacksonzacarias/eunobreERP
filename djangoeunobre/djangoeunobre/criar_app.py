import os
from django.core.management import call_command

def move_app_to_app_folder(app_name):
    # Diretório raiz do projeto Django
    project_root = os.path.dirname(os.path.abspath(__file__))

    # Caminho do diretório do aplicativo
    app_directory = os.path.join(project_root, app_name)

    # Caminho do diretório "app"
    app_folder = os.path.join(project_root, "apps")

    # Verifica se a pasta "app" existe, senão a cria
    if not os.path.exists(app_folder):
        os.makedirs(app_folder)

    # Move a pasta do aplicativo para a pasta "app"
    os.rename(app_directory, os.path.join(app_folder, app_name))

if __name__ == "__main__":
    # Nome do novo aplicativo
    app_name = input('Nome do novo aplicativo (ou digite -cancelar para cancelar): ').strip()

    if app_name == '-cancelar':
        print('Criação do aplicativo cancelada.')
    else:
        if not app_name:
            raise ValueError('Você precisa fornecer um nome para o novo aplicativo!')

        if ' ' in app_name:
            raise ValueError('O nome do aplicativo não pode conter espaços em branco.')

        # Chame o comando startapp com o diretório de destino personalizado
        call_command('startapp', app_name)

        # Mova o aplicativo para a pasta "app"
        move_app_to_app_folder(app_name)

        print(f"O aplicativo '{app_name}' foi movido para a pasta 'app'.")

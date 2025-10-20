Habilitar scripts no PowerShell ADM --> Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
Criar e ativar o ambiente virtual--> cd C:\TrabalhosVscode\crud_fastapi_jinja --> python -m venv venv --> .\venv\Scripts\Activate.ps1
Instalar as dependências --> pip install -r requirements.txt

- Certifique-se de ter o Python instalado e adicionado ao PATH.
- Use sempre o ambiente virtual para evitar conflitos de dependências com outros projetos.
- Se houver erro ao ativar o ambiente virtual no PowerShell, verifique as permissões de execução de script (veja o passo 1).

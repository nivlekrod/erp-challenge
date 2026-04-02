FROM ubuntu:latest
ENTRYPOINT ["top", "-b"]

# 1. Imagem base: Python estável (slim para ser mais leve)
FROM python:3.12-slim

# 2. Variáveis de ambiente para o Python não criar lixo (.pyc)
# e mandar os logs direto para o terminal
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Definir onde o projeto vai morar dentro do container
WORKDIR /app

# 4. Instalar dependências do sistema (necessárias para o Postgres e compilação)
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# 5. Instalar as dependências do Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copiar o restante do código do seu projeto para dentro do container
COPY . /app/

# 7. Expor a porta que o Django usa
EXPOSE 8000

# 8. Comando para rodar o servidor (0.0.0.0 permite acesso externo ao container)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
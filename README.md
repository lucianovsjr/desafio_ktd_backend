# Olá, candidato(a)!

Este é um breve desafio para avaliar sua familiaridade com algumas tecnologias e procedimentos que utilizamos na Kartado, além da sua capacidade de aprendizado, criatividade, e busca de conhecimento. É muito importante que você leia esse documento atentamente, em sua integridade, para compreender todos os passos do desafio, assim como o método de avaliação.

Em resumo, neste desafio, você iniciará a partir de um projeto de back-end existente, e fará algumas modificações para criar um novo endpoint de API, utilizando os dados pré-fornecidos.

### TECNOLOGIAS

Buscamos envolver nesse desafio:

- Django - framework web para Python
- Django Rest Framework (DRF) – conjunto de extensões para construção de uma API REST com Django
- Git - ferramenta que utilizamos para versionamento de software
- Inglês - já que a documentação das ferramentas está em inglês
- Conceitos básicos de um API REST

### ROTEIRO DO DESAFIO

1. Caso ainda não possua, crie uma conta em uma plataforma online de versionamento de código, como o GitHub, GitLab ou BitBucket;
2. Dentro da plataforma de versionamento de código que você tenha escolhido, você pode tanto criar um novo repositório vazio e copiar os arquivos deste repositório, assim como pode simplesmente fazer um fork deste repositório. O seu repositório será utilizado para armazenar os arquivos resultantes do desafio;
3. Caso ainda não tenha familiaridade com as ferramentas utilizadas, recomendamos um acesso ao site do Django (https://www.djangoproject.com) e do DRF (https://www.django-rest-framework.org) para familiarizar-se com o conceito e capacidades dos frameworks. Ambas as páginas contém documentação completa das ferramentas e tutoriais;
4. Seu ponto de início será o projeto Django que está neste repositório. Note que já existe um app chamado `occurrences`, que contém três modelos:
   - `Occurrence` - representa uma ocorrência de problema no pavimento de uma rodovia
   - `Road`- utilizado para o cadastro de rodovias disponíveis na aplicação
   - `Status` - utilizado para o cadastro de status disponíveis na aplicação
5. Para executar o projeto, os passos são semelhantes a qualquer projeto em Python:
   - Você precisa ter um ambiente de desenvolvimento configurado, com Python 3 e Pip disponíveis;
   - Obtenha os arquivos do projeto (seja através de um `git clone` ou baixando o repositório de outras formas
   - Abra o terminal e entre na pasta raiz do projeto;
   - Crie um novo virtualenv com o comando `python -m virtualenv venv`;
   - Ative seu virtualenv com o comando `source venv/bin/activate`;
   - Instale as dependências com o comando `pip install -r requirements.txt`;
   - Execute os testes com o comando `python manage.py test apps/`;
   - Inicie o servidor com o comando `python manage.py runserver`. Agora você deve conseguir acessar a Browsable API em http://localhost:8000. Note que não é necessário executar um banco de dados, ou executar migrations iniciais, já que o projeto está configurado para utilizar a engine SQLite, com um arquivo que está incluso no repositório;
   - O banco de dados incluso no repositório contém uma conta de usuário criada com username `desafio` e senha `desafio`. Você pode precisar dessas credenciais para fazer login na página da Browsable API.
6. Analise o projeto e repare que já existem endpoints para acessar os modelos `Road` (http://localhost:8000/roads/) e `Status` (http://localhost:8000/status/), mas não existe um endpoint para acessar o modelo `Occurrence`.
7. Seu objetivo é desenvolver um endpoint para acessar o modelo `Occurrence`. Esse endpoint deverá estar acessível em http://localhost:8000/occurrences/, e seu retorno deve ter formato conforme abaixo:

```
{
	"count": 100,
	"next": "http://localhost:8000/occurrences/?page=2",
	"previous": null,
	"results": [{
			"description": "Quiquia modi etincidunt modi.",
			"road": "http://localhost:8000/roads/1/",
			"road_name": "BR-101",
			"km": "65",
			"status": "http://localhost:8000/status/1/",
			"status_name": "Para fazer",
			"created_at": "2021-01-20",
			"updated_at": "2021-01-20"
		},
		{
			"description": "Labore numquam adipisci quisquam ipsum.",
			"road": "http://localhost:8000/roads/2/",
			"road_name": "BR-116",
			"km": "28",
			"status": "http://localhost:8000/status/2/",
			"status_name": "Fazendo",
			"created_at": "2021-01-20",
			"updated_at": "2021-01-20"
		},
		...
	]
}
```

Note que, no caso dos campos relacionais, além do link para o respectivo objeto, existe também um outro campo com sufixo `_name` que contém a informação do campo `name` do objeto relacionado.

8. (OPCIONAL) Caso deseje, você pode fazer quaisquer outras alterações e incrementos no seu projeto.
9. Adicione os alterações ao repositório que você criou ou forkou no passo 2. Você pode fazer um único commit ou commits incrementais, conforme julgar mais adequado;
10. Nos informe a respeito da conclusão do projeto! Caso deseje, você pode nos encaminhar um vídeo ou agendar uma chamada para apresentar o seu desenvolvimento. Precisamos também ver o código-fonte resultante. Ah, e não se esqueça, para que o desafio seja considerado como completo, o projeto precisa estar rodando corretamente!

### AVALIAÇÃO

O seu trabalho será avaliado segundo os seguintes critérios:

- Finalização - O desafio foi concluído?
- Qualidade - Indentação e organização do código.
- Coerência - A solução implementada é coerente com os requisitos apresentados?
- Inovação - Você fez algo além do roteiro do desafio?

Em caso de dúvidas, ou para reportar a finalização do desafio, entre em contato com o seu recrutador ou entrevistador. Caso deseje um feedback detalhado a respeito da avaliação, por favor manifeste esse interesse ao recrutador ou entrevistador.

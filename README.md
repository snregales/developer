# Assessment

## Local

### Requirments

- Python 3.7.*
- Pip3
- Pyenv and Pipenv (alternative virtualenv)
- Docker-compose

### Database

To setup Postgres DB and companion pgAdmin, from project directory run

```sh
docker-compose up -d
```

### Python

Yes there are other ways of running this virtual enviorment, but described below is my workflow setup. If you are curious about it just ask.

#### Pyenv
  
- if the required python version is not yet installed through pyenv install it

to list the python versions

```sh
pyenv install -l
```

```sh
pyenv install <version>
```

- register project's python version

while in the prject root directory

```sh
pyenv local <version>
```

- check if pyenv is running the correct python in local project

while in the project directory

```sh
python -V
```

- update this python pip

```sh
python -m pip install -U pip
```

- install pipenv

```sh
python -m pip install pipenv
```

- create an pipenv alias (optional)

```sh
alias penv='python -m pipenv'
```

#### Pipenv
  
- install all dependencies

```sh
penv install --dev
```

- create a .env file in the project root directory with "DJANGO_SETTINGS_MODULE=config.settings.local" and "SECRET_KEY=some_secret_key"

```sh
echo 'DJANGO_SETTINGS_MODULE=config.settings.local
SECRET_KEY=some_secret_key' > .env
```

### Docs

There are three docs comands

- initialization of sphinx docs (don't run)

```sh
penv run init_docs
```

- compiling project docs, for instance during a project code modification this can run to recompile autodoc

```sh
penv run docs

```

- serving html version of docs most important to you

```sh
penv run html
```

after creating the html files *./docs/build/html/index.html* you can view them on the browser of your choosing

```sh
firefox ./docs/build/html/index.html &
```

### Tests

simplest thing run

```sh
penv run test
```  

### Webservice

- activate containered database
- migrate migrations

```sh
penv run migrate
```

- create a super user (optional)

```sh
penv run manage createsuperuser
```

- start webserver

```sh
penv run server
```

if default port is taken

```sh
penv run server <port>
```

you can either use an aplication such as insomia for request, but the graphql is set as interactive. so you are also able to make requests through the browser

## Project Execution

### Django over Flask

Even tho Django has way more overhead than flask. I am simply more comfortable around the Django environment. Furthermore I love the out of the box manage.py script that makes some development workflow faster than Flask. and lastly Django has a broughter support and use in the industry and show you that I also form part of this community.

### GraphQL over REST

I am very opinionated about this subject I believe that. I would even put myself in the group of people that believe that GrahpQL and gRPC are the future of backend web development. That said I am not blind to the limitations of both, and that are certain scenarios where REST is more benificial than the others.

>Not all problems need to be solved with a hammer

### Tasked done

- ~~Written in Python~~
- ~~Webservice~~
  - ~~POST~~ and only post (graphql)
  - ~~HTTP Error~~ quick and dirty way
  - HTTP status 302
- Datastore
- ~~Mac or Linux Execution~~
- ~~Unit Tests~~
- ~~Clean Code~~ subjective*

### Additional

Since I took so long to pick the Assessment up, I decide to put it live on Heroku

### Done differently

- Keep code base smaller with flask
- Use REST for HTTP status/errors

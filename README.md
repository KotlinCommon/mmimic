# mimic-storyteller-bot-discord

- project based on creating and manipulating bots for discord

#### project creating and compiled in "Pycharm"

#### Python-3.10

#### Requirements in [requirements.txt](requirements.txt)

## Run

 - --------------------------------------------------

```bash
python -m src.python.application.main
```
 - --------------------------------------------------

## Docker

 - --------------------------------------------------

#### Run LOCAL

```bash
sudo docker-compose --env-file=.docker/.env.dev up --build 
```

#### Run PROD

```bash
sudo docker-compose --env-file=.docker/.env.prod up --build 
```

 - --------------------------------------------------

### Clear Docker

```bash
sudo docker-compose down
```

```bash
sudo docker system prune -a
```

 - --------------------------------------------------

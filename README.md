## Switch Environment

```sh
$ pipenv install
$ pipenv shell
```

## Run on your local

```sh
$ python src/main.py
```

## Run with container

```sh
$ vim .env  # 各自設定
$ docker build -t $tag_name .
$ docker run --env-file=.env $tag_name
```

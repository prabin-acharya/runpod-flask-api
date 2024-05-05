
# install caddy
```
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' |  gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg

curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' |  tee /etc/apt/sources.list.d/caddy-stable.list

apt update
```


gunicorn app:app  # runs flask api on port 8000

  
gunicorn -b 0.0.0.0:8000 app:app  

nohup gunicorn -b 0.0.0.0:8000 app:app &  


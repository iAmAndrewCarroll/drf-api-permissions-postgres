

Some Commands

alias dcn="docker container stop $(docker container ls -a -q); docker system prune -a -f --volumes"


http POST :8000/api/token/ username=admin password=admin
 will return your.own.token

http localhost:8000/api/v1/things/ "Authorization: Bearer your.own.token"

docker-compose run web python manage.py migrate
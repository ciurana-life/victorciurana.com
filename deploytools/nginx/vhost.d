location /staticfiles/ {
  alias /home/app/web/staticfiles/;
  add_header Access-Control-Allow-Origin *;
}
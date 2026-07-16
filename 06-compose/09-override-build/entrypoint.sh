#!/bin/bash
sed -i '/<head>/a <meta name="environment" content="development">' /usr/share/nginx/html/index.html
exec "$@"

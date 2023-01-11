MIGRATIONS=app/core/database/migrations
DB=PortionsApp
ENVKEY=MONGODB_CONNECTIONSTRING
URI=$(cd .. \
    | cat .env \
    | grep $ENVKEY \
    | cut -f 2 -d '"')
FORWARD=f
BACKWARD=b

if [ $1 = $FORWARD ]; then
    echo "Running one migration forward"
    beanie migrate -uri $URI -p $MIGRATIONS -db $DB --distance 1
elif [ $1 = $BACKWARD ]; then
    echo "Running one migration backward"
    beanie migrate -uri $URI -p $MIGRATIONS -db $DB --distance 1 --backward
else
    echo "Method not allowed"
fi
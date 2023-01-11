ENVKEY=MONGODB_CONNECTIONSTRING
URI=$(cd .. \
    | cat .env \
    | grep $ENVKEY \
    | cut -f 2 -d '"')

mongodump --uri="$URI"

# mongorestore --uri "mongodb://localhost:27017" --dir=dump

# rm -r dump
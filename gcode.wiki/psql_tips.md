# psql tips

- How to use psql querry from psql user's home directory  
`psql -h $DB_HOST -U DB_USER  -d  $DB_NAME  -c "select * from  ~~ ;" `


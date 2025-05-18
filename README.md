Woodland_ABC_backend
docker-compose build backend
docker-compose up --build       <----------------------------------------
docker exec -i postgres-db psql -U postgres -d mydatabase < backup.sql  <----в базу
docker exec -t postgres-db pg_dump -U postgres -d postgres > backup.sql  <----c бази


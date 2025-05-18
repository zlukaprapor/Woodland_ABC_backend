Woodland_ABC_backend

{
  "username": "testuser1",
  "email": "testuser1@example.com",
  "password": "testpassword1"
}

{
  "username": "testadmin1",
  "email": "testadmin1@example.com",
  "password": "testpassword1"
}

http://localhost:8000/docs
docker-compose build backend
docker-compose up --build       <----------------------------------------
docker exec -i postgres-db psql -U postgres -d mydatabase < backup.sql  <----в базу
docker exec -t postgres-db pg_dump -U postgres -d postgres > backup.sql  <----c бази


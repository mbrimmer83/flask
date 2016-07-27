CREATE TABLE todoList (
  id serial primary KEY,
  content varchar NOT NULL,
  completionDate date,
  complete boolean
)

insert into todoList values (default, 'Code', 2016-07-26, False);

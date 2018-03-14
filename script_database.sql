--Many-to-one
CREATE TABLE "category"(
	"id" int primary key not null,
	"name" varchar(20)
);


CREATE TABLE "post"(
	"id" int primary key not null,
	"title" varchar(50),
	"date" date,
	"time" time,
	"category" int not null,

	constraint fk_post_category
		foreign key (category)
			references category(id)
);

insert into post (id, title, date, time, category) values (1,'ok', '09-07-1992', '00:00', 1);
insert into category (id, name) values (1,'Todas');

select * from post

--One-To-One
CREATE TABLE books (
  id serial,
  title varchar(100) NOT NULL,
  author varchar(100) NOT NULL,
  published_date timestamp NOT NULL,
  isbn char(12),
  PRIMARY KEY (id),
  UNIQUE (isbn)
);

/*
 one to many: Book has many reviews
*/

CREATE TABLE reviews (
  id serial,
  book_id integer NOT NULL,
  reviewer_name varchar(255),
  content varchar(255),
  rating integer,
  published_date timestamp DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (book_id) REFERENCES books(id) ON DELETE CASCADE
);

INSERT INTO books (id, title, author, published_date, isbn) VALUES
  (1, 'My First SQL Book', 'Mary Parker', '2012-02-22 12:08:17.320053-03', '981483029127'),
  (2, 'My Second SQL Book', 'John Mayer', '1972-07-03 09:22:45.050088-07', '857300923713'),
  (3, 'My First SQL Book', 'Cary Flint', '2015-10-18 14:05:44.547516-07', '523120967812');


INSERT INTO reviews (id, book_id, reviewer_name, content, rating, published_date) VALUES
  (1, 1, 'John Smith', 'My first review', 4, '2017-12-10 05:50:11.127281-02'),
  (2, 2, 'John Smith', 'My second review', 5, '2017-10-13 15:05:12.673382-05'),
  (3, 2, 'Alice Walker', 'Another review', 1, '2017-10-22 23:47:10.407569-07');


 select * from reviews where book_id=2


 --One-To-One

CREATE TABLE users(
	id int primary key,
	name varchar(250)
);
 /*
one to one: User has one address
*/
CREATE TABLE addresses (
  id int primary key,
  user_id int, -- Both a primary and foreign key
  street varchar(30) NOT NULL,
  city varchar(30) NOT NULL,
  state varchar(30) NOT NULL,
  FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
);

INSERT INTO users (id, name) VALUES
  (1, 'bruno'),
  (2, 'andre'),
  (3, 'joao');

INSERT INTO addresses (id,user_id, street, city, state) VALUES
  (1,1, '1 Market Street', 'San Francisco', 'CA'),
  (2,2, '2 Elm Street', 'San Francisco', 'CA'),
  (3,3, '3 Main Street', 'Boston', 'MA');

--ManytoMany
-- Create a table for blog entries.
CREATE TABLE entry (
  id      int PRIMARY KEY,
  title   varchar(100),
  content_entry varchar(250)
);

-- Create a table for tags.
CREATE TABLE tag (
  id   int PRIMARY KEY,
  name varchar(50)
);

-- Create a join table to collect tags for entries.

 CREATE TABLE entrytag (
  id int primary key,
  entry_id int NOT NULL,
  tag_id int NOT NULL,
  FOREIGN KEY (entry_id) REFERENCES entry(id) ON DELETE CASCADE,
  FOREIGN KEY (tag_id) REFERENCES tag(id) ON DELETE CASCADE
);

INSERT INTO entry (id, title,content_entry) VALUES (1,'meu primeiro post', 'conteudo do PRIMEIRO POST');
INSERT INTO entry (id, title,content_entry) VALUES (2,'meu segundo post', 'conteudo do SEGUNDO POST');

INSERT INTO tag (id, name) VALUES (1,'Melhores posts');
INSERT INTO tag (id, name) VALUES (2,'Posts aleatorios');
INSERT INTO tag (id, name) VALUES (3,'posts mais acessados');
INSERT INTO tag (id, name) VALUES (4,'recomendados');

INSERT INTO EntryTag (id, entry_id, tag_id) VALUES (1,1, 1);
INSERT INTO EntryTag (id, entry_id, tag_id) VALUES (2,1, 4);


select * from EntryTag

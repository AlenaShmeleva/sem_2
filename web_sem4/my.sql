CREATE TABLE groupmate (
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  address TEXT NOT NULL
);

-- insert
INSERT INTO groupmate (name, age, address) VALUES ('Алёна', '27','Санкт-Петербург');
INSERT INTO groupmate (name, age, address) VALUES ('Александр', '31','Москва');
INSERT INTO groupmate (name, age, address) VALUES ('Михаил', '21','Самара');
INSERT INTO groupmate (name, age, address) VALUES ('Ева', '33','Мурманск');
INSERT INTO groupmate (name, age, address) VALUES ('Мирослав', '24','Москва');
INSERT INTO groupmate (name, age, address) VALUES ('Павел', '36','Владивосток');
INSERT INTO groupmate (name, age, address) VALUES ('Вячеслав', '45','Екатеринбург');
-- fetch 
SELECT name FROM groupmate WHERE address = 'Москва' AND age > 17 AND age < 30;
CREATE TABLE Person(
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  first_name TEXT,
  last_name TEXT,
  middle_name TEXT,
  cell_phone TEXT,
  email TEXT
);

CREATE TABLE Address(
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  line_1 TEXT,
  line_2 TEXT,
  city TEXT,
  state TEXT,
  zip_code TEXT
);

CREATE TABLE Household(
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL
);

CREATE TABLE Business(
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL
);

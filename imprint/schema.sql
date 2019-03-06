DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS product;
DROP TABLE IF EXISTS landing;
DROP TABLE IF EXISTS locations;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL
);

CREATE TABLE posts (
  post_id INTEGER PRIMARY KEY AUTOINCREMENT,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  url TEXT NOT NULL,
  body TEXT,
  plain_body TEXT,
  author_id INTEGER NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);

CREATE TABLE product (
  page_id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  description TEXT NOT NULL,
  filename TEXT NOT NULL,
  bulletpoint1 TEXT,
  bulletpoint2 TEXT,
  bulletpoint3 TEXT,
  bulletpoint4 TEXT,
  bulletpoint5 TEXT,
  author_id INTEGER NOT NULL,
  page_layout TEXT NOT NULL,
  buy_button_text TEXT NOT NULL,
  buy_button_link TEXT,
  url TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);

CREATE TABLE landing (
  page_id INTEGER PRIMARY KEY AUTOINCREMENT,
  heading TEXT NOT NULL,
  subheading TEXT NOT NULL,
  button_text TEXT NOT NULL,
  button_url TEXT,
  author_id INTEGER NOT NULL,
  url TEXT NOT NULL,
  email_cta TEXT,
  FOREIGN KEY (author_id) REFERENCES user (id)
);

CREATE TABLE locations (
  location_id INTEGER PRIMARY KEY AUTOINCREMENT,
  city TEXT NOT NULL,
  state TEXT NOT NULL,
  street TEXT NOT NULL,
  author_id INTEGER NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);
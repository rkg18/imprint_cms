DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS posts;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL
);

CREATE TABLE posts (
  post_id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT UNIQUE NOT NULL,
  url TEXT NOT NULL,
  body TEXT,
  FOREIGN KEY (author_id) REFERENCES username (id)
);
DROP TABLE if EXISTS recipes;
CREATE TABLE recipes (
  r_id integer PRIMARY KEY,
  recipe_id text NOT NULL,
  recipe_name text NOT NULL,
  img_link text NOT NULL,
  recipe_link text NOT NULL
);

DROP TABLE if EXISTS users;
CREATE TABLE users (
  user_id integer PRIMARY KEY,
  username text NOT NULL,
  email text NOT NULL,
  password_hash text NOT NULL
);

DROP TABLE if EXISTS saved_recipes;
CREATE TABLE saved_recipes (
  saved_recipes_id integer PRIMARY KEY,
  user_id integer NOT NULL,
  r_id integer NOT NULL
  -- FOREIGN KEY(recipe_name) REFERENCES recipes(recipe_id),
  -- FOREIGN KEY(username) REFERENCES users(user_id)
);

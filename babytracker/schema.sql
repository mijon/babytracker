DROP TABLE IF EXISTS feed_sessions;
DROP TABLE IF EXISTS feed_subsessions;
DROP TABLE IF EXISTS sleeps;
DROP TABLE IF EXISTS changes;


CREATE TABLE feed_sessions (
								id INTEGER PRIMARY KEY AUTOINCREMENT,
								start_time TIMESTAMP NOT NULL,
								stop_time TIMESTAMP NOT NULL,
								notes TEXT
);

CREATE TABLE feed_subsessions (
								id INTERGER PRIMARY KEY AUTOINCREMENT,
								session_id INTEGER,
								breast CHAR(1),
								start_time TIMESTAMP NOT NULL,
								stop_time TIMESTAMP NOT NULL,
								FOREIGN KEY (session_id) REFERENCES feed_sessions (id)
);

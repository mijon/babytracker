DROP TABLE IF EXISTS feed_sessions;
DROP TABLE IF EXISTS feed_subsessions;
DROP TABLE IF EXISTS sleeps;
DROP TABLE IF EXISTS changes;

DROP TABLE IF EXISTS medications;
DROP TABLE IF EXISTS medications_log;

CREATE TABLE feed_sessions (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	start_time TIMESTAMP NOT NULL,
	stop_time TIMESTAMP NOT NULL,
	notes TEXT
);

CREATE TABLE feed_subsessions (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	session_id INTEGER,
	breast CHAR(1),
	start_time TIMESTAMP NOT NULL,
	stop_time TIMESTAMP NOT NULL,
	FOREIGN KEY (session_id) REFERENCES feed_sessions (id)
);

CREATE TABLE medications (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name VARCHAR(50) NOT NULL,
	time_between_doses INTEGER NOT NULL,
	unit_between_doses VARCHAR(20)
);

CREATE TABLE medications_log (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	medication INTEGER NOT NULL,
	taken_date TIMESTAMP NOT NULL,
	FOREIGN KEY (medication) REFERENCES medications (id)
);



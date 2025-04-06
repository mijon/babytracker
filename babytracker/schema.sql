DROP TABLE IF EXISTS feeds;
DROP TABLE IF EXISTS sleeps;
DROP TABLE IF EXISTS changes;

DROP TABLE IF EXISTS medications;
DROP TABLE IF EXISTS medications_log;

DROP TABLE IF EXISTS settings;

CREATE TABLE feeds (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	start_time TIMESTAMP NOT NULL,
	stop_time TIMESTAMP NOT NULL,
	breast VARCHAR(5) NOT NULL,
	duration INTEGER NOT NULL,
	notes TEXT
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

CREATE TABLE changes (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	change_type VARCHAR(10) NOT NULL,
	change_time TIMESTAMP NOT NULL
);

CREATE TABLE settings (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	setting_name VARCHAR(50) NOT NULL,
	setting_value VARCHAR(100) NOT NULL,
	setting_type VARCHAR(50) NOT NULL
);


-- Standard Settings
INSERT INTO settings (setting_name, setting_value, setting_type) VALUES ('timezone', 'UTC', 'string');

CREATE UNIQUE INDEX index_setting_name ON settings (setting_name);

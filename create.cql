CREATE KEYSPACE IF NOT EXISTS organizationsOfEvents 
WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 2};

CREATE TYPE IF NOT EXISTS organizationsOfEvents.mentor (
 name text,
 surname text,
 birthday timestamp
);
create table if not exists organizationsOfEvents.user(
	userId int,
	name text,
	surName text,
	birthday timestamp,
	userContacts tuple<set<text>,map<text,text>>,
	countOfEvent int,
	event set<int>,
	PRIMARY KEY(userId)
);

create table if not exists organizationsOfEvents.event(
	eventId int,
	name text,
	category text,
	date timestamp,
	city text,
	adress text,
	price text,
	userId int,
	PRIMARY KEY(eventId,date)
);

create table if not exists organizationsOfEvents.planOfEvent(
	eventId int,
	hashtag text,
	fullname text,
	name text STATIC,
	category text STATIC,
	date timestamp static,
	description text,
	newSkill text,
	company text,
	mentor frozen<mentor>,
	PRIMARY KEY(eventId,fullname)
);

create table if not exists organizationsOfEvents.bonus(
	name text,
	value text,
	eventId int,
	PRIMARY KEY(eventId)
);
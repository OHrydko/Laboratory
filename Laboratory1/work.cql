
//3.1
insert into organizationsOfEvents.user(userId,name,surName,birthday,userContacts,countOfEvent,event) 
values(1,'Sasha','Hrydko','1999-06-23',(
	{'example@gmail.com'},
	{'home':'0633165695','work':'15315351531'}
	),
	1,{1});
	
insert into organizationsOfEvents.user(userId,name,surName,birthday,userContacts,countOfEvent,event) 
values(2,'Dima','Hsdf','1999-06-24',(
	{'adsasd@gmail.com'},
	{'home':'4165465465','work':'15315351531'}
	),
	1,{2});
	
insert into organizationsOfEvents.user(userId,name,surName,birthday,userContacts,countOfEvent,event) 
values(3,'Bob','Hrydko','1999-06-25',(
	{'example@gmail.com'},
	{'home':'6546','work':'15315351531'}
	),
	1,{1});
select * from organizationsOfEvents.user;


insert into organizationsOfEvents.event(eventId,name,category,date ,city,adress,price,userId) 
values(1,'android and network','android','2019-06-23','Kyiv','kovalskoho,5','free',1);

insert into organizationsOfEvents.event(eventId,name,category,date ,city,adress,price,userId) 
values(2,'android and reactive programming','android','2019-06-27','Kyiv','kovalskoho,5','free',1);

insert into organizationsOfEvents.event(eventId,name,category,date ,city,adress,price,userId) 
values(3,'ai','ai','2019-08-23','Kyiv','kovalskoho,5','free',1);

select * from organizationsOfEvents.event;

insert into organizationsOfEvents.planOfEvent(eventId,hashtag,fullname,name,
	category,date,description,newSkill,company,mentor
) 
values(1,'android','android and networking with retrofit','android and network','android',
'2019-06-23','very interesting','retrofit ','google',{name:'Sasha',surname:'asdf',birthday:'2019-06-23'});

insert into organizationsOfEvents.planOfEvent(eventId,hashtag,fullname,name,
	category,date,description,newSkill,company,mentor
) 
values(2,'android','android and networking with rxjava','android and reactive programming','android',
'2019-06-23','very interesting','rxJava','google',{name:'Sasha',surname:'asdf',birthday:'2019-06-23'});

insert into organizationsOfEvents.planOfEvent(eventId,hashtag,fullname,name,
	category,date,description,newSkill,company,mentor
) 
values(3,'ai','ai','ai','ai',
'2019-06-23','very interesting','retrofit and rxJava','google',{name:'Sasha',surname:'asdf',birthday:'2019-06-23'});

select * from organizationsOfEvents.planOfEvent;


insert into organizationsOfEvents.bonus(name,value,eventId) 
values('money','45',1);

insert into organizationsOfEvents.bonus(name,value,eventId) 
values('money','48',2);

insert into organizationsOfEvents.bonus(name,value,eventId) 
values('money','123',3);
select * from organizationsOfEvents.bonus;
//3.2


update organizationsOfEvents.user 
set countOfEvent = 3 where userId =1 ;

select countOfEvent from organizationsOfEvents.user where userId =1 ;

update organizationsOfEvents.user 
set event = event+{2}   where userId =1 ;

select event from organizationsOfEvents.user where userId =1 ;

update organizationsOfEvents.user 
set userContacts = (
	{'update@gmail.com'},
	{'home':'234','work':'23432'}
	)
	   where userId =1 ;

select userContacts from organizationsOfEvents.user where userId =1 ;



update organizationsOfEvents.planOfEvent
set name = 'androids' where eventId = 1 ;

select name from organizationsOfEvents.planOfEvent where eventId = 1 ;

update organizationsOfEvents.planOfEvent
set mentor = {name:'Dima',surname:'Dima',birthday:'2019-06-23'}  where eventId = 1 and fullname = 'android and networking with retrofit' ;

select mentor from organizationsOfEvents.planOfEvent where eventId = 1 and fullname = 'android and networking with retrofit' ;

update organizationsOfEvents.planOfEvent
set newSkill = 'androids' where eventId = 1 and fullname = 'android and networking with retrofit' ;

select newSkill from organizationsOfEvents.planOfEvent where eventId = 1 and fullname = 'android and networking with retrofit' ;

update organizationsOfEvents.bonus 
set name = 'certificate' where eventId = 1;
select name from organizationsOfEvents.bonus where eventId = 1;

update organizationsOfEvents.bonus 
set name = 'not Money' where eventId = 2;
select name from organizationsOfEvents.bonus where eventId = 2;

update organizationsOfEvents.bonus 
set value = 'android Certificate' where eventId = 1;
select value from organizationsOfEvents.bonus where eventId = 1;

update organizationsOfEvents.event 
set name = 'android' where eventId =3 and date = '2019-08-23';

select name from organizationsOfEvents.event where eventId =3 and date = '2019-08-23';

update organizationsOfEvents.event 
set category = 'android' where eventId =3 and date = '2019-08-23';

select category from organizationsOfEvents.event where eventId =3 and date = '2019-08-23';

update organizationsOfEvents.event 
set city = 'kyiv' where eventId =3 and date = '2019-08-23';

select city from organizationsOfEvents.event where eventId =3 and date = '2019-08-23';

//3.3
create index if not exists on organizationsOfEvents.event(userId);
select * from organizationsOfEvents.event where userId = 1;
select category,company from organizationsOfEvents.planOfEvent where eventId = 1;
select hashtag,date from organizationsOfEvents.planOfEvent where eventId = 1;

select name,value from organizationsOfEvents.bonus where eventId = 1;
//3.4

delete countOfEvent from organizationsOfEvents.user where userId =1 ;
delete event from organizationsOfEvents.user where userId =1 ;
delete userContacts from organizationsOfEvents.user where userId =1 ;
delete price from organizationsOfEvents.event where eventId = 1 and date = '2019-06-23';
delete city from organizationsOfEvents.event where eventId = 1 and date = '2019-06-23';
delete adress from organizationsOfEvents.event where eventId = 1 and date = '2019-06-23';
delete description from organizationsOfEvents.planOfEvent where eventId = 1 and fullname = 'android and networking with retrofit' ;
delete newSkill from organizationsOfEvents.planOfEvent where eventId = 1 and fullname = 'android and networking with retrofit' ;
delete company from organizationsOfEvents.planOfEvent where eventId = 1 and fullname = 'android and networking with retrofit' ;
delete name from organizationsOfEvents.bonus where eventId = 1;
delete value from organizationsOfEvents.bonus where eventId = 1;
delete name from organizationsOfEvents.bonus where eventId = 2;


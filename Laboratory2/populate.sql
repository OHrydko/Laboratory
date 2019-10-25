INSERT INTO public.bonus(
	event_id, name, value)
	VALUES (1, 'sa', 'saa');
	
INSERT INTO public.bonus(
	event_id, name, value)
	VALUES (2, 'sa', 'saa');
	
INSERT INTO public.bonus(
	event_id, name, value)
	VALUES (3, 'sa', 'saa');

INSERT INTO public."user"(
	user_id, name, surname, birthday)
	VALUES (1, 'as', 'asd', '2019-12-12');
INSERT INTO public."user"(
	user_id, name, surname, birthday)
	VALUES (2, 'as', 'asd', '2019-12-12');
INSERT INTO public."user"(
	user_id, name, surname, birthday)
	VALUES (3, 'as', 'asd', '2019-12-12');

INSERT INTO public.event(
	event_id, name, user_id_fk, category, city, dates, price, hashtag, adress)
	VALUES (1, 'sda', 1, 'as', 'asd', '2019-2-2', 100, 'sa', 'asd');
	
INSERT INTO public.event(
	event_id, name, user_id_fk, category, city, dates, price, hashtag, adress)
	VALUES (2, 'sda', 1, 'as', 'asd', '2019-2-2', 100, 'sa', 'asd');
	
INSERT INTO public.event(
	event_id, name, user_id_fk, category, city, dates, price, hashtag, adress)
	VALUES (3, 'sda', 1, 'as', 'asd', '2019-2-2', 100, 'sa', 'asd');

INSERT INTO public.plan(
	event_id, "newSkill", description, company, category)
	VALUES (1, 'sad', 'asd', 'as', 'as');
	
	
INSERT INTO public.plan(
	event_id, "newSkill", description, company, category)
	VALUES (2, 'sad', 'asd', 'as', 'as');
	
INSERT INTO public.plan(
	event_id, "newSkill", description, company, category)
	VALUES (3, 'sad', 'asd', 'as', 'as');

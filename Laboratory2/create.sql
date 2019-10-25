-- Table: public."user"

-- DROP TABLE public."user";

CREATE TABLE public."user"
(
    user_id integer NOT NULL,
    name character varying(40) COLLATE pg_catalog."default",
    surname character varying(40) COLLATE pg_catalog."default",
    birthday date,
    CONSTRAINT user_pkey PRIMARY KEY (user_id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;


-- Table: public.bonus

-- DROP TABLE public.bonus;

CREATE TABLE public.bonus
(
    event_id integer NOT NULL DEFAULT nextval('bonus_event_id_seq'::regclass),
    name character varying(40) COLLATE pg_catalog."default",
    value character varying(40) COLLATE pg_catalog."default",
    CONSTRAINT bonus_pkey PRIMARY KEY (event_id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.bonus
    OWNER to postgres;


-- Table: public.event

-- DROP TABLE public.event;

CREATE TABLE public.event
(
    event_id integer NOT NULL,
    name character varying(40) COLLATE pg_catalog."default",
    user_id_fk integer,
    category character varying(40) COLLATE pg_catalog."default",
    city character varying(40) COLLATE pg_catalog."default",
    dates date,
    price integer,
    hashtag character varying(40) COLLATE pg_catalog."default",
    adress character varying(40) COLLATE pg_catalog."default",
    CONSTRAINT event_pkey PRIMARY KEY (event_id),
    CONSTRAINT event_user_id_fk_fkey FOREIGN KEY (user_id_fk)
        REFERENCES public."user" (user_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.event
    OWNER to postgres;

-- Table: public.plan

-- DROP TABLE public.plan;

CREATE TABLE public.plan
(
    event_id integer NOT NULL DEFAULT nextval('plan_event_id_seq'::regclass),
    "newSkill" character varying(40) COLLATE pg_catalog."default",
    description character varying(40) COLLATE pg_catalog."default",
    company character varying(40) COLLATE pg_catalog."default",
    category character varying(40) COLLATE pg_catalog."default",
    CONSTRAINT plan_pkey PRIMARY KEY (event_id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.plan
    OWNER to postgres;


ALTER TABLE public."user"
    OWNER to postgres;

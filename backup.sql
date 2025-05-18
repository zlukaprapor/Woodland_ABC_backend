--
-- PostgreSQL database dump
--

-- Dumped from database version 17.4
-- Dumped by pg_dump version 17.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: userrole; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.userrole AS ENUM (
    'ADMIN',
    'USER'
);


ALTER TYPE public.userrole OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: lesson; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.lesson (
    id integer NOT NULL,
    letter_upper character varying(1) NOT NULL,
    letter_lower character varying(1) NOT NULL,
    description text NOT NULL,
    training text NOT NULL,
    regulations text NOT NULL,
    letter_image character varying NOT NULL,
    object_image_first character varying NOT NULL,
    object_image_second character varying NOT NULL,
    object_image_third character varying NOT NULL,
    audio_file character varying NOT NULL,
    quiz_file character varying NOT NULL
);


ALTER TABLE public.lesson OWNER TO postgres;

--
-- Name: lesson_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.lesson_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.lesson_id_seq OWNER TO postgres;

--
-- Name: lesson_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.lesson_id_seq OWNED BY public.lesson.id;


--
-- Name: progress; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.progress (
    id integer NOT NULL,
    user_id integer NOT NULL,
    lesson_id integer NOT NULL,
    completed boolean NOT NULL
);


ALTER TABLE public.progress OWNER TO postgres;

--
-- Name: progress_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.progress_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.progress_id_seq OWNER TO postgres;

--
-- Name: progress_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.progress_id_seq OWNED BY public.progress.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id integer NOT NULL,
    email character varying NOT NULL,
    username character varying NOT NULL,
    password_hash character varying NOT NULL,
    role public.userrole,
    is_active boolean,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.users_id_seq OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: lesson id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.lesson ALTER COLUMN id SET DEFAULT nextval('public.lesson_id_seq'::regclass);


--
-- Name: progress id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.progress ALTER COLUMN id SET DEFAULT nextval('public.progress_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: lesson; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.lesson (id, letter_upper, letter_lower, description, training, regulations, letter_image, object_image_first, object_image_second, object_image_third, audio_file, quiz_file) FROM stdin;
1	А	а	Аа-а-аа-а! Говорить мама Ані\\n\r\n\\n\r\nАбетку вивчає маленька Анюта\\n	А | А | А |\\n\r\nа | а | а | а |\\n\r\nА | а | а | А | а\\n\r\n\\n\r\n|А|-|на|-|нас|\\n\r\n|А|-|пель|-|син|\\n\r\n|Ав|-|то|-|бус|\\n	🔹 Пригадайте разом із дитиною, які звуки називаються голосними. Це такі звуки, які можна співати. До голосних належать звуки, що позначаються буквами А, О, У, Е, И, І, Ї, Є, Ю, Я.\r\n🔹 Зверніть увагу малюка на те, що літера А — це голосна.\r\nПоясніть, що під час вимови звуку [а] рот розкривається дуже широко. Покажіть це разом у дзеркалі.\r\n🔹 Проспівайте з дитиною звук [а].\r\nПовторіть кілька разів, тягнучи звук: «А-а-а», звертаючи увагу, як вібрує голос, і як звучить голосно та чисто.\r\n🔹 Розкажіть, що ми вивчаємо дві літери: велику та малу А.\r\nПоясніть, що великі літери (або прописні) пишуться на початку речень, а також у іменах людей, міст, країн тощо.\r\n🔹 Запропонуйте дитині розглянути малюнки.\r\nЗапитайте:\r\n– З якої букви починається назва кожного зображеного предмета?\r\n– Скільки разів буква А зустрічається в кожному слові?\r\n📌 Наприклад:\r\nАнанас — 3 букви А\r\nАпельсин — 1 буква А\r\nАвтобус — 1 буква А\r\n🔹 Разом розбийте слова на склади:\r\n– А-на-нас\r\n– А-пель-син\r\n– Ав-то-бус\r\n🔹 Дотримуйтеся цієї схеми в роботі з іншими літерами.\r\nСпочатку знайомтесь зі звуком, показуйте букви (велику й малу), співайте, шукайте її в словах, розбивайте слова на склади.\r\n🔹 Навчайте дитину читати букви по рядку.\r\nПокажіть, як вести пальцем або олівцем зліва направо, промовляючи кожну букву вголос.\r\nПоясніть, що саме так ми читаємо й пишемо — зліва направо.	letters/А\\f1df75c0-6df3-4840-8aca-2c301817d162.png	objects/А\\080e36fa-d65c-4a57-ae84-060906a19723.png	objects/А\\a774de3b-c786-439a-953f-274a4c40b1dc.png	objects/А\\095f097f-aeef-45c8-93d6-13b91b6492d4.png	audio/А\\dbdb99a2-cf64-42dd-82d3-f4403b5826b8.mp3	quiz/А\\229aaa32-2c31-48fa-a38b-ab5f8fdb6e69.json
2	У	у	Удав сумує дуже -\\n\r\nз ним ніхто не дружить\\n\r\n\\n\r\nУсмішка вранці у вікно загляда,\\n\r\nУсіх навколо теплом обійма!\\n	У | У | У |\\n\r\nу | у | у | у |\\n\r\nУ | у | у | У | а\\n\r\n\\n\r\n|У|-|дав|\\n\r\n|Ру|-|ка|\\n\r\n|Ву|-|хо|-\\n	🔹 Розкажіть дитині, що звук У — це голосний звук, як і звук А. Поясніть, що голосні звуки можна співати.\r\n\r\n🔹 Зверніть увагу на те, як ми складаємо губи, коли вимовляємо звук У. Порівняйте це з артикуляцією звуку А: при звуці У губи округлені, а при звуці А — широко відкриті.\r\n\r\n🔹 Покажіть це разом у дзеркалі, щоб дитина побачила, як змінюється форма рота.\r\n\r\n🔹 Запитайте дитину, що зображено на малюнках, які ви їй покажете.\r\n\r\n🔹 Обговоріть, де стоїть звук У в цих назвах: на початку, в середині чи в кінці слова.\r\n\r\n🔹 Запитайте, чи є у назвах інші знайомі дитині букви.\r\n\r\n🔹 Разом розбийте слова на склади і визначте наголошені звуки.\r\n\r\n🔹 Знайдіть знайомі букви в словах і поясніть, що так працювати з іншими словами та літерами.\r\n\r\n🔹 Навчайте дитину читати букви, водячи вказівний палець зліва направо та по стовпчиках згори вниз.\r\n\r\n🔹 Наприкінці заняття прочитайте малюкові додаткові матеріали (вірші, казки, загадки), акцентуючи увагу на літері, яку вивчаєте.	letters/У\\841f2ff1-9db5-407d-8edf-59d92bc585f0.png	objects/У\\77180381-f3f0-4477-903e-e2a6162eb614.png	objects/У\\89710c93-59af-4107-86be-cda8bb5000a1.png	objects/У\\0423b6cd-ccfd-4f34-b3e1-8a9697243333.png	audio/У\\771ddd51-8623-4e67-8c21-81b8bdad3531.mp3	quiz/У\\5e665d78-d641-46d5-b37e-7371c437e138.json
3	О	о	Осляті цукру дам з руки:\\n \r\nХочуть покататись малюки\\n\r\n\\n\r\nОгірочок в огороді —\\n\r\nСонце світить на природі.\\n	А | о | О | у | А | У |\\n\r\nа | о | У | а | О | у |\\n\r\n\\n\r\nА_____________________О\\n\r\nУ_____________________А\\n\r\nА_____________________У\\n\r\n\\n\r\n|О|-|са|\\n\r\n|О|-|ко|\\n\r\n|О|-|гі|-|рок|\\n	🔹 Розкажіть дитині, що звук O — це голосний звук, як і звук А та У. \r\n🔹 Зверніть увагу на те, як ми складаємо губи, коли вимовляємо звук О. Порівняйте це з артикуляцією попередніх букв: при звуці У губи округлені, а при звуці А — широко відкриті.\r\n🔹 Покажіть це разом у дзеркалі, щоб дитина побачила, як змінюється форма рота.\r\n🔹 Запитайте дитину, що зображено на малюнках, які ви їй покажете.\r\n🔹 Обговоріть, де стоїть звук О в цих назвах: на початку, в середині чи в кінці слова.\r\n🔹 Запитайте, чи є у назвах інші знайомі дитині букви.\r\n🔹 Разом розбийте слова на склади і визначте наголошені звуки.\r\n🔹 Знайдіть знайомі букви в словах і поясніть, що так працювати з іншими словами та літерами.\r\n🔹 Починайте навчати малюка читати буквенні сполучення, уникаючи читання по одній букві. Показавши пальцем на першу букву, слід почати "Тягнути" перший звук голосом,\r\nведучи при цьому палець управо, аж поки не дістанетесь до другої букви, а тоді відразу вимовляти другий звук. Сполучення букв мають читатися разом!!!	letters/О\\1f42b7ef-2da0-473c-a9b7-02a0157a5936.png	objects/О\\644f36d5-565d-455f-8686-f04b63e31331.png	objects/О\\7b015714-4cc9-44aa-84fe-c1a731e21df5.png	objects/О\\078804a8-1f14-4859-9d74-5310d8686b1b.png	audio/О\\8a4fd8a7-3da4-4b5a-9228-507b95d7c05f.mp3	quiz/О\\dde327cc-eb8b-43f9-a6b2-26498b4dd3a9.json
\.


--
-- Data for Name: progress; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.progress (id, user_id, lesson_id, completed) FROM stdin;
1	2	1	t
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (id, email, username, password_hash, role, is_active, created_at) FROM stdin;
1	testadmin1@example.com	testadmin1	$pbkdf2-sha256$29000$a00phVBqzfmfM2aMUQoB4A$NFCci7o8xmdKtejSA8Mzpsq/RMEzQtnzLswSOvxeBQw	ADMIN	t	2025-04-20 11:26:55.252025
2	testuser1@example.com	testuser1	$pbkdf2-sha256$29000$Xuvdm3Pufa/VGuMcQwiBMA$NoYXLZ9hi3l0ao7v4cNPfPSAobxrBIf0fz6I.bavIBw	USER	t	2025-04-20 11:27:52.682376
\.


--
-- Name: lesson_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.lesson_id_seq', 3, true);


--
-- Name: progress_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.progress_id_seq', 1, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_id_seq', 2, true);


--
-- Name: lesson lesson_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.lesson
    ADD CONSTRAINT lesson_pkey PRIMARY KEY (id);


--
-- Name: progress progress_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.progress
    ADD CONSTRAINT progress_pkey PRIMARY KEY (id);


--
-- Name: lesson unique_letter_upper; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.lesson
    ADD CONSTRAINT unique_letter_upper UNIQUE (letter_upper);


--
-- Name: progress unique_user_lesson; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.progress
    ADD CONSTRAINT unique_user_lesson UNIQUE (user_id, lesson_id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: ix_lesson_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_lesson_id ON public.lesson USING btree (id);


--
-- Name: ix_lesson_letter_upper; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX ix_lesson_letter_upper ON public.lesson USING btree (letter_upper);


--
-- Name: ix_progress_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_progress_id ON public.progress USING btree (id);


--
-- Name: ix_users_email; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX ix_users_email ON public.users USING btree (email);


--
-- Name: ix_users_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_users_id ON public.users USING btree (id);


--
-- Name: ix_users_username; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX ix_users_username ON public.users USING btree (username);


--
-- Name: progress progress_lesson_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.progress
    ADD CONSTRAINT progress_lesson_id_fkey FOREIGN KEY (lesson_id) REFERENCES public.lesson(id);


--
-- Name: progress progress_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.progress
    ADD CONSTRAINT progress_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- PostgreSQL database dump complete
--


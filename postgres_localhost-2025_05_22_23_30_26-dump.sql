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
4	М	м	Мама мила миску милом —\\n\r\nМурчик з неї воду пив.\\n\r\n\\n\r\nМишка мчить між маків красних,\\n\r\nМріє про пиріг із маслом. \\n	А______________М (ам) <-----  це закритий склад\\n\r\nУ______________М (ом)\\n\r\nО______________М (ом)\\n\r\n\\n\r\nМ+У=МУ <-----  це відкритий склад\\n\r\n\\n\r\n|Ма|-|к|\\n\r\n|Ми|-|ша|\\n\r\n|Ма|-|ши|-|на|-\\n	🔹 Зверніть увагу дитини на те що буква М належить до приголосних звуків. Пригадайте, що ви знаєте про ці звуки. Чим вони відрізняються від голосних?\r\n\r\n🔹 Закриті склади(перший звук голосний, другий - приголосний) треба читати за схемою, засвоєною на попередньому занятті: дитина тягне перший звук, пересуваючи палець доріжкою, і відразу називає другий. \r\n\r\n🔹 Уникайте побуквеного читання складів.\r\n\r\n🔹 Будьте дуже уважні, переходячи до читання відкритих складів (перший звук приголосний, другий - голосний)\r\n\r\n🔹 Неправильно говорити: "[м] і [у]-разом [му]". Треба казати:"[м],[у]-[му]".\r\nСлід уникати поширеної помилки, пов'язаної з роздільною вимовою звуків у складі. Поясніть малюкові, що в таких випадках спочатку вимовляється приголосний звук, а потім рот відразу розкривається для вимови голосного.	letters/М\\61418d12-de80-462d-91a0-0b7a24d2b4c6.png	objects/М\\b6116e65-9e5b-4ca0-9e38-467333069a4d.png	objects/М\\25f92841-fe3c-4155-9baf-ba6b78805438.png	objects/М\\c6986475-1a1e-4f3f-b441-244ddd69a94c.png	audio/М\\611f4844-17ee-453e-82c3-daa7fc486044.mp3	quiz/М\\976d3356-d592-453a-ac2a-d1b991d6e944.json
6	И	и	Зайчик стрибав через тин —\r\nВчився вимовляти "и".\r\n\\n\r\nВиніс їжачок з комори\r\nГруші, сливи й помідори. 	    - | и\\n\r\nн |  - | а\\n\r\n     - | у\\n\r\n\\n\r\n     - | и\\n\r\nм |  - | а\\n\r\n     - | о\\n\r\n\\n\r\nам | ан | ма | на |\\n\r\nум | ун | му | ну |\\n\r\nим | ин | ми | ни |\\n\r\n\\n\r\n|Сир|\\n\r\n|Ми|-|ло|\\n\r\n|Руш|-|ник|\\n\r\n\\n\r\nУ ма-ми ми.\r\n	🔹 Пригадай що буква И належить до голосних.\r\n🔹 Зверніть увагу дитини на те, що велика буква «и» у нашій мові вживається дуже рідко. Це тому, що велика буква завжди стоїть на початку слів, а в нашій мові доволі мало слів, які починаються на цю букву.  \r\n🔹  Багаторазове уважне читання однотипних складів у рядок та стовпчик запобіжить виникненню у дитини звички читати за здогадкою.\r\n🔹  Доцільно пропонувати малюкові для читання спочатку прості вправи, потім складніші.\r\nНаприклад: спочатку закриті склади, потім відкриті, потім слова, потім речення. 	letters/И\\8477078b-d647-4552-b0d5-fe5254d43702.png	objects/И\\7d12357c-5b05-497c-a9d4-9c49cbefbb81.png	objects/И\\2a5219c0-ae71-404e-962e-0462629c3741.png	objects/И\\8cd18d51-4385-450f-91d4-904c8fd1f2d8.png	audio/И\\9be4d15d-5d58-4f60-a086-40b4bf306221.mp3	quiz/И\\54ce151e-a7d1-4814-8ca1-fcce0d6e529f.json
7	І	і	Іринка малює зірки —\r\nІскряться в небі казки.\r\n\\n\r\nІндик ходить по дворі,\r\nІ шукає щось в траві.	им--ім--ин--ін--ан--ун\\n\r\n\\n\r\nми | му | ни | ні |\\n\r\n\\n\r\nмо--му  | ни--ні\\n\r\nно--ну  | ми--мі\\n\r\nна--ни  | на--ми\\n\r\nма--ми  | ни--ми\\n\r\nма--мі\\n\r\n|Ін|-|дик|\\n\r\n|Лі|-|ки|\\n\r\n|Хліб|\\n\r\n\\n\r\nОн ма-ма і Ні-на. У ма-ми 🍎🍏\r\nНа, Ні-но, 🍎🍏\r\n	🔹 Молодчинка!\r\nТи так гарно стараєшся і не зупиняєшся!\r\nЯ дуже пишаюся тобою — ти вчишся щодня, крок за кроком.\r\nНавіть коли щось складне — ти не здаєшся, а пробуєш знову.\r\nПродовжуй у тому ж дусі — твоя наполегливість обов’язково принесе великі результати!  \r\n🔹 Пригадай що буква І належить до голосних\r\n🔹  Багаторазове уважне читання однотипних складів у рядок та стовпчик запобіжить виникненню у дитини звички читати за здогадкою.\r\n🔹  Доцільно пропонувати малюкові для читання спочатку прості вправи, потім складніші.\r\nНаприклад: спочатку закриті склади, потім відкриті, потім слова, потім речення. 	letters/І\\ee6ac172-6f88-4b35-9712-a401b196d1e8.png	objects/І\\279e245e-c84f-4833-ad31-1b516bf6c728.png	objects/І\\3fe064dc-8c1e-441d-8409-c792ec76ced6.png	objects/І\\572d8774-de2d-41f1-8f79-4dc8f44cb64e.png	audio/І\\aa567db6-868e-4cf7-ac27-d8e3b9233559.mp3	quiz/І\\1844f856-74b8-4c54-869f-33b3ad73776d.json
5	Н	н	На пеньочку їжачок\\n\r\nНіс на спинці пиріжок.\\n	А_____________________Н   ан\\n\r\nО_____________________Н   он\\n\r\nУ_____________________Н   ун\\n\r\n\\n\r\nН+А=НА <-----  це відкритий склад\\n\r\n\\n\r\nан | ам | ом | ун | он \\n\r\nна | ма | мо | ну | но \\n\r\n\\n\r\n|Ніж|\\n\r\n|Нит|-|ка|\\n\r\n|Но|-|жи|-|ці|-\\n\r\n\\n\r\nНа мамо ці, 🌼🌸🌷.	🔹 Продовжуйте читати закриті та відкриті склади, звертаючи увагу дитини на особливості їх прочитання: у закритих складах перший звук тягнеться (співається), а потім без паузи вимовляється другий -- приголосний звук. У відкритих складах спочатку вимовляється перший, приголосний звук, а потім рот одразу розкривається для вимови голосного звука. Стежте, щоб не припуститися побуквеного прочитання складів.  \r\n🔹  Аналізуйте з малюком прочитані склади. Скільки букв у складі? Яка буква перша? Який звук вона позначає: голосний чи приголосний? Яка буква друга? Який звук вона позначає? \r\n🔹  Прочитайте з дитиною речення. Не забудьте відзначити це досягнення. Зверніть увагу дитини на те, що речення починається з великої літери і закінчується крапкою. Із самого початку привчайте мао люка виділяти інтонацією кінець речення. 	letters/Н\\125268b8-0c6a-4e24-b439-b8c94f49415c.png	objects/Н\\fb633ef2-4a78-4899-8c30-ea9513287464.png	objects/Н\\8ddcbc4b-b6ac-4c2b-a2e9-db266288ad23.png	objects/Н\\c5b5cfd2-193d-4c37-9be3-26eae580fa5e.png	audio/Н\\2055ef41-d5c3-4546-a34b-955e8baf77ec.mp3	quiz/Н\\8bb8307a-7135-4b06-a96d-1d248a96d44f.json
8	С	с	Сонце світить з висоти,\\n\r\nСяють срібні кольори.\\n\r\nСоловейко в садку співає,\\n\r\nСон про літо навіває.\\n	ми\\n\r\nна|с\\n\r\nна|м\\n\r\nу на|с\\n\r\n\\n\r\nС----О-----М\\n\r\nС----У-----М\\n\r\nС----А-----М\\n\r\nС----І-----М\\n\r\n\\n\r\nси|н   со|м   со|с-на\\n\r\nси|ни   со|ми   на-со|с\\n\r\n\\n\r\n|Сом|\\n\r\n|Слон|\\n\r\n|Сон|-|це|-\\n\r\n\\n\r\nУ ма-ми син.\\n\r\nУ си-на сом.\\n\r\n-На, мо-мо, со-ма.\\n\r\n	🔹 Склади з трьох букв ми будемо розбивати для зручності читання вертикальною лінією. Так, наприклад, у слові «нас» дитина має спочатку разом прочитати «на», в а потім додати звук [с]\r\n🔹  Важливо, щоб малюк, читаючи речення, розумів зміст прочитаного. \r\n🔹 Прочитавши перше слово речення, нехай дитина промовить його ще раз, а потім відразу читає друге. Після цього попросіть її сказати перші два слова і прочитати третє. Прагніть, щоб дитина могла переказати зміст оповідання.\r\n\r\n	letters/С\\12f278c1-b0f4-4b95-bf52-ebd9b958e428.png	objects/С\\8089d8b7-9227-43db-a388-f55f0187043b.png	objects/С\\1661c912-ccdf-41bd-8abf-d224a9fe65d6.png	objects/С\\02bcfa96-dfe2-4149-a55b-65c82b8a7a3f.png	audio/С\\6ccfdc2f-4c86-4e61-8d44-dc0243465eb4.mp3	quiz/С\\2df897ec-9686-4c7e-82fa-855142fc8e71.json
9	Л	л	Лисеня в лісочку гралось,\\n\r\nЛистячком пухким ховалось.\\n\r\nЛуг зелений, квітів море —\\n\r\nЛіто кличе всіх надворі!\\n	ми-ло\\n\r\nма|с-ло\\n\r\nс|мо-ла\\n\r\n\\n\r\nлі|с\\n\r\nли|с\\n\r\nми-ло\\n\r\nло-ми\\n\r\nли-мо-ни\\n\r\n\\n\r\n|Ли|-|мон|\\n\r\n|Лі|-|так|\\n\r\n|Ли|-|си|-|ця|-\\n\r\n\\n\r\nМа-ма ми-ла Ліну.\\n\r\nУ ма-ми ми-ло.\\n\r\n	🔹 Зверніть увагу дитини на те, як змінюються слова із заміною однієї букви або переставлянні складів.\r\n🔹 Під час читання стежте, щоб малюк називав не алфавітну назву букви, а звук, який вона позначає. Неправильно: (ел) або (ле). Правильно: (л). \r\n🔹 Пам'ятайте також про правила читання складів. Неправильно, коли дитина каже: «(м) і (и) - разом (ми)». Правильно: «(м) (и) - (ми)».\r\n🔹Тут і надалі візьміть За правило ставити дитині запитання щодо змісту та структури оповідань. Наприклад: Кого мила мама? Хто мив Ліну? Чим мама мила дівчинку? Скільки речень в оповіданні?\r\nПокажи, де починаються речення (великі літери) та де вони закінчуються (крапки). Скільки в оповіданні великих літер? Що вони позначають? Які слова позначають назви предметів, а які -- дії?\r\nЧи є в оповіданні слова, які позначали б ознаки предметів?	letters/Л\\bb668e7b-dbcb-47ef-9e02-a2e5479bf068.png	objects/Л\\31ee5f36-efd4-4957-8203-d8f72a3f17d3.png	objects/Л\\e93290c5-dab4-46dd-8651-324d31175ee5.png	objects/Л\\c6ec7ec4-8299-4afd-bce5-be656456332e.png	audio/Л\\ff35704c-38e0-44f0-ac3c-2a5e3e9c387d.mp3	quiz/Л\\7433cf7e-32d3-4f9f-a746-30403616406a.json
10	К	к	Казку котик розповів,\\n\r\nКапелюх приміряв, свій.\\n\r\nКольорові сни кружляють —\\n\r\nКазкові сни діток втішають.\\n	ми|му|мо|ми\\n\r\nка|ку|ко|ки\\n\r\n\\n\r\nко-ло\\n\r\nко-ло|с\\n\r\n\\n\r\nс|ла   с|ма\\n\r\nс|лу   с|му\\n\r\nма|к   о-са\\n\r\nс|ма|к   ко-са\\n\r\n\\n\r\nОк-са-на\\n\r\nМи-ко-ла\\n\r\nка-ли-на\\n\r\nма-ли-на\\n\r\n\\n\r\n|Кур|-|ка|\\n\r\n|Ко|-|ро|-|ва|\\n\r\n|Лкиж|-|ка|-\\n\r\n\\n\r\nМа-ма ми-ла Ліну.\\n\r\nУ ма-ми ми-ло.\\n	🔹 Разом із дитиною продовжуйте тренуватися у визначенні місця звука і букви, що вивчаються, у словах та складах.\r\n🔹 Якщо читання деяких слів або складів дається малюкові важко, не акцентуйте на цьому увагу. Поверніться до цих вправ пізніше.\r\n🔹 Не забувайте про принцип поступового ускладнення: спочатку склади, потім слова, потім речення або тексти.\r\n🔹 Опитуйте дитину після кожного прочитаного тексту за схемою, наведеною в уроці на букву (Л).	letters/К\\b433749c-ee05-4691-87a9-61b91c9a589f.png	objects/К\\8813b774-31c0-416c-b9ca-f0e235f47093.png	objects/К\\f33b6101-2c18-4fce-b197-b411696dbb4a.png	objects/К\\d3551b4f-9540-41c8-a509-72217d2434f5.png	audio/К\\88e1034e-d650-4264-8bb8-7d8acf4b0d9e.mp3	quiz/К\\c8debb67-2cac-4134-920c-d91a97798f1e.json
11	В	в	Ведмедик в лісі мед шукав,\\n\r\nВеселу пісеньку співав.\\n\r\nВухатий зайчик вибіг враз —\\n\r\nВітатися прийшов якраз!\\n	ну|ва|но|ми|мі\\n\r\nму|ма|во|ни|ні\\n\r\nву|на|мо|ви|ві\\n\r\n\\n\r\nві|к\\n\r\nві|к-но\\n\r\nві-но|к\\n\r\n\\n\r\nві|н  во-но\\n\r\nво-на  во-ни\\n\r\n\\n\r\nна-ли|в\\n\r\nви-ли|в\\n\r\n\\n\r\n|Ві|-|нок|\\n\r\n|Вовк|\\n\r\n|Виш|-|ні|-\\n\r\n\\n\r\nУ Олі ві-но|к.\\n\r\nУ ві|н-ку к|ві-ти.\\n	🔹 Починаючи з цієї сторінки, ми пропонуємо дитині нову вправу: читання слів з однією незнайомою буквою. Це завдання не викличе у дитини утруднень, якщо ви допоможете їй знайти зв'язок між оповіданням та малюнком.\r\n🔹 Не забувайте дотримуватися принципу поступового ускладнення вправ під час заняття. Опитуйте дитину щодо змісту та структури оповідань за схемою, поданою на уроці з буквою [Л]	letters/В\\3d732f69-99fe-465e-9f6f-4a743252904d.png	objects/В\\49cd9eca-7426-4612-8650-74740e231d21.png	objects/В\\5a930816-57bd-497d-a8b2-bc58db134ccf.png	objects/В\\58712a7d-5089-42bb-8700-be2ba0b85d75.png	audio/В\\21329473-9fa0-42b6-bd01-655c9024ea57.mp3	quiz/В\\0e6fe029-326f-478a-a82c-32f787e94937.json
12	Е	е	Екскаватор землю риє-\\n\r\nпрацювати добре вміє\\n\r\n	ло|с  с|ло\\n\r\nла|с  с|ла\\n\r\nле|с  с|ле\\n\r\nлі|с  с|лі\\n\r\nли|с  с|ли\\n\r\n\\n\r\nса-ло\\n\r\nсе-ло\\n\r\nси-ла\\n\r\nве-се-ло\\n\r\nве-се|л-ка\\n\r\n\\n\r\nСе-ме|н  О-ле-на\\n\r\nко-ле-со  ле-ле-ка\\n\r\n\\n\r\n|Сер|-|це|\\n\r\n|Ве|-|сел|-|ка|\\n\r\n|Ес|-|кі|-|мо|-\\n\r\n\\n\r\nВе|с-на\\n\r\nУ се-лі ве|с-на.\\n\r\nНа к|ле-ні ле-ле-ка.\\n\r\nСе-ме|н не-се 🌳.\\n\r\nУ Ле-сі 🚿.\\n	🔹 Обов'язково пояснюйте малюкові незнайомі слова.\r\n🔹 Не забувайте звертати увагу дитини на те, що імена починаються з великих літер. Великі літери також стоять на початку речення, а кінець речення позначається крапкою.\r\n🔹 Пам'ятайте, що зовсім не обов'язково прочитувати весь матеріал цього уроку за одне заняття. 	letters/Е\\1aa6221e-21d9-4e51-a8f2-0735075e3206.png	objects/Е\\9e14b122-6ff5-400e-a7d7-4a37c089c09c.png	objects/Е\\b55cba45-089b-45e0-a306-e32da71c8065.png	objects/Е\\8a78248b-4ad3-4378-a2e3-de294a952ed7.png	audio/Е\\884c78ee-ae00-4f7f-a448-21ba193f53af.mp3	quiz/Е\\5802565c-0911-4112-a26a-0f56f2f827d2.json
13	Р	р	Равлик рано вийшов на прогулянку,\\n\r\nПоглянув навколо — світ яскравий,\\n\r\nРадіє сонцю, птахам і квітам,\\n\r\nДень починається з новими мріями.\\n	ра|н  ро|м  рі|к\\n\r\nре|в  ру|м  ри|к\\n\r\n\\n\r\nси|р  ко-ра  ру-ка ра-но\\n\r\nри|с  но-ра  рі-ка ра-но|к\\n\r\n\\n\r\nко-ро-ва  во-ро-на\\n\r\n\\n\r\nр-у-ка  р-і-ка\\n\r\n\\n\r\nко-ра  по-ра  но-ра\\n\r\n\\n\r\n|Ри|-|ба|\\n\r\n|Рав|-|лик|\\n\r\n|Ра|-|ке|-|та|-\\n\r\n\\n\r\nРо-мі сі|м ро-кі|в.\\n\r\nА Ма-ри-ні ві-сі|м.\\n\r\nРо-ма ми|в ру-ки.\\n\r\nМа-ри-на ва-ри-ла сі|п.\\n\r\n	🔹 Пам'ятайте про порядок читання вправ: спочатку склади, потім слова, потім тексти.\r\n🔹 Не забувайте стежити за тим, щоб дитина виділяла інтонацією кінець речення. Опитуйте малюка щодо змісту та структури тексту за схемою, наведеною в уроці букви [Л] 	letters/Р\\70306964-d28f-4d8d-a4c8-7bd3325c8846.png	objects/Р\\0b914ccf-5a43-4ada-94f5-109ea342d58a.png	objects/Р\\24b0c343-1028-4640-aacf-fad85efb549b.png	objects/Р\\22cf195e-d2ec-4c74-87c9-d302fc739676.png	audio/Р\\573e9152-39ce-49c3-941a-dcb7ea11febc.mp3	quiz/Р\\1b1dae3b-87e3-480c-a326-d421d131f984.json
\.


--
-- Data for Name: progress; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.progress (id, user_id, lesson_id, completed) FROM stdin;
1	2	1	t
2	2	2	t
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

SELECT pg_catalog.setval('public.lesson_id_seq', 13, true);


--
-- Name: progress_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.progress_id_seq', 2, true);


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


# polls

```shell
python manage.py makemigrations polls

# output
Migrations for 'polls':
  polls/migrations/0001_initial.py
    - Create model Question
    - Create model Choice
```

## 내부적 sql execution

호출 구문 확인

```shell
python manage.py sqlmigrate polls 0001

# output
BEGIN;
--
-- Create model Question
--
CREATE TABLE "polls_question" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "question_text" varchar(200) NOT NULL, "pub_date" datetime NOT NULL);
--
-- Create model Choice
--
CREATE TABLE "polls_choice" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "choice_text" varchar(200) NOT NULL, "votes" integer NOT NULL, "question_id" bigint NOT NULL REFERENCES "polls_question" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "polls_choice_question_id_c5b4b260" ON "polls_choice" ("question_id");
COMMIT;
```

### check issue

```shell
python manage.py check

# if no issue
System check identified no issues (0 silenced).
```

## make migrate

```shell
python manage.py migrate
```

## enter the interactive shell

use Django API

```shell
python manage.py shell
```

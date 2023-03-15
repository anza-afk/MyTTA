CREATE TABLE "public.users" (
	"id" serial NOT NULL,
	"email" varchar(255) NOT NULL UNIQUE,
	"password" varchar(255) NOT NULL,
	"is_active" bool NOT NULL,
	"is_superuser" bool NOT NULL,
	CONSTRAINT "users_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.profiles" (
	"id" serial NOT NULL,
	"name" varchar(255) NOT NULL,
	"surname" varchar(255) NOT NULL,
	"patronymic" varchar(255) NOT NULL,
	"user_id" int NOT NULL,
	"job_id" int NOT NULL,
	"department_id" int NOT NULL,
	CONSTRAINT "profiles_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.jobs" (
	"id" serial NOT NULL,
	"name" varchar(255) NOT NULL,
	CONSTRAINT "jobs_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.departments" (
	"id" serial NOT NULL,
	"name" varchar(255) NOT NULL,
	"address" varchar(255) NOT NULL,
	CONSTRAINT "departments_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.jobs_departments" (
	"id" serial NOT NULL,
	"jobs_id" int NOT NULL,
	"department_id" int NOT NULL,
	CONSTRAINT "jobs_departments_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.tickets" (
	"id" serial NOT NULL,
	"title" varchar(50) NOT NULL,
	"text" varchar(1000) NOT NULL,
	"owner_id" int NOT NULL,
	"img" varchar(255) NOT NULL,
	CONSTRAINT "tickets_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.superuser_ticket" (
	"id" serial NOT NULL,
	"superuser_id" int NOT NULL,
	"ticket_id" int NOT NULL,
	CONSTRAINT "superuser_ticket_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.superusers" (
	"id" serial NOT NULL,
	"user_id" int NOT NULL,
	CONSTRAINT "superusers_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "public.comments" (
	"id" serial NOT NULL,
	"text" varchar(255) NOT NULL,
	"img" varchar(255) NOT NULL,
	"user_id" int NOT NULL,
	"ticket_id" int NOT NULL,
	"parent_id" int NOT NULL,
	CONSTRAINT "comments_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);




ALTER TABLE "profiles" ADD CONSTRAINT "profiles_fk0" FOREIGN KEY ("user_id") REFERENCES "users"("id");
ALTER TABLE "profiles" ADD CONSTRAINT "profiles_fk1" FOREIGN KEY ("job_id") REFERENCES "jobs"("id");
ALTER TABLE "profiles" ADD CONSTRAINT "profiles_fk2" FOREIGN KEY ("department_id") REFERENCES "departments"("id");



ALTER TABLE "jobs_departments" ADD CONSTRAINT "jobs_departments_fk0" FOREIGN KEY ("jobs_id") REFERENCES "jobs"("id");
ALTER TABLE "jobs_departments" ADD CONSTRAINT "jobs_departments_fk1" FOREIGN KEY ("department_id") REFERENCES "departments"("id");

ALTER TABLE "tickets" ADD CONSTRAINT "tickets_fk0" FOREIGN KEY ("owner_id") REFERENCES "users"("id");

ALTER TABLE "superuser_ticket" ADD CONSTRAINT "superuser_ticket_fk0" FOREIGN KEY ("superuser_id") REFERENCES "superusers"("id");
ALTER TABLE "superuser_ticket" ADD CONSTRAINT "superuser_ticket_fk1" FOREIGN KEY ("ticket_id") REFERENCES "tickets"("id");

ALTER TABLE "superusers" ADD CONSTRAINT "superusers_fk0" FOREIGN KEY ("user_id") REFERENCES "users"("id");

ALTER TABLE "comments" ADD CONSTRAINT "comments_fk0" FOREIGN KEY ("user_id") REFERENCES "users"("id");
ALTER TABLE "comments" ADD CONSTRAINT "comments_fk1" FOREIGN KEY ("ticket_id") REFERENCES "tickets"("id");
ALTER TABLE "comments" ADD CONSTRAINT "comments_fk2" FOREIGN KEY ("parent_id") REFERENCES "comments"("id");











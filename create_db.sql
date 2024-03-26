CREATE TABLE "episodes" (
  "id" integer PRIMARY KEY,
  "title" varchar,
  "air_date" varchar,
  "month" varchar,
  "colors" varchar,
  "subjects" varchar
);

CREATE TABLE "months" (
  "id" integer PRIMARY KEY,
  "name" varchar,
  "episodes" varchar
);

CREATE TABLE "colors" (
  "id" integer PRIMARY KEY,
  "name" varchar,
  "episodes" varchar
);

CREATE TABLE "subjects" (
  "id" integer PRIMARY KEY,
  "name" varchar,
  "episodes" varchar
);

ALTER TABLE "months" ADD FOREIGN KEY ("episodes") REFERENCES "episodes" ("month");

CREATE TABLE "episodes_colors" (
  "episodes_colors" varchar,
  "colors_episodes" varchar,
  PRIMARY KEY ("episodes_colors", "colors_episodes")
);

ALTER TABLE "episodes_colors" ADD FOREIGN KEY ("episodes_colors") REFERENCES "episodes" ("colors");

ALTER TABLE "episodes_colors" ADD FOREIGN KEY ("colors_episodes") REFERENCES "colors" ("episodes");


CREATE TABLE "episodes_subjects" (
  "episodes_subjects" varchar,
  "subjects_episodes" varchar,
  PRIMARY KEY ("episodes_subjects", "subjects_episodes")
);

ALTER TABLE "episodes_subjects" ADD FOREIGN KEY ("episodes_subjects") REFERENCES "episodes" ("subjects");

ALTER TABLE "episodes_subjects" ADD FOREIGN KEY ("subjects_episodes") REFERENCES "subjects" ("episodes");


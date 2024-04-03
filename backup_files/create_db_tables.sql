DROP TABLE IF EXISTS "episodes", "months", "colors", "subjects";

CREATE TABLE IF NOT EXISTS "episodes" (
  "episode_id" integer PRIMARY KEY,
  "title" varchar,
  "air_date" varchar,
  "month_name" varchar,
  "color_id" int[],
  "subject_id" int[]
);

CREATE TABLE IF NOT EXISTS "months" (
  "month_name" varchar PRIMARY KEY,
  "episode_id" int[]
);

CREATE TABLE IF NOT EXISTS "colors" (
  "color_id" integer PRIMARY KEY,
  "color_name" varchar,
  "episode_id" int[]
);

CREATE TABLE IF NOT EXISTS "subjects" (
  "subject_id" integer PRIMARY KEY,
  "subject_name" varchar,
  "episode_id" int[]
);

ALTER TABLE "months" ADD FOREIGN KEY ("episode_id") REFERENCES "episodes" ("episode_id");
ALTER TABLE "episodes" ADD FOREIGN KEY ("month_name") REFERENCES "months" ("month_name");

ALTER TABLE "colors" ADD FOREIGN KEY ("episode_id") REFERENCES "episodes" ("episode_id");
ALTER TABLE "episodes" ADD FOREIGN KEY ("color_id") REFERENCES "colors" ("color_id");

ALTER TABLE "subjects" ADD FOREIGN KEY ("episode_id") REFERENCES "episodes" ("episode_id");
ALTER TABLE "episodes" ADD FOREIGN KEY ("subject_id") REFERENCES "subjects" ("subject_id");

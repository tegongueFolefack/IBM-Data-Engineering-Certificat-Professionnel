-- This script was generated by the ERD tool in pgAdmin 4.
-- Please log an issue at https://github.com/pgadmin-org/pgadmin4/issues/new/choose if you find any bugs, including reproduction steps.
BEGIN;


CREATE TABLE IF NOT EXISTS public."softcartDimDate"
(
    "DateID" integer NOT NULL,
    "DateValue" date,
    "Year" integer,
    "Month" integer,
    "MonthName" character(30),
    "Day" integer,
    "DayName" character(30),
    "Week" integer,
    PRIMARY KEY ("OrderID")
);

CREATE TABLE IF NOT EXISTS public."softcartDimCategory"
(
    "CategoryID" integer NOT NULL,
    "CategoryName" character(30),
    "CategoryDescription" text,
    PRIMARY KEY ("CategoryID")
);

CREATE TABLE IF NOT EXISTS public."softcartDimItem"
(
    "ItemID" integer NOT NULL,
    "ItemName" character(30),
    "CategoryID" integer,
    "Price" double precision,
    PRIMARY KEY ("ItemID")
);

CREATE TABLE IF NOT EXISTS public."softcartDimCountry"
(
    "CountryID" integer NOT NULL,
    "CountryName" character(50),
    "Region" character(50),
    PRIMARY KEY ("CountryID")
);

CREATE TABLE IF NOT EXISTS public."softcartFactSales"
(
    "SalesID" integer NOT NULL,
    "DateID" integer,
    "CategoryID" integer,
    "ItemID" integer,
    "CountryID" integer,
    "SalesAmount" double precision,
    "QuantitySold" integer,
    PRIMARY KEY ("SalesID")
);

ALTER TABLE IF EXISTS public."softcartDimItem"
    ADD CONSTRAINT "CategoryID" FOREIGN KEY ("CategoryID")
    REFERENCES public."softcartDimCategory" ("CategoryID") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public."softcartFactSales"
    ADD CONSTRAINT "CategoryID" FOREIGN KEY ("CategoryID")
    REFERENCES public."softcartDimCategory" ("CategoryID") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public."softcartFactSales"
    ADD CONSTRAINT "ItemID" FOREIGN KEY ("ItemID")
    REFERENCES public."softcartDimItem" ("ItemID") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public."softcartFactSales"
    ADD CONSTRAINT "DateID" FOREIGN KEY ("DateID")
    REFERENCES public."softcartDimDate" ("DateID") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public."softcartFactSales"
    ADD CONSTRAINT "CountryID" FOREIGN KEY ("CountryID")
    REFERENCES public."softcartDimCountry" ("CountryID") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public."softcartFactSales"
    ADD FOREIGN KEY ("DateID")
    REFERENCES public."softcartDimDate" ("DateID") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public."softcartFactSales"
    ADD FOREIGN KEY ("ItemID")
    REFERENCES public."softcartDimItem" ("ItemID") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public."softcartFactSales"
    ADD FOREIGN KEY ("CountryID")
    REFERENCES public."softcartDimCountry" ("CountryID") MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;

END;
----------------------------- Database Connection and Query -------------------------------

-- Create a database
CREATE DATABASE travel_ms_db;

-- Create a details table for storing data
CREATE TABLE details_table(
    bus_no varchar(50) primary key not null,
    from_place varchar(50),
    to_place varchar(50),
    departure_date varchar(50),
    departure_time varchar(50), 
    bus_agency varchar(50),
    station varchar(50),
    bus_type varchar(50), 
    fare varchar(50),
    reporting_time varchar(50),
    available_seats varchar(50),
    seats_sold varchar(50),
    seats_booked varchar(50),
    total_seats varchar(50),
    added_date varchar(50)
);


USE travel_ms_db;
SELECT * FROM details_table;
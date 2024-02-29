----------------------------- Database Connection and Query -------------------------------

-- Create a database
CREATE DATABASE travel_ms_db;

create table passenger_details
(
	passenger_register_id BIGINT AUTO_INCREMENT PRIMARY KEY not null,
	fname varchar(50),
    lname varchar(50),
    username varchar(50) UNIQUE not null,
    address varchar(100),
	contact varchar(50) UNIQUE not null,
    email varchar(100) UNIQUE not null,
    security_qn varchar(50),
    security_ans varchar(50),
    new_password varchar(50)
);


create table admin_code
(
	admin_code_id BIGINT AUTO_INCREMENT PRIMARY KEY not null,
    admin_code varchar(50) UNIQUE not null
);

insert into admin_code (admin_code) 
values ("admin");


create table admin_details
(
	admin_register_id BIGINT AUTO_INCREMENT PRIMARY KEY not null,
	fname varchar(50),
    lname varchar(50),
    username varchar(50) UNIQUE not null,
    address varchar(100),
	contact varchar(50) UNIQUE not null,
    email varchar(100) UNIQUE not null,
    security_qn varchar(50),
    security_ans varchar(50),
    new_password varchar(50)
);


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


create table bus_seat_bookings
(
	id BIGINT AUTO_INCREMENT PRIMARY KEY not null,
	bus_no varchar(50),
	booked_seats text(1000),
    seat_reference text(1000),
    added_date varchar(50),
    FOREIGN KEY (bus_no) REFERENCES details_table (bus_no) on delete cascade
);


create table booking_id_table
(
	booking_id BIGINT AUTO_INCREMENT PRIMARY KEY not null,
	bus_no varchar(50),
	booked_seats_wrt_id text(1000),
    seat_reference_wrt_id text(1000),
	booking_date varchar(50),
    FOREIGN KEY (bus_no) REFERENCES details_table (bus_no) on delete cascade
);


create table ticket_info_table
(
	ticket_id BIGINT AUTO_INCREMENT PRIMARY KEY not null,
	passenger_name varchar(50),
    mobile_no varchar(50) not null,
    booked_date varchar(50),
	bus_no varchar(50) not null,
    bus_agency varchar(100) ,
    bus_type varchar(50),
    from_place varchar(50),
    to_place varchar(50),
    departure_date varchar(50),
    departure_time varchar(50),
    seat_no text(1000),
    total_passenger varchar(50),
    fare varchar(50),
    total_price varchar(50),
    rept_time varchar(50),
    FOREIGN KEY (bus_no) REFERENCES details_table (bus_no) on delete cascade
);


create table track_table
(
	track_id BIGINT AUTO_INCREMENT PRIMARY KEY not null,
    from_place varchar(50),
    to_place varchar(50),
    departure_date varchar(50),
    searchby_combox varchar(50),
    searchby_entry varchar(50)
);

    
use travel_ms_db;
select * from details_table;
select * from bus_seat_bookings;
select * from booking_id_table;
select * from ticket_info_table;
select * from passenger_details;
select * from admin_details;
select * from admin_code;
select * from track_table;
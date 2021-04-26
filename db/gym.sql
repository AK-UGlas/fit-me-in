DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS activities;
DROP TABLE IF EXISTS locations;
DROP TABLE IF EXISTS members;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    premium BOOLEAN,
    active BOOLEAN
);

CREATE TABLE locations (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    capacity INT
);

CREATE TABLE activities (
    id SERIAL PRIMARY KEY,
    activity_name VARCHAR(255),
    start_time TIME,
    end_time TIME,
    date DATE,
    location_id INT REFERENCES locations(id)
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id),
    activity_id INT REFERENCES activities(id)
);
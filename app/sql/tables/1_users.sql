create table if not exists users (
    id serial primary key,
    username varchar(50) unique,
    email varchar(100) unique,
    password text not null,
    created_at timestamp default CURRENT_TIMESTAMP,
    las_update timestamp default CURRENT_TIMESTAMP
);
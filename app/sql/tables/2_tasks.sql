create table if not exists tasks (
    id serial primary key,
    title varchar(255),
    description text,
    priority varchar(50),
    deadline timestamp,
    status varchar(50),
    created_at timestamp default CURRENT_TIMESTAMP,
    last_update timestamp default CURRENT_TIMESTAMP,
    user_id integer not null,
    foreign key (user_id) references users(id)
);
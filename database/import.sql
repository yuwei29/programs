DROP TABLE IF EXISTS tb2;
create table tb2(
    id int,
    attr1 int,
    attr2 int,
    attr3 int,
    primary key(id)
);
copy tb2 from 'd:/personal/programs/database/test2.csv'
delimiter ',' csv header;
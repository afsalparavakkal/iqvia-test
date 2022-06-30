
-- psql queries 

-- counts for each driver, 2017 September deliveries that happened in Dubai (stats).

select count(1) from deliveries ds 
                inner join drivers dr 
                    on ds.driver_id = dr.id 
        where EXTRACT(year from ds.day)=2017 
            and EXTRACT(month from ds.day)=09  
            and dr.city='Dubai';


-- counts how many drivers made more than 1,000 overall deliveries in Dubai (top drivers).

select count(*) from (
                        select count(*) from deliveries ds 
                                        inner join drivers dr 
                                                on ds.driver_id = dr.id 
                                        where dr.city='Dubai' 
                                    group by dr.id having count(1) > 1000
                    ) as q ;




-- counts how many days driver John Smith made deliveries in 2017 September (active days).

select count(*) from (
                        select count(*) from deliveries ds 
                                            inner join drivers dr 
                                                on ds.driver_id = dr.id 
                                    where EXTRACT(year from ds.day)=2017 
                                          and EXTRACT(month from ds.day)=09 
                                          and dr.name='John Smith' 
                                    group by EXTRACT(day from ds.day) 
                    ) as q ;




-- counts deliveries on 2017-09-01 that were assigned to a non-existent driver (errors)


select count(*) from deliveries ds  
                where ds.day = '2017-09-01' 
                    and ds.driver_id not in (select id from drivers);




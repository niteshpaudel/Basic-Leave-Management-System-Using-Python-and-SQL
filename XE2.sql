create table leaveinfo
(
roll_no number not null,
leave_date date not null,
no_of_days number not null,
reason varchar2(50) not null,
approved varchar2(7),
remarks varchar2(30),
constraint pk primary key(roll_no,leave_date),
constraint fk_studentinfo foreign key(roll_no) references studentinfo(roll_no)
);

insert into studentinfo values('Asif',21770001,'mydatabase','Bsc.IT');
insert into studentinfo values('Danish',21770002,'mydatabase','Bsc.IT');
insert into studentinfo values('Fateen',21770003,'mydatabase','Bsc.IT');
insert into studentinfo values('Muneeb',21770004,'mydatabase','Bsc.IT');
insert into studentinfo values('Muzamil',21770005,'mydatabase','Bsc.IT');
insert into studentinfo values('Rubaan',21770006,'mydatabase','Bsc.IT');
insert into studentinfo values('Umar',21770007,'mydatabase','Bsc.IT');
insert into studentinfo values('Numaan',21770008,'mydatabase','Bsc.IT');
insert into studentinfo values('Manan',21770009,'mydatabase','Bsc.IT');
insert into studentinfo values('Nitesh',21770010,'mydatabase','Bsc.IT');
insert into studentinfo values('Atif',21770017,'mydatabase','BCA');
insert into studentinfo values('Mehak',21770018,'mydatabase','BCA');
insert into studentinfo values('Iqra',21770019,'mydatabase','BCA');
insert into studentinfo values('Saniya',21770020,'mydatabase','BCA');
insert into studentinfo values('Muneer',21770017,'mydatabase','Bcom');
insert into studentinfo values('Khushboo',21770028,'mydatabase','Bcom');
insert into studentinfo values('Tahir',21770029,'mydatabase','Bcom');
insert into studentinfo values('Baseer',21770110,'mydatabase','Mcom');
select * from studentinfo;
drop table leaveinfo;
describe leaveinfo;
select * from leaveinfo;
insert into leaveinfo values(21770010,'30-03-22',5,'sick leave','waiting','waiting');
select * from leaveinfo where roll_no = 21770010;

create table tempdate
(
today date
);
insert into tempdate values(to_date('12-03-22','dd-mm-yy'));
select * from tempdate;

select * from leaveinfo where roll_no=21770010;
create table hods
(
name varchar2(30) not null,
course varchar2(20) not null,
passwo varchar2(20) not null
);
select * from hods;
insert into hods values('Sameer Sir','bscit','bscit123');
insert into hods values('Bilal Sir','bca','bca123');
insert into hods values('Seema Mam','bba','bba123');
insert into hods values('Irfana Mam','bcom','bcom123');
insert into hods values('Sumair Sir','mba','mba123');
insert into hods values('Altaf sir','mcom','mcom123');
commit;
drop table hods;
select * from studentinfo;
insert into leaveinfo values(21770010,'30-03-22',5,'sick leave','waiting','waiting');
insert into leaveinfo values(21770001,'15-04-22',5,'sick leave','waiting','waiting');
insert into leaveinfo values(21770002,'07-03-22',5,'sick leave','waiting','waiting');
insert into leaveinfo values(21770003,'12-04-22',5,'sick leave','waiting','waiting');
insert into leaveinfo values(21770004,'14-03-22',5,'sick leave','waiting','waiting');
insert into leaveinfo values(21770005,'18-03-22',5,'sick leave','waiting','waiting');
insert into leaveinfo values(21770006,'19-03-22',5,'sick leave','waiting','waiting');
insert into leaveinfo values(21770007,'16-03-22',5,'sick leave','waiting','waiting');
insert into leaveinfo values(21770008,'18-04-22',5,'sick leave','waiting','waiting');
insert into leaveinfo values(21770009,'30-03-22',5,'sick leave','waiting','waiting');

select roll_no,name,leave_date,no_of_days,reason,approved,remarks from studentinfo inner join  leaveinfo using (roll_no);
select * from (select roll_no,name,leave_date,no_of_days,reason,approved,remarks,course from studentinfo inner join  leaveinfo using (roll_no)) where approved='waiting';


select * from (select roll_no,name,leave_date,no_of_days,reason,approved,remarks,course from studentinfo inner join  leaveinfo using (roll_no)) where approved='waiting' 

desc leaveinfo
update  studentinfo set course ='bca' where course='BCA'
select * from studentinfo;
select * from (select roll_no,name,leave_date,no_of_days,reason,approved,remarks,course from studentinfo inner join  leaveinfo using (roll_no)) where course='bscit' and approved='waiting'
select * from (select roll_no,name,leave_date,no_of_days,reason,approved,remarks,course from studentinfo inner join  leaveinfo using (roll_no)) where course='bscit' and approved='waiting'

select * from (select roll_no,name,leave_date,no_of_days,reason,approved,remarks,course from studentinfo inner join  leaveinfo using (roll_no)) where course='bscit' and approved='waiting'
select * from leaveinfo;
update studentinfo set approved = 'yes' and remarks = 'get well soon' where approved ='waiting' and remarks ='waiting';
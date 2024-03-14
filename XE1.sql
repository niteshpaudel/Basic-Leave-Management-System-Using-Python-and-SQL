create table studentinfo
(
name varchar2(20) not null,
roll_no number primary key,
password varchar2(30) not null, 
course varchar2(20)not null
);
create table leaveinfo
(
roll_no number not null foreign key,
leave_date date not null,
no_of_days number not null,
reason varchar2(50) not null,
approved varchar2(5) not null,
remarks varchar2(50) not null
constraint pk primary key(roll_no,leave_date)
);
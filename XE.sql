create table student
(
rollno number primary key,
name varchar2(20),
courseid number
);
create table course
(
coursename varchar2(15),
credits number,
courseid number
);
insert into student values(1,'Numaan Nazir',100);
insert into student values(2,'Danish Altaf',105);
insert into student values(3,'Fateen Nisar',103);
insert into student values(4,'Syed Muneef',100);
insert into student values(5,'Arif Sofi',103);
insert into student values(6,'Shakir Yousuf',100);
insert into course values('BCA',10,100);
insert into course values('BSC IT',8,103);
insert into course values('BCOM',6,105);
select * from student;
select * from course;
commit;
describe student;

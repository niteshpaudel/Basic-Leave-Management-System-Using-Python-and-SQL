select * from leaveinfo ;
describe leaveinfo;
select * from studentinfo;
update leaveinfo set approved='wai' where roll_no=21770010 and leave_date='16-03-22';

commit;

select * from (select roll_no,name,to_char(leave_date,'dd-mm-yy'),no_of_days,reason,approved,remarks,course from studentinfo inner join  leaveinfo using (roll_no)) 
select * from studentinfo;
select roll_no,'10',sum(no_of_days),10-sum(no_of_days) from leaveinfo where approved='yes' group by roll_no;

select sum(no_of_days) from leaveinfo where approved='yes' and roll_no=21770010;
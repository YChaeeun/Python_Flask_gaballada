create database project_db;
use project_db;

create table board_info_table(
board_idx   int primary key auto_increment,
board_name   varchar(500) not null unique
);


create table user_table(
user_idx int auto_increment,
user_name varchar(20) not null,
user_id varchar(200) not null unique,
user_pw   varchar(200) not null,
user_postal   char(7) not null,
user_addr1   varchar(200) not null,
user_addr2   varchar(200) not null,
user_status   int not null,
constraint user_pk primary key (user_idx)
);


create table study_table(
s_content_subject   varchar(500) not null,
s_content_idx   int primary key unique auto_increment,
s_content_writer_idx   int not null,
s_content_date   date not null,
s_content_text   varchar(500) not null,
s_content_file   varchar(500) unique,
s_content_status   int not null,
s_content_board_idx   int not null,
constraint s_content_fk1 foreign key(s_content_board_idx)
references board_info_table(board_idx),
constraint s_content_fk2 foreign key(s_content_writer_idx)
references user_table(user_idx)
);

create table club_table(
c_content_subject   varchar(500) not null,
c_content_idx   int primary key auto_increment,
c_content_writer_idx   int not null,
c_content_date   date not null,
c_content_text   varchar(500) not null,
c_content_file   varchar(500) unique,
c_content_status   int not null,
c_content_board_idx   int not null,
constraint c_content_fk1 foreign key(c_content_board_idx)
references board_info_table(board_idx),
constraint c_content_fk2 foreign key(c_content_writer_idx)
references user_table(user_idx)
);

create table activity_table(
a_content_subject   varchar(500) not null, 
a_content_idx   int primary key auto_increment,
a_content_text   varchar(500) not null,
a_content_file   varchar(500),
a_content_status   int not null,
a_content_board_idx   int not null,
constraint a_content_fk1 foreign key(a_content_board_idx)
references board_info_table(board_idx)
);

create table ex_table(
ex_content_subject   varchar(500) not null,
ex_content_idx   int primary key auto_increment,
ex_content_status   int not null,
ex_content_board_idx   int not null,
ex_input   varchar(500) not null,
ex_output   varchar(500) not null,
ex_content_date   date not null,
ex_test varchar(10000) not null,
ex_time_limit varchar(500) not null,
ex_memory_limit varchar(500) not null,
constraint ex_content_fk1 foreign key(ex_content_board_idx)
references board_info_table(board_idx)
);



create table free_table(
f_content_subject   varchar(500) not null,
f_content_idx   int primary key auto_increment,
f_content_writer_idx   int  not null,
f_content_date   date not null,
f_content_text   varchar(500) not null,
f_content_file   varchar(500) unique,
f_content_status   int not null,
f_content_board_idx   int not null,
f_view   int not null,
f_likes   int not null,
constraint f_content_fk1 foreign key(f_content_writer_idx)
references user_table(user_idx),
constraint f_content_fk2 foreign key(f_content_board_idx)
references board_info_table(board_idx)
);

create table app_table(
app_content_subject   varchar(500) not null,
app_content_idx   int primary key auto_increment,
app_content_writer_idx   int not null,
app_content_date   date not null,
app_content_text   varchar(500) not null,
app_content_file   varchar(500) unique,
app_content_status   int not null,
app_content_board_idx   int not null,
app_view   int not null,
app_likes   int not null,
constraint app_content_fk1 foreign key(app_content_writer_idx)
references user_table(user_idx),
constraint app_content_fk2 foreign key(app_content_board_idx)
references board_info_table(board_idx)
);

create table web_service_table(
web_content_subject   varchar(500) not null,
web_content_idx   int primary key auto_increment,
web_content_writer_idx   int not null,
web_content_date   date not null,
web_content_text   varchar(500) not null,
web_content_file   varchar(500) unique,
web_content_status   int not null,
web_content_board_idx   int not null,
web_view   int not null,
web_likes   int not null,
constraint web_content_fk1 foreign key(web_content_writer_idx)
references user_table(user_idx),
constraint web_content_fk2 foreign key(web_content_board_idx)
references board_info_table(board_idx)
);

create table m_service_table(
m_content_subject   varchar(500) not null,
m_content_idx   int primary key auto_increment,
m_content_writer_idx   int not null,
m_content_date   date not null,
m_content_text   varchar(500) not null,
m_content_file   varchar(500) unique,
m_content_status   int not null,
m_content_board_idx   int not null,
m_view   int not null,
m_likes   int not null,
constraint m_content_fk1 foreign key(m_content_writer_idx)
references user_table(user_idx),
constraint m_content_fk2 foreign key(m_content_board_idx)
references board_info_table(board_idx)
);

insert into board_info_table(board_name) values ('App');
insert into board_info_table(board_name) values ('Phone');
insert into board_info_table(board_name) values ('Web Service');
insert into board_info_table(board_name) values ('예제');
insert into board_info_table(board_name) values ('스터디ㆍ동아리');
insert into board_info_table(board_name) values ('공모전ㆍ대외활동');
insert into board_info_table(board_name) values ('자유게시판');


insert into ex_table(ex_content_subject, ex_test, ex_content_status, ex_content_board_idx, ex_input, ex_output, ex_content_date, ex_time_limit, ex_memory_limit)
values( "A+B", " 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.", 1, 4, "1,2", "3", curdate(),"2sec","128MB");

insert into ex_table(ex_content_subject, ex_test, ex_content_status, ex_content_board_idx, ex_input, ex_output, ex_content_date, ex_time_limit, ex_memory_limit)
values("수열 정렬", " P[0], P[1], ...., P[N-1]은 0부터 N-1까지(포함)의 수를 한 번씩 포함하고 있는 수열이다. 수열 P를 길이가 N인 배열 A에 적용하면 길이가 N인 배열 B가 된다. 적용하는 방법은 B[P[i]] = A[i]이다.
배열 A가 주어졌을 때, 수열 P를 적용한 결과가 비내림차순이 되는 수열을 찾는 프로그램을 작성하시오. 비내림차순이란, 각각의 원소가 바로 앞에 있는 원소보다 크거나 같을 경우를 말한다. 
만약 그러한 수열이 여러개라면 사전순으로 앞서는 것을 출력한다.", 1, 4, "첫째 줄에 배열 A의 크기 N이 주어진다.
둘째 줄에는 배열 A의 원소가 0번부터 차례대로 주어진다.
N은 50보다 작거나 같은 자연수이고, 배열의 원소는 1,000보다 작거나 같은 자연수이다.",
"첫째 줄에 비내림차순으로 만드는 수열 P를 출력한다.", curdate(), "2sec", "128MB");


insert into ex_table(ex_content_subject, ex_test, ex_content_status, ex_content_board_idx, ex_input, ex_output, ex_content_date, ex_time_limit, ex_memory_limit)
values( "쥐잡기",
"이번에 김지민은 쥐를 잡는 게임을 만들어냈다. 이 게임은 큰 보드 위를 움직이는 로봇 쥐를 가지고 한다. 
이 게임의 참가자는 정사각형 모양의 우리를 움직일 수 있다.
참가자는 이 우리를 보드 위라면 어느 곳이든지 이동할 수 있고, 떨어뜨려서 쥐를 잡을 수 있다.
하지만 김지민은 모든 쥐를 한 번에 잡는 것이 불가능하도록 우리의 크기를 작게 하고 싶다.
로봇 쥐는 2차원 평면에서 움직인다. 쥐는 항상 일정한 속도로 움직이고,
처음 위치가 알려져 있다고 가정한다. 
우리는 길이가 L이고 축에 평행한 정사각형 모양이고 회전시키지 못한다.
우리는 게임이 시작된 직후부터 움직이거나 떨어뜨릴 수 있다.
게임은 쥐가 우리 내부에 완벽하게 포함되어야 잡혔다고 간주한다.
만약 쥐가 우리의 경계에 있다면 그 쥐는 잡힌 쥐가 아니다.
한 번에 모든 쥐를 절대로 잡을 수 없는 가장 큰 L을 구하는 프로그램을 작성하시오. ", 1, 4,
"첫째 줄에 쥐의 수 N이 주어진다. N은 2보다 크거나 같고,
50보다 작거나 같은 자연수이다. 둘째 줄부터 각 쥐의 시작 위치와 속도가 주어진다.
이 값은 모두 절댓값이 1,000보다 작거나 같은 정수이다.
시작 위치를 (px, py)라고 하고, 속도가 (vx, vy)라면, t초 때 쥐의 위치는 (px+vx*t, py+vy*t)이다.",
"첫째 줄에 문제의 정답을 출력한다. 절대/상대 오차는 10-9까지 허용한다.", curdate(),"2sec","128MB");


insert into ex_table(ex_content_subject, ex_test, ex_content_status, ex_content_board_idx, ex_input, ex_output, ex_content_date, ex_time_limit, ex_memory_limit)
values( "마법의 구슬",
"옛날에 백은진이라는 마법사가 S개의 마법의 구슬을 만들었다. 이 마법의 구슬은 함께 모여있을 때는, 상상을 초월하는 힘의 근원이 된다. 이것을 김지민과 같은 악당이 사용하는 것을 막기 위해 백은진은 F개의 가짜 구슬을 만들었다. 이 가짜 구슬은 마법의 구슬과 똑같이 생겼지만, 마법의 힘은 없다.

이제 김형택은 세계를 지배하기 위해 어떤 구슬이 진짜 구슬인지 알아야 한다. 따라서 김지민은 N명의 사람을 모아서, S+F개 중 모든 S개의 조합을 테스트하기로 했다.

김형택은 각 사람들에게 미리 어떤 조합을 테스트 할 것인지 정해주었다. 그리고 같은 조합을 최대 한 번만 테스트한다.

그런데, 이 사람들은 절대로 다른 사람보다 일을 많이 하지 않는다. 즉, 모두 같은 개수의 조합을 테스트 한다. 따라서 김형택은 몇 명의 사람을 뽑아야, 모든 조합을 테스트하면서, 모든 사람이 같은 횟수의 테스트를 하는지 궁금해졌다.

김형택이 모을 수 있는 사람의 최댓값 M이 주어질 때, M을 넘지 않으면서, 김형택이 뽑을 수 있는 최대 사람의 수를 구하는 프로그램을 작성하시오", 1, 4,
"첫째 줄에 S F M이 주어진다. S와 F는 1,000,000,000보다 작거나 같은 자연수이고, M은 100,000보다 작거나 같은 자연수이다.",
"첫째 줄에 문제의 정답을 출력한다. 만약 불가능 할 때는 -1을 출력한다.",
 curdate(),"2sec","128MB");
 
 
insert into ex_table(ex_content_subject, ex_test, ex_content_status, ex_content_board_idx, ex_input, ex_output, ex_content_date, ex_time_limit, ex_memory_limit)
values( "방 번호",
"이번에 VIP 회장으로 새로 부임한 백은진은 빅뱅의 위대함을 세계에 널리 알리기 위해서 사무실을 하나 임대했다.

빅뱅은 위대하기 때문에, 사무실의 번호도 되도록이면 커야 한다고 생각한다. 따라서 지금 가지고 있는 돈 전부를 가지고 방 번호를 만들려고 한다.

1층에 있는 문방구에서는 숫자를 판다. 각 숫자의 가격은 서로 같지 않기 때문에, 현재 가지고 있는 돈을 이용해서 만들 수 있는 가장 큰 숫자를 만들려고 한다.

예를 들어, 문방구에서 파는 숫자가 0, 1, 2이고, 각 숫자의 가격이 6, 7, 8이고, 백은진이 현재 가지고 있는 돈이 21이라면, 백은진이 만들 수 있는 가장 큰 수는 210(8+7+6=21)이다.", 1, 4,
"문방구에서 파는 숫자의 개수 N이 주어진다. N은 10보다 작거나 같은 자연수이다. 문방구에서 파는 숫자는 0보다 크거나 같고, N-1보다 작거나 같은 자연수이다. 예를 들어, N=4이면, 문방구에서 파는 숫자는 0,1,2,3인 것이다. 둘째 줄에 숫자 0을 사는 비용, 숫자 1을 사는 비용, … 숫자 N-1을 사는 비용이 차례대로 주어진다. 이 비용은 10^18보다 작거나 같다. 마지막 줄에는 백은진이 현재 가지고 있는 돈이 주어진다. 돈은 10^18보다 작거나 같은 자연수 또는 0이다.",
"첫째 줄에 백은진이 가지고 있는 돈으로 만들 수 있는 가장 큰 수의 자리수를 출력한다. 둘째 줄에는 그 수의 처음 50자리를 출력하고, 셋째 줄에는 그 수의 마지막 50자리를 출력한다.",
curdate(),"2sec","128MB");


insert into ex_table(ex_content_subject, ex_test, ex_content_status, ex_content_board_idx, ex_input, ex_output, ex_content_date, ex_time_limit, ex_memory_limit)
values( "소트게임",
"홍준이는 소트 게임을 하려고 한다. 소트 게임은 1~N으로 이루어진 N자리의 순열을 이용한다. 이 게임에선 2보다 크거나 같고 N보다 작거나 같은 수 K가 주어진다.

홍준이가 어떤 수를 뒤집는다고 하면, 그 수부터, 오른쪽으로 총 K개의 수를 뒤집는 것이다.

예를 들어 순열이 5 4 3 2 1 이었고, 여기서 K가 3일 때, 4를 뒤집으면 5 2 3 4 1이 된다. (뒤집는 다는 소리는 순서를 역순으로 바꾼다는 것)

반드시 K개의 수를 뒤집어야하기 때문에, 처음 상태에서 2나 1을 선택하는 것은 불가능하다.

홍준이는 입력으로 들어온 순열을 오름차순으로 만들려고 한다. 오름차순으로 만들면 게임이 끝난다.

홍준이가 게임을 빨리 끝내려고 할 때, 수를 최소 몇 개 선택해야 하는지 출력하는 프로그램을 작성하시오.", 1, 4,
"첫째 줄에 순열의 크기 N과 K가 주어진다. N은 2보다 크거나 같고, 8보다 작거나 같다. 둘째 줄에 순열에 들어가는 수가 주어진다.",
"첫째 줄에 정답을 출력한다. 만약 오름차순으로 만들 수 없으면 -1을 출력한다.",
curdate(),"2sec","128MB");

insert into ex_table(ex_content_subject, ex_test, ex_content_status, ex_content_board_idx, ex_input, ex_output, ex_content_date, ex_time_limit, ex_memory_limit)
values( "부재중 전화",
"얼마전, Day Of Mourning의 새 앨범이 나왔고, 강토는 이 앨범을 들으려고 한다.

이 앨범에는 총 노래가 N곡이 들어있고, 모든 노래의 길이는 L초이다. 그리고, 노래와 노래 사이에는 5초 동안 아무 노래도 들리지 않는 조용한 구간이 있다.

강토가 앨범의 첫 곡을 듣는 순간이 0초이다. 그리고 그 0초부터 강토의 전화벨이 울리기 시작한다. 전화벨은 D초에 1번씩 울리며, 한 번 울릴 때 1초동안 울린다.

강토는 락 스피릿을 진심으로 느끼기 위해서 볼륨을 매우 크게 하고 듣기 때문에, 노래가 나오는 중에는 전화벨 소리를 듣지 못한다.

만약, 전화벨이 노래가 시작되는 순간 울린다면, 강토는 전화를 받지 못한다. 또, 전화벨이 노래가 끝나는 순간 같이 끝난다면, 강토는 전화를 받을 수 없다.

강토는 앨범을 1번만 듣는다. 즉, 모든 앨범 수록곡을 다 듣고 난 후에는 전화벨을 들을 수 있다.

강토가 전화벨을 들을 수 있는 가장 빠른 시간을 구하는 프로그램을 작성하시오.", 1, 4,
"첫째 줄에 N, L, D가 공백을 사이에 두고 주어진다. 모든 수는 1,000보다 작거나 같은 자연수이다.",
"첫째 줄에 강토가 전화벨을 들을 수 있는 가장 빠른 시간을 출력한다.",
curdate(),"2sec","128MB");

insert into ex_table(ex_content_subject, ex_test, ex_content_status, ex_content_board_idx, ex_input, ex_output, ex_content_date, ex_time_limit, ex_memory_limit)
values( "보물",
"옛날 옛적에 수학이 항상 큰 골칫거리였던 나라가 있었다. 이 나라의 국왕 김지민은 다음과 같은 문제를 내고 큰 상금을 걸었다.

길이가 N인 정수 배열 A와 B가 있다. 다음과 같이 함수 S를 정의하자.

S = A[0]*B[0] + ... + A[N-1]*B[N-1]

S의 값을 가장 작게 만들기 위해 A의 수를 재배열하자. 단, B에 있는 수는 재배열하면 안된다.

S의 최솟값을 출력하는 프로그램을 작성하시오.",
1, 4, "첫째 줄에 N이 주어진다. 둘째 줄에는 A에 있는 N개의 수가 순서대로 주어지고, 셋째 줄에는 B에 있는 수가 순서대로 주어진다. N은 50보다 작거나 같은 자연수이고, A와 B의 각 원소는 100보다 작거나 같은 음이 아닌 정수이다.",
"첫째 줄에 S의 최솟값을 출력한다.",
curdate(),"2sec","128MB");

insert into ex_table(ex_content_subject, ex_test, ex_content_status, ex_content_board_idx, ex_input, ex_output, ex_content_date, ex_time_limit, ex_memory_limit)
values( "수2",
 "Lucky Set이란 정수의 집합이다.

구간 [A,B]란 A보다 크거나 같고, B보다 작거나 같은 모든 정수가 있는 구간이다. 이때, A와 B는 모두 양수이고, B는 A보다 크다.

구간 [A,B]가 Unlucky가 되기 위해선 구간에 속한 모든 정수가 Lucky Set에 없어야 한다.

Lucky Set과 N이 주어질 때, N을 포함하는 Unlucky 구간의 개수를 구하는 프로그램을 작성하시오.",
 1, 4, "첫째 줄에 Lucky Set에 포함된 숫자의 개수 L이 주어진다. 둘째 줄에는 L개의 수가 주어진다. 이 수는 1,000보다 작거나 같은 자연수이고, L은 50보다 작거나 같은 자연수이다. 그리고 중복되지 않는다. 마지막 줄에는 N이 주어진다. N은 Lucky Set에서 가장 큰 수보다 작거나 같은 자연수이다.",
 "첫째 줄에 문제의 정답을 출력한다.",
 curdate(),"2sec","128MB");
 
 insert into ex_table(ex_content_subject, ex_test, ex_content_status, ex_content_board_idx, ex_input, ex_output, ex_content_date, ex_time_limit, ex_memory_limit)
values( "gcd(n,k) = 1",
 " 자연수 n이 주어졌을 때, gcd(n, k) = 1을 만족하는 자연수 1 ≤ k ≤ n 의 개수를 구하는 프로그램을 작성하시오.",
 1, 4, "첫째 줄에 자연수 n (1 ≤ n ≤ 1018)이 주어진다.",
 "gcd(n, k) = 1을 만족하는 자연수 1 ≤ k ≤ n 의 개수를 출력한다.",
 curdate(),"2sec","512MB");
 
 insert into ex_table(ex_content_subject, ex_test, ex_content_status, ex_content_board_idx, ex_input, ex_output, ex_content_date, ex_time_limit, ex_memory_limit)
values( "도깨비 말",
 "도깨비말은 언어 유희 중 하나로, 글자를 특정 법칙에 따라 재구성하는 것을 말한다.

영어권에서는 피그라틴어라는 것이 있다. 주로 어린이들이 많이 쓰는 데, 남들에게 무슨 말인지 모르게 하기 위해 종종 쓴다. 

여기엔 규칙이 있는데, 맨 앞글자가 모음이 아닐때 까지 맨 앞 글자를 어미로 돌린 후 그 끝에 ay를 붙여서 완성한다. 예를 들면 frog는 ogfray이 된다. 만약 맨 앞자음이 없는 apple과 같은 경우는 끝에 ay만 붙여 appleay가 된다. 또는, 단어에 모음이 없는 경우에도 단어의 끝에 ay만 붙인다.

주어진 단어를 피그라틴어로 바꾸는 프로그램을 작성하시오.",
 1, 4, "한 줄에 하나의 단어씩 주어진다. 그리고 마지막 줄에 #을 입력받고 끝낸다.

주어진 단어는 20자를 넘지 않고 공백없이 소문자로만 이루어져있다. 여기서 모음이란 'a', 'e', 'i', 'o', 'u' 를 말한다.",
 "한 줄에 하나씩 피그라틴어를 출력한다.",
 curdate(),"1sec","128MB");

select *s
from web_service_table;

update web_service_table
set web_likes = 54
where web_content_idx = 4;
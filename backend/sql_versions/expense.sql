create sequence if not exists expense_id_seq start 1 increment 1
;
create table if not exists expense (
  expense_id      BIGINT primary key default nextval('expense_id_seq')
  ,	category      varchar(50)
  ,	amount        float(50)
  , side_note     varchar(100)
  , expense_ts    timestamp without time zone default current_timestamp
  , create_ts     timestamp without time zone default current_timestamp
  , user_name     varchar(30)
)
;
场景需求：
   有一定功能的脚本，运行在一台instance 机器上，为了确保该机器挂掉脚本功能照样work, 请设计一种方法将两台或超过两台的instance上都运行着这个脚本，但是同一时间只有一个实例脚本上的功能是work的，其他实例上只有检测到该正常work的脚本出现了异常，才会及时启动自身脚本功能继续工作。

以下是我的设计思路：
数据库中先创建好heartbeat表
脚本执行逻辑：
先锁定整张表防止查询数据不一致情况发生
然后查询results = select ip, timestamp from timestamp where status = 1
如果results为空 说明还没有active (status=1)实例，如果实例自身在heartbeat表中不存在就直接插入，否则把自身设置为active 并且更新timestamp字段 ,执行的sql语句为
( insert into heartbeat(ip, timestamp, status) values(selfIP, int(time.time()), 1) on duplicate key update status = 1, timestamp = int(time.time()))，最后执行脚本实际要做的功能
如果results不为空 就一个个result 判断，看看 timestamp有没有超时，目前设置是5分钟，如果五分钟没有超时，则检查ip值是不是当前实例的ip，如果是就更新timestamp字段 
并且更新flag 为true 退出 for 循环
循环结束后判断flag， 如果为false说明 不存在正常工作的 instance，所以这个时候设置自身为status=1 并且更新timestamp，同样如果自身在heartbeat表里面不存在就直接插入一条新的记录，执行的sql语句为
（insert into heartbeat(ip, timestamp, status) values(selfIP, int(time.time()), 1) on duplicate key update status = 1, timestamp = int(time.time())）最后启动自身脚本功能
最后释放表锁

部署环节：
只需要创建好 heartbeat表，启动多个运行着实际script 的实例即可，不需要初始化heartbeat表，脚本会自动更新表。

详细设计：
# table name: heartbeat
# table structure:
create table heartbeat(id int primary key NOT NULL auto_increment,
                       ip varchar(24) NOT NULL,
                       timestamp int NOT NULL,
                       status bool NOT NULL);
# create unique for ip field
create unique index ip_unique on heartbeat(ip);

mysql> desc heartbeat;
+-----------+-------------+------+-----+---------+----------------+
| Field     | Type        | Null | Key | Default | Extra          |
+-----------+-------------+------+-----+---------+----------------+
| id        | int(11)     | NO   | PRI | NULL    | auto_increment |
| ip        | varchar(24) | NO   | UNI | NULL    |                |
| timestamp | int(11)     | NO   |     | NULL    |                |
| status    | tinyint(1)  | NO   |     | NULL    |                |
+-----------+-------------+------+-----+---------+----------------+
4 rows in set (0.00 sec)

script logic:
    lock heartbeat table
    # select ip and timestamp value where status = 1
    # Note: status equal to 1 means active instance and status equal to 0 means inactive
    results = select ip, timestamp from timestamp where status = 1
    flag = False # to record whether exists active and work noraml instance or not
    if not results:
        # not exists active instance
        # we will set the script itself instance as active
        # "insert into ... on duplicate key", if selfIP exists we update status field
        # equal to 1 and update timestamp or we insert a new record into heartbeat table
        # and finally we start the script to make its function enable
        insert into heartbeat(ip, timestamp, status) values(selfIP, int(time.time()), 1)
        on duplicate key update status = 1, timestamp = int(time.time())

        execute script function
    else:
        # exists active instance
        # we begin to judge whether the instance work or not
        for ip, timestamp in results:
            if int(time.time())-timestamp <= 5*60:
                # the instance of the ip timestamp field not timeout
                # if selfIP equal to ip, we update the timestamp field
                if ip == selfIP:
                    # selfIP value is the instance itself ip address
                    update heartbeat set timestamp = int(time.time());
                # flag = True means active instance exists and work normal
                flag = True
                break
        if not flag:
            # active instance exists but can not work
            # we set the instance itself as active and update the timestamp
            # then enable the script function
            insert into heartbeat(ip, timestamp, status) values(selfIP, int(time.time()), 1)
            on duplicate key update status = 1, timestamp = int(time.time())

            execute script function
    unlock heartbeat table




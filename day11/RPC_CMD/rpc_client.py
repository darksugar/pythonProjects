#Author:Ivor
import pika
import uuid
import time,random,json

class Cmd_RPC_Client(object):
    def __init__(self):
        self.task_dic = {}
        self.corr_id = str(uuid.uuid4())
        #实例连接
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='localhost'))
        #实例频道
        self.channel = self.connection.channel()
        #实例消息返回队列
        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue
        self.channel.basic_consume(self.on_response,
                                   no_ack=True,
                                   queue=self.callback_queue)
        #实例发布exchange
        self.channel.exchange_declare(exchange='ssh_client',
                         type='direct')

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = json.loads(body.decode())
            # print(self.response)
            host = self.response["host"]
            res = self.response["res_msg"]
            task_id = self.response["task_id"]
            self.task_dic[task_id][host] = res

    def run(self,cmd_list):
        if cmd_list[0] == "run":
            if cmd_list[2].startswith("--"):
                cmd = cmd_list[1]
                hosts = cmd_list[3:]
            elif cmd_list[2].startswith("-"):
                cmd = cmd_list[1] + " " + cmd_list[2]
                hosts = cmd_list[4:]
            else:
                cmd = cmd_list[1]
                hosts = cmd_list[3:]
            print(cmd, hosts)
            task_id = str(time.time())[-4:]
            msg = {
                "task_id":task_id,
                "cmd":cmd
            }
            msg = json.dumps(msg).encode()
            self.call(msg,hosts)
            for host in hosts:
                self.task_dic[task_id] = {
                    host:None
                }
            self.task_dic[task_id]["task_num"] = len(hosts)
            return print("task id:",task_id)

    def call(self, msg, hosts):
        for host in hosts:
            print(host)
            print(msg)
            self.channel.basic_publish(exchange='ssh_client',
                                       routing_key=host,
                                       properties=pika.BasicProperties(
                                           reply_to=self.callback_queue,
                                           correlation_id=self.corr_id,
                                       ),
                                       body=msg)

    def check_task(self,cmd_list):
        # for num in range(self.task_dic[cmd_list[1]]["task_num"]):
        self.connection.process_data_events()
        # print(self.task_dic)
        if all(self.task_dic.get(cmd_list[1]).values()):
            for k,v in self.task_dic.get((cmd_list[1])).items():
                if k == "task_num":
                    continue
                print(k.center(50,"-"))
                print(v)
        return print("CMD is executing...")

        # for res_key in self.task_dic.get(cmd_list[1]):
        #     if not self.task_dic[cmd_list[1]][res_key]:
        #         return print("CMD is executing...")
        # if self.task_dic.get(cmd_list[1]) is None:
        #     return print("CMD is executing...")
        # return print(self.task_dic.get(cmd_list[1]))

exec_cmd = Cmd_RPC_Client()
menu = '''  CMD EXAMPLE
run "dir" --host 1.1.1.1 2.2.2.2
check_task 6666
'''
print(menu)
while True:
    cmd = input(">>>:")
    cmd_list = cmd.strip().split(" ")
    # print(cmd_list)
    if hasattr(exec_cmd,cmd_list[0]):
        func = getattr(exec_cmd,cmd_list[0])
        func(cmd_list)
    else:
        print("Invalid CMD...")
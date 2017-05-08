#Author:Ivor
import pika
import uuid
import time,random,json

class Cmd_RPC_Client(object):
    def __init__(self):
        self.task_dic = {}
        self.corr_id = str(uuid.uuid4())
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='localhost'))
        self.channel = self.connection.channel()
        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue
        self.channel.basic_consume(self.on_response,
                                   no_ack=True,
                                   queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            # print(self.response)
            self.response = json.loads(body.decode())
            task_id = self.response["task_id"]
            res = self.response
            self.task_dic[task_id] = res


    def run(self,cmd_list):
        if cmd_list[0] == "run":
            if cmd_list[2].startswith("-"):
                cmd = cmd_list[1] + " " + cmd_list[2]
                hosts = cmd_list[4:]
            else:
                cmd = cmd_list[1]
                hosts = cmd_list[3:]
            print(cmd, hosts)
            task_id = str(time.time())[-4:]
            msg = {
                "task_id":task_id,
                "cmd":cmd,
                "hosts":hosts
            }
            msg = json.dumps(msg).encode()
            self.call(msg)
            self.task_dic[task_id] = None
            return print("task id:",task_id)

    def call(self, msg):
        self.response = None
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(
                                       reply_to=self.callback_queue,
                                       correlation_id=self.corr_id,
                                   ),
                                   body=msg)
        self.connection.process_data_events()

    def check(self,cmd_list):
        self.connection.process_data_events()
        if self.task_dic.get(cmd_list[1]) is None:
            return print("CMD is executing...")
        return print(self.task_dic.get(cmd_list[1]))

exec_cmd = Cmd_RPC_Client()
while True:
    cmd = input(">>>:")
    cmd_list = cmd.strip().split(" ")
    print(cmd_list)
    if hasattr(exec_cmd,cmd_list[0]):
        func = getattr(exec_cmd,cmd_list[0])
        func(cmd_list)

#  run "df -h" --host 1.1.1.1 2.2.22.2
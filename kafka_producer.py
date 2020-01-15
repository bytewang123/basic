from kafka import KafkaProducer 

producer = KafkaProducer(bootstrap_servers=['localhost1:9092', 'localhost2:9092'])
for i in xrange(0, 9):
    msg = 'this[%s],is[%s],test[%s],kafka[%s],message[%s],%s'%(i, i, i, i, i, i)
    print msg
    producer.send('test_async', msg)

producer.close()

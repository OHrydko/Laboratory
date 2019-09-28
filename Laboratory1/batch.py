from cassandra.cluster import Cluster
from cassandra.query import BatchStatement, BatchType,SimpleStatement
from cassandra import ConsistencyLevel


cluster = Cluster()
session = cluster.connect('organizationsofevents')
update_plan = session.prepare('''update organizationsOfEvents.planOfEvent set name = 'adasda' where eventId = 1 ;''')
update_user = session.prepare('''update organizationsOfEvents.user set countOfEvent = 122 where userId = 1;
''')
batch = BatchStatement(consistency_level=ConsistencyLevel.ONE)

batch.add(update_plan)
batch.add(update_user)
    
session.execute(batch)





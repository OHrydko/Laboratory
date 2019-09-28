from cassandra.cluster import Cluster
from cassandra.query import BatchStatement, BatchType,SimpleStatement
from cassandra import ConsistencyLevel

cluster = Cluster()
session = cluster.connect('organizationsofevents')


session.execute("create index if not exists on organizationsOfEvents.event(userId);")
categoryAndCompany = SimpleStatement(
    "select category,company from organizationsOfEvents.planOfEvent where eventId = 1;",
    consistency_level=ConsistencyLevel.ONE)
session.execute(categoryAndCompany)

hashtagFromDate = SimpleStatement(
    "select hashtag,date from organizationsOfEvents.planOfEvent where eventId = 1;",
    consistency_level=ConsistencyLevel.ONE)
session.execute(hashtagFromDate)


userEvent = SimpleStatement(
    "select * from organizationsOfEvents.event where userId = 1;",
    consistency_level=ConsistencyLevel.ONE)
session.execute(userEvent)

nameOfBonus = SimpleStatement(
    "select name,value from organizationsOfEvents.bonus where eventId = 1;",
    consistency_level=ConsistencyLevel.ONE)
session.execute(nameOfBonus)






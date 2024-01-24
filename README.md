# GCP - Container 2 - Docker Images and Custom Builds

wildcodeschool quest solution

## Result

sudo docker exec -it mongodb bash
test> use testdb
switched to db testdb
testdb> show collections
testcollection
testdb> db.testcollection.find()
[
  {
    _id: ObjectId('65b0eb018f0c5644df57537d'),
    message: 'Hello from Python to MongoDB!',
    timestamp: ISODate('2024-01-24T10:48:33.256Z')
  }
]

More info in the these files:

- GCP_container_log.txt
- all_commands.txt


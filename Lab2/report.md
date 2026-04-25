\# Lab 2 Report: Distributed Consistency and Consensus in the Cloud



\## 1. Introduction

This lab explores how distributed systems handle consistency, availability, 

and consensus under different conditions using Redis and etcd.



\*\*Tools Used:\*\*

\- Docker 29.4.0

\- Redis 7 (Replication)

\- etcd v3.5.9 (Raft Consensus)



\---



\## 2. Methodology



\### Task 1: Redis Replication \& CAP Theorem

\- Deployed 2 Redis nodes (Master/Replica) using Docker Compose

\- Wrote key-value pairs to redis-node1 (Master)

\- Read from redis-node2 (Replica) to verify replication

\- Simulated network partition by stopping redis-node2

\- Observed write availability during partition

\- Restarted redis-node2 and verified automatic sync



\### Task 2: Raft Consensus with etcd

\- Deployed 3-node etcd cluster using Docker Compose

\- Identified cluster Leader using endpoint status

\- Wrote key-value pair (foo=bar) to the cluster

\- Stopped the Leader (etcd1) to trigger re-election

\- Observed new Leader election (etcd3)

\- Restarted etcd1 and verified it rejoined as Follower



\---



\## 3. Results



\### Task 1: Redis Replication

| Step | Command | Result |

|------|---------|--------|

| Write to node1 | SET mykey "Hello from Node1" | OK |

| Read from node2 | GET mykey | "Hello from Node1" |

| Stop node2 (Partition) | docker stop redis-node2 | Stopped |

| Write during partition | SET newkey "Written during partition" | OK |

| Read from stopped node2 | GET newkey | Error: container not running |

| Restart node2 | docker start redis-node2 | Started |

| Read after recovery | GET newkey | "Written during partition" |



\### Task 2: etcd Raft Consensus

| Step | Result |

|------|--------|

| Initial Leader | etcd1 (RAFT TERM = 2) |

| Write foo=bar | OK |

| Read foo | bar |

| Stop etcd1 | Leader removed |

| New Leader | etcd3 (RAFT TERM = 3) |

| etcd1 rejoined | Follower (RAFT TERM = 3) |



\---



\## 4. Analysis



\### CAP Theorem - Redis

Redis chose \*\*AP (Availability + Partition Tolerance)\*\*:

\- During network partition, redis-node1 continued accepting writes

\- Consistency was temporarily sacrificed

\- After recovery, \*\*Eventual Consistency\*\* was achieved automatically



\### Raft Consensus - etcd

etcd chose \*\*CP (Consistency + Partition Tolerance)\*\*:

\- When Leader failed, cluster held election automatically

\- New Leader elected in RAFT TERM 3

\- System maintained consistency through Raft protocol

\- Majority quorum (2 out of 3) was enough to elect new Leader



\---



\## 5. Discussion Questions



\*\*Q1: What does CAP theorem state?\*\*

CAP theorem states that a distributed system can only guarantee 

two out of three properties simultaneously:

\- \*\*C\*\*onsistency: All nodes see the same data

\- \*\*A\*\*vailability: System always responds

\- \*\*P\*\*artition Tolerance: System works despite network failures



\*\*Q2: Which CAP properties does Redis sacrifice during partition?\*\*

Redis sacrifices \*\*Consistency\*\* during partition. It remains 

Available and Partition Tolerant (AP system), achieving only 

Eventual Consistency after recovery.



\*\*Q3: How does Raft ensure consensus?\*\*

Raft works through:

1\. \*\*Leader Election\*\*: Nodes vote for a Leader

2\. \*\*Log Replication\*\*: Leader replicates all writes to Followers

3\. \*\*Majority Quorum\*\*: Need (n/2)+1 nodes to agree

4\. \*\*Term Numbers\*\*: Each election gets a new term number



\*\*Q4: What happened when etcd1 (Leader) stopped?\*\*

\- etcd2 and etcd3 detected no heartbeat from Leader

\- They started a new election (RAFT TERM 2 to 3)

\- etcd3 won the election and became new Leader

\- When etcd1 restarted, it rejoined as Follower



\---



\## 6. Conclusion

This lab demonstrated:

1\. Redis implements \*\*Eventual Consistency\*\* (AP system)

2\. etcd implements \*\*Strong Consistency\*\* via Raft (CP system)

3\. Network partitions affect different systems differently

4\. Raft consensus provides automatic failover and recovery



\---



\## 7. Environment

\- OS: Windows 11

\- Docker: 29.4.0

\- Redis: 7

\- etcd: v3.5.9


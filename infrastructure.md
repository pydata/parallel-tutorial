Threads v. Processes
--------------------

*  <img src="images/multi-threaded-process.svg" width="30%" align="right">

    **Multithreading**:

    *  Share data
    *  C/NumPy/Pandas
    *  Fast but dangerous

*  **Multiprocessing**:

    <img src="images/multiple-processes.svg" width="30%" align="right">

    *  Transfer data
    *  Pure Python
    *  Avoids GIL issues


Distributed Systems
-------------------

Multiple computers talk to each other over network sockets

<img src="images/multi-threaded-process.svg" width="30%">
<img src="images/multi-threaded-process.svg" width="30%">
<img src="images/multi-threaded-process.svg" width="30%">

Extreme version of multi-processing.  Lose shared disk, shared software
environments, etc..


Distributed Systems
-------------------

<img src="images/network.svg" width="70%">


Communication Bandwidth
-----------------------

Workers communicate with various technologies.

These mechanisms all have associated speeds.

*  Shared memory (threads): **Infinite**
*  Inter-Process-Communication: **300 MB/s**
*  Ethernet:  **100 MB/s** or 1000 MB/s (optimistically)


## Serialization

*  Turns Python objects: `'hello', np.ones(5)`
*  Into Bytes: `00000001`

<hr>

*  Python Objects: 100 MB/s
*  Numeric arrays: 2000 MB/s

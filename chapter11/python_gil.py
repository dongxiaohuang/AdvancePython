# Python 中的线程对应 c 语言中的一个线程。
# Python 前期为了简单，在解释器上加一把非常大的锁，也就是说同一时刻只有一个线程运行，无法将多个线程映射到多个 CPU 上，并发很受限，
# 也就是说，Python 是没有多线程的。
# 不过 gil 也不是会等待一个线程执行完再执行下一个线程，它也是会释放的，它会根据执行的字节码的行数以及时间片等释放 gil，
# 遇到 IO 操作时也会释放（这使得 Python 是比较适合 IO 多的操作）。

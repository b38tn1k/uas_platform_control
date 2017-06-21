import time
running = 0
count = 0
while True:
    count = count + 1
    then = time.time()
    time.sleep(0.5)
    now = time.time()
    running = running + (now - then)
    print "Average sleep time: " + str(running/count)


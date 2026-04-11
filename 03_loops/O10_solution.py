import time 

# for i in range(10):
#     time.sleep(5)
#     print(i)

wait_time = 1
max_retires = 5
attempts = 0

while attempts < max_retires:
    print("Attempts", attempts+1,"_wait time",wait_time,)
    time.sleep(wait_time)
    wait_time *= 2
    attempts +=1
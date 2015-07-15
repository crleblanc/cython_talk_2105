# Simple Julia test for running sin() over a large array
time1 = time()
worker_array = [0.0:1.0/5000000:1.0]
output_array = sin(worker_array)
time2 = time()

println(time2-time1)
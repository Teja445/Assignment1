# AWS EC2 Auto-Scaling Simulator
This Python script simulates an EC2 auto-scaling mechanism based on CPU usage. It reads CPU data from a file and adjusta the number of instances based on preset CPU limits.

# How it works
1. the script reads the metrics.json file data that contains CPU usage data over time.
2. It scales up when the average CPU usage goes over 70%
3. It scales down when CPU usage falls below 20% and only if more than one instance is running.

## Usage
1. Ensure that 'metrics.json' file contains the CPU utilization data in the required format.
2. Run the script using the the following command:
     python auto_scaling.py
   
## Scaling Logic
1. For each time inetrval, the script shows the current time, CPU usage, and number of instances.
2. The script waits 1 second between each metric to simulate processing in real-time.
3. The Python script scales up (adds am instance) if the CPU utilization is more than 70%.
4. It scales down (removes the instance) if CPU utilization falls below 20% and there's more than one instance running.

## Sample Output

1. Time 05-11-2024T10:00:00 | Current CPU utilization: 50% | Instances: 1

2. Time 05-11-2024T11:00:00 | Current CPU utilization: 75% | Instances: 2



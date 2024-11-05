# AWS EC2 Auto-Scaling Simulator
This Python script simulates an auto-scaling mechanism based on CPU utilization metrics.

## Usage
1. Ensure that 'metrics.json' file contains the CPU utilization data in the required format.
2. Run the script using the the following command:
     python auto_scaling_simulator.py
   
## Scaling Logic
1. The Python script scales up (adds am instance) if the CPU utilization is more than 70%.
2. It scales down (removes the instance) if CPU utilization falls below 20% and there's more than one instance running.

## Sample Output

1. Time 05-11-2024T10:00:00 | Current CPU utilization: 50% | Instances: 1

2. Time 05-11-2024T11:00:00 | Current CPU utilization: 75% | Instances: 2



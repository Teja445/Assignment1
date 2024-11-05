import json
import time
# Scaling thresholds
SCALE_UP_THRESHOLD = 70
SCALE_DOWN_THRESHOLD = 20
# Initial number of instances
instance_count = 1

def load_mertics(file_path):
  with open(file_path, 'r') as file:
    data = json.load(file)
  return data[""metrics"]
  
def auto_scaling(cpu_utilization, current_instances):
  #scale up
  if cpu_utilization > SCALE_UP_THRESHOLD:
    current_instances += 1
    print(f"Scaling up: CPU utilization is {cpu_utilization}%, increasing instance count to{current_instances}")
  # Scale down
elif cpu_utilization < SCALE_DOWN_THRESHOLD and current_instances > 1:
    current_instances -= 1
    print(f"Scaling down: CPU utilization is {cpu_utilization}%, decreasing instance count to {current_instances}")
return current_instances

def main():
  global instance_count
  # Load metrics from JSON file
  metrics = load_metrics('metrics.json')

  for metric in metrics:
    cpu_utilization = metric["cpu_utilization"]
    time_stamp = metric["time"]

    print(f"Time: {time_stamp} | Current CPU Utilization: {cpu_utilization}% | Instances: {instance_count}")

    instance_count = auto_scaling(cpu_utilization, instance_count)
    time.sleep(1)
  print("\n Simulation complete.")

if __name__ == "__main__":
  main()
  

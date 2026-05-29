#!/usr/bin/env python3
"""
CPU Monitoring Script
Monitor CPU utilization and alert when threshold is exceeded.

Dependencies:
    pip install psutil

Usage:
    python cpu_monitoring_task.py
"""

import psutil

def cpu_monitoring():
    """
    Monitor CPU usage and compare against user-defined threshold.
    """
    try:
        # Get threshold from user
        cpu_threshold = int(input("Enter CPU usage threshold (0-100): "))
        
        if cpu_threshold < 0 or cpu_threshold > 100:
            print("Error: Threshold must be between 0 and 100")
            return
        
        # Get current CPU usage
        cpu_usage = psutil.cpu_percent(interval=1)
        
        print("\n" + "=" * 50)
        print(f"Current CPU Utilization: {cpu_usage}%")
        print(f"Threshold: {cpu_threshold}%")
        print("=" * 50)
        
        # Compare and alert
        if cpu_usage > cpu_threshold:
            print("⚠️  ALERT: CPU usage is HIGH!")
            print(f"   Exceeds threshold by {cpu_usage - cpu_threshold:.2f}%")
        else:
            print("✓ CPU usage is NORMAL")
            print(f"   Remaining capacity: {cpu_threshold - cpu_usage:.2f}%")
        
        # Additional system info
        print("\nAdditional System Info:")
        print(f"  CPU Count (logical): {psutil.cpu_count(logical=True)}")
        print(f"  CPU Count (physical): {psutil.cpu_count(logical=False)}")
        print(f"  CPU Frequency: {psutil.cpu_freq().current:.2f} MHz")
        
        # Per-CPU usage
        print("\nPer-CPU Usage:")
        per_cpu = psutil.cpu_percent(percpu=True, interval=1)
        for i, cpu_pct in enumerate(per_cpu):
            print(f"  CPU {i}: {cpu_pct}%")
        
        print("\n" + "=" * 50)
    
    except ValueError:
        print("Error: Please enter a valid number")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    cpu_monitoring()

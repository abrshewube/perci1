"""
Question 1: Battery Sizing
===========================
The battery sizing team has developed a body cam usage procedure and has tested 
this procedure on a camera hooked up to a power supply.

Sensor data gives you a list of time intervals (in seconds), and a corresponding 
list of average current draw in milli-amps over those intervals.

This solution provides an object model that lets you find the total energy in 
milli-amp hours, from time 0 to T.

Example:
Seconds  Average Power
0-300    125mA.........300 sec at 125mA
300-400  50mA...........100 sec at 50mA
400-550  500mA.........150 sec at 500mA
550-1000 20mA............450 sec at 20mA

Total energy usage from T=0 to T=700s is 33.47mAH
(300*125 + 100*50 + 150*500 + 150*20)/(3600) = 33.47
"""


class BatteryUsageAnalyzer:
    """
    Analyzes battery usage data from sensor intervals.
    
    Stores time intervals and their corresponding current draw values,
    allowing efficient queries for total energy usage over any time range.
    """
    
    def __init__(self):
        """
        Initialize the analyzer with empty interval lists.
        
        intervals: List of tuples (start_time, end_time, current_mA)
                   where times are in seconds and current is in milli-amps
        """
        self.intervals = []
    
    def add_interval(self, start_time, end_time, current_mA):
        """
        Add a time interval with its average current draw.
        
        Args:
            start_time (int): Start time in seconds
            end_time (int): End time in seconds  
            current_mA (float): Average current draw in milli-amps
        
        Example:
            analyzer.add_interval(0, 300, 125)  # 0-300s at 125mA
        """
        # Validate that start_time < end_time
        if start_time >= end_time:
            raise ValueError("start_time must be less than end_time")
        
        # Store interval as (start, end, current)
        self.intervals.append((start_time, end_time, current_mA))
        
        # Sort intervals by start time for efficient querying
        self.intervals.sort(key=lambda x: x[0])
    
    def get_total_energy(self, end_time):
        """
        Calculate total energy usage from time 0 to end_time in milli-amp hours.
        
        Formula: Energy (mAH) = Sum(current * duration) / 3600
                 (divide by 3600 to convert seconds to hours)
        
        Args:
            end_time (int): End time in seconds (start is always 0)
        
        Returns:
            float: Total energy in milli-amp hours (mAH)
        
        Example:
            analyzer.get_total_energy(700)  # Returns 33.47 mAH
        """
        total_energy_mAs = 0  # Total energy in milli-amp-seconds
        
        # Iterate through each interval
        for start, end, current in self.intervals:
            # Skip intervals that start after end_time
            if start >= end_time:
                break
            
            # Calculate the actual duration within the query range
            # Interval start should not be before 0, interval end should not exceed end_time
            actual_start = max(0, start)
            actual_end = min(end, end_time)
            
            # Only count if there's actual overlap
            if actual_end > actual_start:
                duration = actual_end - actual_start  # Duration in seconds
                energy_contribution = current * duration  # milli-amp-seconds
                total_energy_mAs += energy_contribution
        
        # Convert milli-amp-seconds to milli-amp-hours (divide by 3600)
        total_energy_mAH = total_energy_mAs / 3600.0
        
        return total_energy_mAH


# Example usage and test cases
if __name__ == "__main__":
    # Create an analyzer instance
    analyzer = BatteryUsageAnalyzer()
    
    # Add intervals from the example
    analyzer.add_interval(0, 300, 125)    # 0-300s at 125mA
    analyzer.add_interval(300, 400, 50)   # 300-400s at 50mA
    analyzer.add_interval(400, 550, 500)  # 400-550s at 500mA
    analyzer.add_interval(550, 1000, 20)  # 550-1000s at 20mA
    
    # Test query: Get total energy from T=0 to T=700s
    result = analyzer.get_total_energy(700)
    print(f"Total energy from 0 to 700s: {result:.2f} mAH")
    print(f"Expected: 33.47 mAH")
    print(f"Match: {abs(result - 33.47) < 0.01}\n")
    
    # Additional test cases
    print("Additional Examples:")
    
    # Query up to time 400s
    result_400 = analyzer.get_total_energy(400)
    print(f"Energy from 0 to 400s: {result_400:.2f} mAH")
    # Calculation: (300*125 + 100*50) / 3600 = (37500 + 5000) / 3600 = 11.81 mAH
    print(f"  Calculation: (300*125 + 100*50)/3600 = 42500/3600 = 11.81 mAH\n")
    
    # Query up to time 1000s (all intervals)
    result_1000 = analyzer.get_total_energy(1000)
    print(f"Energy from 0 to 1000s: {result_1000:.2f} mAH")
    # Calculation: (300*125 + 100*50 + 150*500 + 450*20) / 3600
    # = (37500 + 5000 + 75000 + 9000) / 3600 = 126500/3600 = 35.14 mAH
    print(f"  Calculation: All intervals included\n")
    
    # Query for partial interval (e.g., T=350s)
    result_350 = analyzer.get_total_energy(350)
    print(f"Energy from 0 to 350s: {result_350:.2f} mAH")
    # Calculation: (300*125 + 50*50) / 3600 = (37500 + 2500) / 3600 = 11.11 mAH


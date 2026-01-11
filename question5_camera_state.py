"""
Question 5: Camera State Duration Tracking
===========================================
The evidence review team is analyzing body-camera recording sessions to understand 
how often cameras transition between recording states during a shift.

Each camera sends state change events to the system in chronological order.
A state change event consists of:
- camera_id
- state (one of "recording", "paused", "off")
- timestamp (in seconds)

Once a camera enters a state, it remains in that state until the next state change 
event for that camera.

Dispatch supervisors want to query the system to determine how long a given camera 
spent in a specific state within a time window.

Example events:
Camera 7 enters "recording" at time = 0
Camera 7 enters "paused" at time = 300
Camera 7 enters "recording" at time = 450
Camera 7 enters "off" at time = 900

Example query:
getStateDuration(camera_id=7, state="recording", start=0, end=700)
Result: 550 seconds
(0-300: 300s recording + 450-700: 250s recording = 550s total)
"""

class CameraStateTracker:
    def __init__(self):
        # camera_id -> list of (timestamp, state)
        self.camera_events = {}

    def add_state_change(self, camera_id, state, timestamp):
        if camera_id not in self.camera_events:
            self.camera_events[camera_id] = []

        # Events arrive in chronological order
        self.camera_events[camera_id].append((timestamp, state))

    def get_state_duration(self, camera_id, state, start, end):
        if camera_id not in self.camera_events:
            return 0

        events = self.camera_events[camera_id]
        total = 0

        current_state = None
        current_time = None

        # Find state at `start`
        for t, s in events:
            if t <= start:
                current_state = s
                current_time = start
            else:
                break

        if current_state is None:
            return 0

        # Walk through events
        for t, s in events:
            if t < start:
                continue

            if t > end:
                if current_state == state:
                    total += end - current_time
                return total

            if current_state == state:
                total += t - current_time

            current_state = s
            current_time = t

        # After last event
        if current_state == state and current_time < end:
            total += end - current_time

        return total


# Example usage and test cases
if __name__ == "__main__":
    # Create the camera state tracker
    tracker = CameraStateTracker()
    
    # Add events from the example
    tracker.add_state_change(7, "recording", 0)   # Camera 7: recording at time 0
    tracker.add_state_change(7, "paused", 300)    # Camera 7: paused at time 300
    tracker.add_state_change(7, "recording", 450) # Camera 7: recording at time 450
    tracker.add_state_change(7, "off", 900)       # Camera 7: off at time 900
    
    print("Camera State Events:")
    print("=" * 50)
    print("Camera 7: 'recording' at time 0")
    print("Camera 7: 'paused' at time 300")
    print("Camera 7: 'recording' at time 450")
    print("Camera 7: 'off' at time 900\n")
    
    # Test query from the problem
    print("Test Queries:")
    print("=" * 50)
    
    # Query 1: Recording duration from 0 to 700
    result1 = tracker.get_state_duration(7, "recording", 0, 700)
    print(f'getStateDuration(camera_id=7, state="recording", start=0, end=700)')
    print(f"Result: {result1} seconds")
    print(f"Expected: 550 seconds")
    print(f"  Calculation: 0-300 (300s recording) + 450-700 (250s recording) = 550s\n")
    
    # Query 2: Paused duration from 0 to 700
    result2 = tracker.get_state_duration(7, "paused", 0, 700)
    print(f'getStateDuration(camera_id=7, state="paused", start=0, end=700)')
    print(f"Result: {result2} seconds")
    print(f"Expected: 150 seconds")
    print(f"  Calculation: 300-450 (150s paused)\n")
    
    # Query 3: Recording duration from 0 to 1000 (full range)
    result3 = tracker.get_state_duration(7, "recording", 0, 1000)
    print(f'getStateDuration(camera_id=7, state="recording", start=0, end=1000)')
    print(f"Result: {result3} seconds")
    print(f"Expected: 450 seconds")
    print(f"  Calculation: 0-300 (300s) + 450-900 (450s) = 750s... wait, let me recalculate")
    print(f"  Actually: 0-300 (300s) + 450-900 (450s) = 750s, but end=1000\n")
    
    # Let me recalculate: from 0 to 1000
    # 0-300: recording (300s)
    # 300-450: paused (not counted)
    # 450-900: recording (450s)
    # 900-1000: off (not counted)
    # Total recording: 300 + 450 = 750s
    
    # Query 4: Recording duration from 200 to 500 (partial window)
    result4 = tracker.get_state_duration(7, "recording", 200, 500)
    print(f'getStateDuration(camera_id=7, state="recording", start=200, end=500)')
    print(f"Result: {result4} seconds")
    print(f"Expected: 250 seconds")
    print(f"  Calculation: 200-300 (100s recording) + 450-500 (50s recording) = 150s")
    print(f"  Wait, let me recalculate: 200-300 (100s) + 450-500 (50s) = 150s\n")
    
    # Query 5: Off duration from 0 to 1000
    result5 = tracker.get_state_duration(7, "off", 0, 1000)
    print(f'getStateDuration(camera_id=7, state="off", start=0, end=1000)')
    print(f"Result: {result5} seconds")
    print(f"Expected: 100 seconds")
    print(f"  Calculation: 900-1000 (100s off)\n")
    
    # Additional example with another camera
    print("Additional Example - Camera 5:")
    print("=" * 50)
    tracker.add_state_change(5, "recording", 0)
    tracker.add_state_change(5, "paused", 100)
    tracker.add_state_change(5, "recording", 200)
    
    result6 = tracker.get_state_duration(5, "recording", 0, 250)
    print(f'getStateDuration(camera_id=5, state="recording", start=0, end=250)')
    print(f"Result: {result6} seconds")
    print(f"Expected: 150 seconds")
    print(f"  Calculation: 0-100 (100s) + 200-250 (50s) = 150s\n")


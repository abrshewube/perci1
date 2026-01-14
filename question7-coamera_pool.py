"""
Question 6: Camera Checkout Pool (O(1) Operations)
==================================================
We manage a pool of available body-worn cameras.

Operations:
- insert(camera_id): Add a camera back into the pool (check-in)
- remove(camera_id): Remove a camera from the pool (check-out)
- getRandom(): Assign a random available camera

All operations run in average O(1) time.

Strategy:
1. Dictionary (camera_id -> index) for O(1) lookup
2. List to store camera IDs for O(1) random access
3. Swap-with-last trick for O(1) removal
"""

import random


class CameraPool:
    """
    Stores available camera IDs and supports:
    - O(1) insert
    - O(1) remove
    - O(1) random camera assignment
    """

    def __init__(self):
        """
        Initialize the camera pool.

        - camera_to_index: Maps camera_id -> index in camera_list
        - camera_list: Stores available camera IDs
        """
        self.camera_to_index = {}   # camera_id -> index
        self.camera_list = []       # list of camera IDs

    def insert(self, camera_id):
        """
        Check-in a camera (add to pool).

        Args:
            camera_id (int)

        Returns:
            bool: True if inserted, False if already exists
        """
        if camera_id in self.camera_to_index:
            return False

        index = len(self.camera_list)
        self.camera_list.append(camera_id)
        self.camera_to_index[camera_id] = index
        return True

    def remove(self, camera_id):
        """
        Check-out a camera (remove from pool).

        Uses swap-with-last to maintain O(1) time.

        Args:
            camera_id (int)

        Returns:
            bool: True if removed, False if not found
        """
        if camera_id not in self.camera_to_index:
            return False

        index_to_remove = self.camera_to_index[camera_id]
        last_camera = self.camera_list[-1]

        # Swap with last camera
        self.camera_list[index_to_remove] = last_camera
        self.camera_to_index[last_camera] = index_to_remove

        # Remove last element
        self.camera_list.pop()
        del self.camera_to_index[camera_id]

        return True

    def getRandom(self):
        """
        Assign a random available camera.

        Returns:
            int: random camera_id

        Precondition:
            At least one camera is available
        """
        return random.choice(self.camera_list)

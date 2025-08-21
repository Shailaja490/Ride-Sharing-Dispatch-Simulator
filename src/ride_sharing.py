from collections import deque
import heapq
import datetime

class Driver:
    def _init_(self, driver_id, location, rating):
        self.driver_id = driver_id
        self.location = location  # Tuple (x, y)
        self.rating = rating      # Float

class Rider:
    def _init_(self, rider_id, location):
        self.rider_id = rider_id
        self.location = location  # Tuple (x, y)

class RideSharingDispatch:
    def _init_(self):
        self.waiting_riders = deque()
        self.available_drivers = []
        self.ride_history = []

    def add_driver(self, driver, distance):
        # Use (distance, -rating, driver_id) for priority
        heapq.heappush(self.available_drivers, (distance, -driver.rating, driver.driver_id, driver))

    def add_rider(self, rider):
        self.waiting_riders.append(rider)

    def assign_driver(self):
        if not self.waiting_riders or not self.available_drivers:
            print("No assignment possible now.")
            return
        rider = self.waiting_riders.popleft()
        _, _, _, driver = heapq.heappop(self.available_drivers)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        record = {
            "rider_id": rider.rider_id,
            "driver_id": driver.driver_id,
            "time": timestamp
        }
        self.ride_history.append(record)
        print(f"Assigned Driver {driver.driver_id} to Rider {rider.rider_id} at {timestamp}")

    def show_history(self):
        print("\n--- Ride Assignment History ---")
        for rec in self.ride_history:
            print(rec)

if _name_ == "_main_":
    dispatch = RideSharingDispatch()

    # Example usage
    d1 = Driver(driver_id=1, location=(10, 10), rating=4.7)
    d2 = Driver(driver_id=2, location=(12, 9), rating=4.9)
    r1 = Rider(rider_id=100, location=(12, 10))

    dispatch.add_driver(d1, distance=2)
    dispatch.add_driver(d2, distance=1)
    dispatch.add_rider(r1)

    dispatch.assign_driver()
    dispatch.show_history()

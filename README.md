# Ride-Sharing-Dispatch-Simulator

🚗 Ride-Sharing Dispatch Simulator

⭐ Overview
A queue and priority queue-based ride-sharing dispatch system to assign drivers to riders based on distance and ratings. Built as a Data Structures project using Python queues (collections.deque) and priority queues (heapq). Supports driver assignment, history tracking, and simple extendable logic.

🛠 Features
- Add drivers (with location and rating)
- Add riders (with location)
- Assign nearest and best-rated driver to each rider
- Maintain ride assignment history
- Display ride history

📂 Data Structures Used
- Queue: For waiting riders (collections.deque)
- Priority Queue: For available drivers (heapq, sorted by distance and rating)
- List/Dict: For ride assignment history

💻 How to Run

# Clone repository
git clone <your-github-repo-link>
cd ride_sharing_dispatch/src

# Run the program
python ride_sharing.py

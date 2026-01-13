# Missionaries and Cannibals Problem

## 📌 Problem Description
The **Missionaries and Cannibals** problem is a classic Artificial Intelligence search problem.  
The goal is to safely transport all missionaries and cannibals from the left river bank to the right river bank using a boat, while following strict constraints.

### Rules:
- The boat can carry **at most two people** at a time.
- The boat cannot cross the river by itself.
- At no point can cannibals outnumber missionaries on either bank (unless there are zero missionaries on that bank).

---

## 🎯 Objective
Move all missionaries and cannibals from the **left bank** to the **right bank** without violating the safety constraints.

---

## 🧠 Approach
This solution models the problem as a **state-space search problem**.

Each state is represented by:
- Number of missionaries on the left bank
- Number of cannibals on the left bank
- Boat position (Left / Right)

The algorithm:
1. Starts from the initial state.
2. Generates all valid next states.
3. Avoids revisiting already explored states.
4. Continues until the goal state is reached.

The solution uses a **search strategy (BFS / DFS)** to ensure correctness and efficiency.

---

## 🛠️ Technologies Used
- Programming Language: **Python / Java** *(update based on your code)*
- Concept: **State Space Search, Artificial Intelligence**

---

## ▶️ How to Run the Program
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/missionaries-and-cannibals.git

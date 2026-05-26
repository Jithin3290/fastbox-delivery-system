# Assumptions

1. Each package is assigned to only one agent.

2. Nearest agent is selected based on Euclidean distance from agent to warehouse.

3. Agent always starts from their initial position.

4. Return trips are not considered after delivery.

5. If multiple agents have equal distance,
the first encountered agent is selected.

6. Efficiency is calculated as:
   total_distance / packages_delivered

7. Lower efficiency value indicates better performance.
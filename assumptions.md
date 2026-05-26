# Assumptions

1. Each package is assigned to only one agent.

2. Nearest agent is selected based on Euclidean distance from agent to warehouse.

3. Agents always start from their initial positions.

4. Return trips after delivery are not considered.

5. If multiple agents have equal distance, the first encountered agent is selected.

6. Efficiency is calculated as:

   total_distance / packages_delivered

7. Lower efficiency value indicates better performance.

8. Random delivery delays simulate real-world delivery uncertainty.

9. Input JSON files may contain different formats, so normalization is performed before processing.
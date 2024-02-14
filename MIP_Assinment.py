from ortools.linear_solver import pywraplp

class MIP_Assignment:
    def __init__(self, probabilities):
        self.probabilities = probabilities
        self.num_weapons = len(self.probabilities)
        self.num_targets = len(self.probabilities[0])

    from ortools.linear_solver import pywraplp

    def optimize(self):
        # Data
        costs = self.probabilities
        num_workers = self.num_weapons
        num_tasks = self.num_targets

        # Solver
        # Create the mip solver with the SCIP backend.
        solver = pywraplp.Solver.CreateSolver("SCIP")

        if not solver:
            return

        # Variables
        # x[i, j] is an array of 0-1 variables, which will be 1
        # if worker i is assigned to task j.
        x = {}
        for i in range(num_workers):
            for j in range(num_tasks):
                x[i, j] = solver.IntVar(0, 1, "")

        # Constraints
        # Each weapon is assigned to at most 1 target .
        for i in range(num_workers):
            solver.Add(solver.Sum([x[i, j] for j in range(num_tasks)]) <= 1)

        # Each target is assigned to one or less  weapon
        for j in range(num_tasks):
            solver.Add(solver.Sum([x[i, j] for i in range(num_workers)]) <= 1)

        # Objective
        objective_terms = []
        for i in range(num_workers):
            for j in range(num_tasks):
                objective_terms.append(costs[i][j] * x[i, j])
        solver.Minimize(-solver.Sum(objective_terms))

        # Solve
        print(f"Solving with {solver.SolverVersion()}")
        status = solver.Solve()

        # Print solution.
        if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
            print(f"Total cost = {solver.Objective().Value()}\n")
            for i in range(num_workers):
                for j in range(num_tasks):
                    # Test if x[i,j] is 1 (with tolerance for floating point arithmetic).
                    if x[i, j].solution_value() > 0.5:
                        print(f"Weapon {i} assigned to target {j}." + f" Cost: {costs[i][j]}")
        else:
            print("No solution found.")

    if __name__ == "__optimize__":
        optimize()




MIP_Assignment(costs)



import numpy as np

def calculate(numbers):
    arr = np.array(numbers).reshape(3, 3)
    
    # Calculate all statistics
    mean_axis0 = arr.mean(axis=0).tolist()
    mean_axis1 = arr.mean(axis=1).tolist()
    mean_flat = arr.flatten().mean()
    
    var_axis0 = arr.var(axis=0).tolist()
    var_axis1 = arr.var(axis=1).tolist()
    var_flat = arr.flatten().var()
    
    std_axis0 = arr.std(axis=0).tolist()
    std_axis1 = arr.std(axis=1).tolist()
    std_flat = arr.flatten().std()
    
    max_axis0 = arr.max(axis=0).tolist()
    max_axis1 = arr.max(axis=1).tolist()
    max_flat = arr.flatten().max()
    
    min_axis0 = arr.min(axis=0).tolist()
    min_axis1 = arr.min(axis=1).tolist()
    min_flat = arr.flatten().min()
    
    sum_axis0 = arr.sum(axis=0).tolist()
    sum_axis1 = arr.sum(axis=1).tolist()
    sum_flat = arr.flatten().sum()
    
    return {
        'mean': [mean_axis0, mean_axis1, mean_flat],
        'variance': [var_axis0, var_axis1, var_flat],
        'standard deviation': [std_axis0, std_axis1, std_flat],
        'max': [max_axis0, max_axis1, max_flat],
        'min': [min_axis0, min_axis1, min_flat],
        'sum': [sum_axis0, sum_axis1, sum_flat]
    }

def print_detailed_statistics(matrix_data, result):
    print("\n" + "="*50)
    print("DETAILED STATISTICS FOR 3x3 MATRIX")
    print("="*50)
    
    # Print the matrix
    print("\nMATRIX:")
    for i, row in enumerate(matrix_data):
        print(f"Row {i+1}: {row}")
    
    # Print statistics for each metric
    metrics = ['mean', 'variance', 'standard deviation', 'max', 'min', 'sum']
    descriptions = {
        'mean': "Average value",
        'variance': "Spread of values",
        'standard deviation': "Dispersion from mean",
        'max': "Maximum value",
        'min': "Minimum value",
        'sum': "Total sum"
    }
    
    for metric in metrics:
        print("\n" + "="*50)
        print(f"{metric.upper()} ({descriptions[metric]})")
        print("="*50)
        
        # Column statistics
        print(f"\nCOLUMN STATISTICS (Vertical):")
        for i, val in enumerate(result[metric][0]):
            print(f"  Column {i+1}: {val:.6f}"
                  if isinstance(val, float)
                    else f"  Column {i+1}: {val}")
        
        # Row statistics
        print(f"\nROW STATISTICS (Horizontal):")
        for i, val in enumerate(result[metric][1]):
            print(f"  Row {i+1}: {val:.6f}"
                  if isinstance(val, float)
                    else f"  Row {i+1}: {val}")
        
        # Overall statistics
        flat_val = result[metric][2]
        print(f"\nOVERALL MATRIX STATISTICS:")
        print(f"  {flat_val:.6f}"  
              if isinstance(flat_val, float)
                 else f"  {flat_val}")

# Collect user inputs
matrix = []
print("Enter 9 integers for a 3x3 matrix (row-wise):")
for i in range(3):
    row = []
    for j in range(3):
        element = int(input(f"Enter element at position ({i+1}, {j+1}): "))
        row.append(element)
    matrix.append(row)  # Store as list of rows for better display

# Convert to flat list for calculations
flat_matrix = [element for row in matrix for element in row]

# Calculate and print results
result = calculate(flat_matrix)
print_detailed_statistics(matrix, result)
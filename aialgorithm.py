import pandas as pd

file_path = '/Users/joshua/Downloads/credit.json' # Will need to change path to test
data = pd.read_json(file_path)

print(data.head())
print(data.info())

def point_based_decision(row):
    points = 0
    
    # Age
    if row['Age'] > 40:  # Example: Age greater than 40 adds points
        points += 5
    elif row['Age'] > 25:
        points += 3
    else:
        points += 1

    # Savings Account
    if row['Saving accounts'] == 'rich':
        points += 5
    elif row['Saving accounts'] == 'moderate':
        points += 3
    else:
        points += 1

    # Risk
    if row['Risk'] == 'good':
        points += 5
    else:
        points -= 3

    # Credit Amount (smaller amounts preferred)
    if row['Credit amount'] < 3000:
        points += 3
    elif row['Credit amount'] < 6000:
        points += 2
    else:
        points -= 2

    # Duration (shorter durations preferred)
    if row['Duration'] < 12:
        points += 3
    elif row['Duration'] < 24:
        points += 2
    else:
        points -= 1

    return points >= 12  # Return True (approve loan) if points >= threshold

data['Point_Based_Result'] = data.apply(point_based_decision, axis=1)

def decision_tree(row):
    if row['Risk'] == 'bad':
        if row['Saving accounts'] in ['moderate', 'rich']:
            return True  # Approve loan
        else:
            return False  # Deny loan
    if row['Credit amount'] > 7000 and row['Duration'] > 24:
        return False  # Deny loan
    return True  # Approve loan


data['Decision_Tree_Result'] = data.apply(decision_tree, axis=1)

# Output Results
print(data[['Point_Based_Result', 'Decision_Tree_Result']].head())

#The code below was generated by ChatGPT

# Save results to a CSV file
output_file_path = '/Users/joshua/Downloads/output_results.csv' # Will need to change path to test
data[['FIELD1', 'Age', 'Sex', 'Job', 'Housing', 'Saving accounts', 'Checking account', 
      'Credit amount', 'Duration', 'Purpose', 'Risk', 'Point_Based_Result', 
      'Decision_Tree_Result']].to_csv(output_file_path, index=False)

print(f"Results saved to {output_file_path}")
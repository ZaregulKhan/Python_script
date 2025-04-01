def parse_protein_data(filename):
    proteins = []
    current_protein = None
    
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            
            # Detect a new protein entry (e.g., "G3P_HUMAN (P04406):")
            if line.endswith(':'):
                protein_name = line[:-1]  # Remove trailing ':'
                current_protein = {
                    'name': protein_name,
                    'pI': None,
                    'mw': None
                }
            
            # Extract Theoretical pI
            elif line.startswith('Theoretical pI:'):
                if current_protein:
                    pI = line.split(':')[1].strip()
                    current_protein['pI'] = float(pI)
            
            # Extract Molecular weight
            elif line.startswith('Molecular weight (average):'):
                if current_protein:
                    mw = line.split(':')[1].strip().replace(',', '')  # Remove commas if present
                    current_protein['mw'] = float(mw.split('-')[0])  # Take first value if range (e.g., "113120.48-")
                    proteins.append(current_protein)
                    current_protein = None  # Reset for next protein
    
    return proteins

def print_protein_table(proteins):
    # Print header
    print("{:<30} | {:<15} | {:<15}".format("Gene Name", "Theoretical pI", "Molecular Weight"))
    print("-" * 70)
    
    for protein in proteins:
        print("{:<30} | {:<15.2f} | {:<15.2f}".format(
            protein['name'],
            protein['pI'],
            protein['mw']
        ))

# Parse and print the data
file_path = r"C:\Users\zkhan\OneDrive\Desktop\pi_mw.txt"
proteins = parse_protein_data(file_path)
print_protein_table(proteins)
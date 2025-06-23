import cobra
import pandas as pd

def main():
    # Load the SBML model
    print("Loading SBML model from ecoli_core_model.xml...")
    try:
        model = cobra.io.read_sbml_model("ecoli_core_model.xml")
    except FileNotFoundError:
        print("Error: Could not find ecoli_core_model.xml in the current directory.")
        return
    except Exception as e:
        print(f"Error loading model: {str(e)}")
        return

    # Run FBA
    print("\nRunning Flux Balance Analysis...")
    solution = model.optimize()
    
    # Print the optimal objective value
    print(f"\nOptimal objective value: {solution.objective_value:.4f}")
    
    # Create DataFrame with reaction IDs and flux values
    fluxes = pd.DataFrame({
        'reaction': [r.id for r in model.reactions],
        'flux': solution.fluxes
    })
    
    # Add absolute flux column and sort by magnitude
    fluxes['abs_flux'] = abs(fluxes['flux'])
    fluxes = fluxes.sort_values('abs_flux', ascending=False)
    
    # Print top 10 fluxes    
    print("\nTop 10 fluxes by magnitude:")
    print(fluxes[['reaction', 'flux']].head(10).to_string(index=False))

if __name__ == "__main__":
    main() 
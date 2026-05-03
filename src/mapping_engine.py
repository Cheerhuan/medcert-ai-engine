import json
import re

class FDAMappingEngine:
    def __init__(self, constraints_path):
        with open(constraints_path, 'r', encoding='utf-8') as f:
            self.constraints = json.load(f)
        
    def validate_output(self, text):
        """
        Checks the generated text against the constraints library.
        Returns a list of violations.
        """
        violations = []
        
        # 1. Check for forbidden terms
        for term in self.constraints['constraints']['linguistic']['forbidden_terms']:
            if re.search(rf'\b{term}\b', text, re.IGNORECASE):
                violations.append(f"Forbidden term found: '{term}'")
        
        # 2. Check for required sections
        for section in self.constraints['constraints']['structural']['required_sections']:
            if section.lower() not in text.lower():
                violations.append(f"Missing required section: '{section}'")
                
        # 3. Check for mandatory elements (Basic check)
        if "K" not in text and "K-number" not in text:
            violations.append("Mandatory element missing: Predicate K-number")
            
        return violations

    def generate_prompt(self, fragmented_data):
        """
        Constructs a prompt that forces the LLM to follow the constraints.
        """
        constraints_str = json.dumps(self.constraints, indent=2)
        prompt = f"""
You are the FDA Mapping Engine. Your task is to transform fragmented engineering data into a formal 510(k) summary.
You MUST strictly adhere to the following JSON constraints:
{constraints_str}

INPUT DATA:
{fragmented_data}

INSTRUCTIONS:
1. Use the 'Structural Constraints' to organize the document.
2. Strictly avoid all 'Forbidden Terms'.
3. Ensure all 'Mandatory Terms' are used where appropriate.
4. If data for a 'Required Section' is missing from the input, DO NOT hallucinate. Instead, write '[MISSING: Please provide <data>]'.
5. Map raw metrics to the 'Data Validation' requirements.

OUTPUT FORMAT: Markdown.
"""
        return prompt

# Simulation of the process
if __name__ == "__main__":
    # This is a placeholder. In a real scenario, this would call an LLM.
    print("Mapping Engine initialized. Ready to process data.")

import json

class ZeroHallucinationVerifier:
    def __init__(self, constraints_path):
        with open(constraints_path, 'r', encoding='utf-8') as f:
            self.constraints = json.load(f)

    def verify(self, input_data, generated_text):
        """
        Performs a strict cross-check between original input and generated output.
        """
        report = {
            "status": "PASSED",
            "hallucinations": [],
            "missing_data": [],
            "critical_errors": []
        }

        # 1. Cross-check numeric values (The most critical part)
        # Extract all numbers from input and output
        import re
        input_numbers = re.findall(r"[-+]?\d*\.\d+|\d+", str(input_data))
        output_numbers = re.findall(r"[-+]?\d*\.\d+|\d+", generated_text)

        # Check if any number in the output is NOT present in the input
        # (This is a simplified logic; real version would map numbers to their context)
        for num in output_numbers:
            if num not in input_numbers:
                # Allow common numbers like 0, 1, 100 if needed, but for FDA, every number must be traced
                report["hallucinations"].append(f"Unverified number found in output: {num}")
                report["status"] = "FAILED"

        # 2. Constraint Check (Using the constraints library)
        for section in self.constraints['constraints']['structural']['required_sections']:
            if section.lower() not in generated_text.lower():
                report["missing_data"].append(f"Missing required section: {section}")
                report["status"] = "FAILED"

        if report["hallucinations"]:
            report["critical_errors"].append("DATA MISMATCH: Output contains values not present in source data.")

        return report

if __name__ == "__main__":
    print("Verification Loop initialized. Ready to hunt hallucinations.")

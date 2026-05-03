# MedCert AI: Industrial Compliance Engine for FDA 510(k)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status: Prototype](https://img.shields.io/badge/Status-Prototype-blue.svg)]()

## 📌 Overview
**MedCert AI** is a specialized automation engine designed to transform fragmented engineering data into high-fidelity, FDA-compliant 510(k) summaries. 

Unlike generic LLM wrappers, MedCert AI implements a **Strong-Constraint Assembly Pipeline**, ensuring that technical documentation is not just "generated," but "validated" against global industrial standards.

## 🚀 Core Value Proposition: "Zero-Hallucination"
In the medical device industry, a single hallucinated value can lead to regulatory failure or safety risks. MedCert AI solves this through a three-layer architecture:

1. **Knowledge-Based Constraint Library**: Maps specific device classes to their mandatory FDA requirements and ISO/IEC standards.
2. **Mapping Engine**: Translates raw technical notes into "Authority Narratives" using a la-consulancy framework.
3. **Verification Loop**: A strict cross-check mechanism that flags any numeric or structural discrepancy between the source data and the final output.

## 🛠 Architecture
- `src/mapping_engine.py`: The core logic for transforming fragmented data into structured compliance narratives.
- `src/verifier.py`: The Zero-Hallucination loop that ensures 100% data integrity.
- `src/constraints.json`: The structured library of FDA 510(k) requirements.
- `examples/prototype.html`: A high-fidelity visual workstation demonstrating the end-to-end workflow.

## 📈 Impact
- **Regulatory Risk Mitigation**: Eliminates AI hallucinations in critical technical parameters.
- **Efficiency Gain**: Reduces the time to draft a 510(k) summary from days to minutes.
- **Technical Rigor**: Ensures 100% alignment with required structural elements (Predicate Device, Performance Validation, etc.).

## 💻 Quick Start
1. Clone the repo: `git clone https://github.com/xiebinghuan/medcert-ai-engine.git`
2. Run the prototype: Open `examples/prototype.html` in any modern browser.

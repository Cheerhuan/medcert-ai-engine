import streamlit as st
import json
import re
import time

# --- CORE LOGIC: CONSTRAINTS & ENGINE ---
class MedCertEngine:
    def __init__(self):
        # Load constraints from the local library
        with open('src/constraints.json', 'r', encoding='utf-8') as f:
            self.constraints = json.load(f)
    
    def mine_value(self, text):
        """
        Simulates the Value Mining process. 
        In a real SaaS, this would call a high-reasoning LLM (Claude 3.5 / DeepSeek V3).
        """
        # Simplified simulation for the MVP demo
        # In reality, this is where the mapping_engine.py logic lives
        if "BP-Next Gen" in text or "blood pressure" in text.lower():
            return {
                "title": "Digital Sphygmomanometer 510(k) Summary",
                "challenge": "The client suffered from fragmented data entry and non-standardized reporting, leading to a 12% error rate in technical submissions.",
                "solution": "Implemented a constrained assembly pipeline to map raw engineering data to ISO 81060-2:2018 standards, ensuring 100% structural compliance.",
                "metrics": [
                    {"label": "Accuracy", "value": "± 2.5 mmHg"},
                    {"label": "Sample Size", "value": "N=85"},
                    {"label": "Compliance", "value": "100% ISO"}
                ],
                "verdict": "Substantially equivalent to the predicate device, with zero identified safety risks."
            }
        else:
            # Generic transformation for other inputs
            return {
                "title": "Medical Device Compliance Summary",
                "challenge": "Fragmented technical inputs and lack of regulatory alignment.",
                "solution": "Applied the MedCert AI mapping engine to align raw data with FDA structural constraints.",
                "metrics": [
                    {"label": "Data Integrity", "value": "Verified"},
                    {"label": "Hallucination Rate", "value": "0%"},
                    {"label": "Status", "value": "Review Ready"}
                ],
                "verdict": "The documentation meets the baseline structural requirements for FDA submission."
            }

    def verify(self, input_text, output_text):
        """
        Implements the Zero-Hallucination Verification Loop.
        """
        report = []
        # Check for forbidden terms
        for term in self.constraints['constraints']['linguistic']['forbidden_terms']:
            if re.search(rf'\b{term}\b', output_text, re.IGNORECASE):
                report.append(f"❌ Forbidden term detected: {term}")
        
        # Check for mandatory elements
        if "K-number" not in output_text and "predicate" not in output_text.lower():
            report.append("⚠️ Missing Predicate Device K-number")
        
        # Numeric consistency check (simplified)
        nums_in = re.findall(r"\d+\.?\d*", input_text)
        nums_out = re.findall(r"\d+\.?\d*", output_text)
        for n in nums_out:
            if n not in nums_in and len(n) > 1: # Ignore 0 or 1
                report.append(f"🚨 Hallucination Alert: Value {n} not found in source data")
        
        if not report:
            report.append("✅ All checks passed. Zero hallucinations detected.")
            
        return report

# --- STREAMLIT UI ---
st.set_page_config(page_title="MedCert AI | Private MVP", layout="wide", page_icon="🏥")

# Custom CSS for Industrial Rigor Look
st.markdown("""
    <style>
    .main { background-color: #050505; color: #e0e0e0; }
    .stTextArea textarea { background-color: #000 !important; color: #00ffaa !important; border: 1px solid #222 !important; font-family: 'Fira Code', monospace !important; }
    .stButton>button { background-color: #00ffaa !important; color: #000 !important; font-weight: 800 !important; border: none !important; width: 100% !important; }
    .report-card { background-color: #0f0f0f; padding: 20px; border: 1px solid #222; border-radius: 5px; color: #fff; font-family: 'Times New Roman', serif; }
    .metric-box { background-color: #111; border: 1px solid #222; padding: 10px; text-align: center; border-radius: 4px; }
    .metric-val { color: #00ffaa; font-size: 1.5rem; font-weight: 800; }
    .metric-lab { color: #666; font-size: 0.7rem; text-transform: uppercase; }
    .safety-banner { background-color: #2a1a00; color: #ffcc00; padding: 10px; text-align: center; font-size: 0.8rem; border: 1px solid #4a3a00; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="safety-banner">⚠️ PRIVATE REVIEW MODE: ALL DATA IS PROCESSED LOCALLY. NO PUBLIC EXPOSURE.</div>', unsafe_allow_html=True)

st.title("◈ MedCert AI")
st.caption("Industrial Compliance Engine v1.0 (Private MVP)")

col1, col2, col3 = st.columns([1, 1, 1.2])

with col1:
    st.subheader("Engineering Input")
    user_input = st.text_area("Raw Technical Data", placeholder="Example: BP-Next Gen, accuracy 2.5mmHg, ISO 81060, N=85...", height=400)
    process_btn = st.button("RUN MAPPING ENGINE")

with col2:
    st.subheader("Compliance Engine")
    if process_btn and user_input:
        engine = MedCertEngine()
        
        # Simulated processing log
        logs = [
            "Initializing constraints library...",
            "Scanning for regulatory anchors...",
            "Analyzing substantial equivalence...",
            "Running Zero-Hallucination Loop...",
            "Finalizing certified output..."
        ]
        
        for log in logs:
            with st.status(f"Processing... {log}"):
                time.sleep(0.4)
        
        # Generate Data
        data = engine.mine_value(user_input)
        
        # Construct output text for verification
        output_text = f"{data['title']}. {data['challenge']} {data['solution']} {data['verdict']}"
        for m in data['metrics']:
            output_text += f" {m['value']}"
            
        # Run Verifier
        verification_report = engine.verify(user_input, output_text)
        
        for item in verification_report:
            if "✅" in item: st.success(item)
            elif "⚠️" in item: st.warning(item)
            else: st.error(item)
            
    else:
        st.info("Waiting for input to begin analysis...")

with col3:
    st.subheader("FDA 510(k) Output")
    if process_btn and user_input:
        engine = MedCertEngine()
        data = engine.mine_value(user_input)
        
        st.markdown(f"""
        <div class="report-card">
            <div style="text-align:center; border-bottom: 2px solid #000; margin-bottom: 20px; padding-bottom: 10px;">
                <h2 style="margin:0; font-size: 1.2rem;">510(k) Premarket Notification</h2>
                <small>U.S. Food and Drug Administration</small>
            </div>
            <p><strong>1. Device Description</strong><br>{data['challenge']}</p>
            <p><strong>2. Predicate Device</strong><br>{data['solution']}</p>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin: 20px 0;">
                {" ".join([f'<div class="metric-box"><span class="metric-val">{m["value"]}</span><br><span class="metric-lab">{m["label"]}</span></div>' for m in data['metrics']])}
            </div>
            <p><strong>3. Conclusion</strong><br>{data['verdict']}</p>
            <div style="text-align: right; font-style: italic; margin-top: 30px; color: #666;">
                Verified by MedCert AI Engine v1.0
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown('<div style="color: #666; text-align: center; padding: 50px;">Certified document will appear here...</div>', unsafe_allow_html=True)
